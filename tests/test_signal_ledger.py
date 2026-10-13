import json
from pathlib import Path
import pytest
from gltest.direct import VMContext, deploy_contract, create_address

CONTRACT = Path(__file__).parents[1] / 'contracts/signal_ledger.py'
URL = 'https://status.example.com/incidents/sample'
PAGE = '2026-10-13T05:00:00Z Payment API in Europe is unavailable. We are investigating.'
QUOTE = 'Payment API in Europe is unavailable.'

@pytest.fixture
def env():
    vm = VMContext()
    vm._chain_id = 61999
    vm.sender = create_address('owner')
    vm.warp('2026-10-13T05:10:00Z')
    with vm.activate():
        contract = deploy_contract(CONTRACT, vm, sdk_version='v0.2.16')
        yield vm, contract

def mock(vm, signal='OUTAGE', stamp='2026-10-13T05:00:00Z', quote=QUOTE, page=PAGE):
    vm.clear_mocks()
    vm.mock_web('status.example.com', {'status': 200, 'body': page})
    vm.mock_llm('Classify a service', json.dumps({'signal':signal, 'updated_at':stamp, 'quote':quote}))

def advance(vm, stamp):
    # gltest 0.29.2 warp updates VM datetime but not SDK message_raw cache.
    vm.warp(stamp)
    from genlayer import gl
    gl.message_raw['datetime'] = stamp

def setup(c):
    c.create_monitor('payment-eu','Payment API in Europe',URL)

def read(c):
    return json.loads(c.get_monitor('payment-eu'))

def test_create_and_duplicate(env):
    vm,c=env;setup(c)
    assert read(c)['state']=='UNKNOWN' and c.get_count()==1
    with pytest.raises(Exception): setup(c)

@pytest.mark.parametrize('url', ['http://status.example.com','https://127.0.0.1','https://localhost/a','https://host.internal/a','https://user@site.com','https://site.com:443','https://site.com?a=b','https://site.com/#x','https://bad..com','https://a.local/a','https://1.2.3.4/'])
def test_bad_urls(env,url):
    vm,c=env
    with pytest.raises(Exception): c.create_monitor('x','Service',url)

@pytest.mark.parametrize('mid,scope', [('X','Service'),('bad id','Service'),('x',''),('x','x'*161),('x','ignore\ntext')])
def test_input_limits(env,mid,scope):
    vm,c=env
    with pytest.raises(Exception): c.create_monitor(mid,scope,URL)

def test_outage_and_independent_validator(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    assert read(c)['state']=='OUTAGE'
    assert vm.run_validator() is True
    mock(vm,'DEGRADED')
    assert vm.run_validator() is False

def test_forged_and_failed_leader(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    for x in [None,{}, {'signal':'OUTAGE'}, {'signal':'OUTAGE','updated_at':'2026-10-13T05:00:00Z','quote':'invented source excerpt','source_sha256':'a'*64}]:
        assert vm.run_validator(leader_result=x) is False
    assert vm.run_validator(leader_error=ValueError('failed')) is False

def test_validator_independent_source_failure(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    mock(vm,page='')
    assert vm.run_validator() is False

def test_unknown_preserves_outage(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    advance(vm, '2026-10-13T05:12:00Z');mock(vm,'UNKNOWN','','');c.check('payment-eu',1)
    assert read(c)['state']=='OUTAGE'
    rec=json.loads(c.get_record('payment-eu',2))
    assert rec['signal']=='UNKNOWN' and rec['disposition']=='INSUFFICIENT_EVIDENCE'
    assert vm.run_validator()

def test_recovery_and_revision(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    advance(vm, '2026-10-13T05:12:00Z')
    page='2026-10-13T05:11:00Z Payment API in Europe is fully restored.'
    mock(vm,'OPERATIONAL','2026-10-13T05:11:00Z','Payment API in Europe is fully restored.',page)
    c.check('payment-eu',1)
    assert read(c)['state']=='OPERATIONAL' and vm.run_validator()
    assert json.loads(c.get_record('payment-eu',2))['before']=='OUTAGE'
    with pytest.raises(Exception): c.check('payment-eu',1)

def test_permissions_and_cooldown(env):
    vm,c=env;setup(c);mock(vm)
    vm.sender=create_address('stranger')
    with pytest.raises(Exception): c.check('payment-eu',0)
    vm.sender=create_address('owner');c.check('payment-eu',0)
    with pytest.raises(Exception): c.check('payment-eu',1)
    assert read(c)['revision']==1

@pytest.mark.parametrize('signal,stamp,quote,page',[
 ('HEALTHY','2026-10-13T05:00:00Z',QUOTE,PAGE),
 ('OUTAGE','2026-10-14T05:00:00Z',QUOTE,PAGE),
 ('OUTAGE','2026-10-01T05:00:00Z',QUOTE,PAGE),
 ('OUTAGE','2026-02-30T05:00:00Z',QUOTE,PAGE),
 ('OUTAGE','missing',QUOTE,PAGE),('OUTAGE','2026-10-13T05:00:00Z','invented quote',PAGE),
 ('UNKNOWN','2026-10-13T05:00:00Z','',PAGE),('UNKNOWN','','', ''),
 ('UNKNOWN','','','x'*24001)])
def test_failed_observation_no_mutation(env,signal,stamp,quote,page):
    vm,c=env;setup(c);before=read(c);mock(vm,signal,stamp,quote,page)
    with pytest.raises(Exception): c.check('payment-eu',0)
    assert read(c)==before

def test_backdated_and_same_time_conflict(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    advance(vm, '2026-10-13T05:12:00Z')
    for stamp in ['2026-10-13T04:00:00Z','2026-10-13T05:00:00Z']:
        mock(vm,'OPERATIONAL',stamp,QUOTE)
        with pytest.raises(Exception): c.check('payment-eu',1)
        assert read(c)['state']=='OUTAGE' and read(c)['revision']==1

def test_unknown_reads(env):
    vm,c=env
    with pytest.raises(Exception): c.get_monitor('missing')
    with pytest.raises(Exception): c.get_record('missing',1)

@pytest.mark.parametrize('signal', ['OPERATIONAL','DEGRADED','MAINTENANCE'])
def test_other_states_and_confirmation(env,signal):
    vm,c=env;setup(c);mock(vm,signal);c.check('payment-eu',0)
    assert read(c)['state']==signal and vm.run_validator()
    advance(vm,'2026-10-13T05:12:00Z');c.check('payment-eu',1)
    assert json.loads(c.get_record('payment-eu',2))['disposition']=='CONFIRMED'

def test_validator_rejects_hash_forgery(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    proposed=dict(vm._captured_validators[-1][0]);proposed['source_sha256']='a'*64
    assert vm.run_validator(leader_result=proposed) is False

def test_monitor_capacity(env):
    vm,c=env
    for n in range(128): c.create_monitor('m'+str(n),'Service',URL)
    with pytest.raises(Exception,match='capacity'): c.create_monitor('overflow','Service',URL)
    assert c.get_count()==128

def test_history_capacity(env):
    vm,c=env;setup(c);mock(vm,'UNKNOWN','','')
    from datetime import datetime,timedelta,timezone
    start=datetime(2026,10,13,5,10,tzinfo=timezone.utc)
    for n in range(256):
        advance(vm,(start+timedelta(minutes=n)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        c.check('payment-eu',n)
    advance(vm,(start+timedelta(minutes=256)).strftime('%Y-%m-%dT%H:%M:%SZ'))
    with pytest.raises(Exception,match='capacity'): c.check('payment-eu',256)
    assert read(c)['revision']==256

def test_rejected_consensus_leaves_state_unchanged(env,monkeypatch):
    vm,c=env;setup(c);mock(vm);before=read(c)
    from genlayer import gl
    def rejecting(leader,validator):
        proposed=leader()
        mock(vm,'DEGRADED')
        assert validator(gl.vm.Return(proposed)) is False
        raise gl.vm.UserError('No consensus')
    monkeypatch.setattr(gl.vm,'run_nondet_unsafe',rejecting)
    with pytest.raises(Exception,match='No consensus'): c.check('payment-eu',0)
    assert read(c)==before

def test_consensus_closures_serializable(env):
    vm,c=env;setup(c);mock(vm);c.check('payment-eu',0)
    import cloudpickle
    _,leader,validator=vm._captured_validators[-1]
    assert cloudpickle.dumps(leader) and cloudpickle.dumps(validator)
