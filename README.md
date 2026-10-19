> **Steward remediation candidate — NOT DEPLOYED.** This branch contains the proposed owner-scoped quota fix. The contract address and onchain evidence below describe the previous deployment. Do not resubmit until the candidate is deployed and its source hash is verified.

# SignalLedger Primitive

A reusable GenLayer Intelligent Contract that converts **scope-bound natural-language service announcements** into a guarded state history. The state describes what a selected source announces, not measured network uptime.

A service can return HTTP 200 while its announcement describes a regional outage. A different component can be down while the target scope is healthy. SignalLedger independently interprets that distinction and prevents incomplete evidence from manufacturing a recovery.

## Mechanism

1. An owner registers an immutable monitor ID, exact service/component/region and public source URL.
2. The leader retrieves the announcement and classifies its latest dated, scoped update.
3. Each validator retrieves the source independently and runs its own LLM classification. The status and update time must agree; the leader's excerpt must appear in the validator's source. The complete source digest must match, conservatively rejecting source drift.
4. Only the accepted decision reaches deterministic storage. Older updates and contradictory same-time updates revert. UNKNOWN records insufficient evidence and preserves the last accepted state.

States: `UNKNOWN`, `OPERATIONAL`, `DEGRADED`, `OUTAGE`, `MAINTENANCE`. No arbitrary user-supplied status setter exists.

## API

| Method | Purpose |
|---|---|
| `create_monitor(id, scope, url)` | Create immutable, owner-bound scope and source |
| `check(id, expected_revision)` | Owner requests independent semantic consensus |
| `get_monitor(owner::id)` | JSON monitor state; public reference is owner-address plus `::` plus ID |
| `get_record(owner::id, revision)` | JSON observation, transition, excerpt and digest |
| `get_count()` | Aggregate count across all owners; informational, not a shared cap |
| `get_owner_count(owner)` | Number of monitors owned by one address |

## Network and status

**Stable Studionet only:** chain `61999`, RPC `https://studio.genlayer.com/api`.

- Contract runner: GenVM `v0.2.16`, pinned `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.
- JS integration: `genlayer-js@1.1.8`; direct tests: `genlayer-test@0.29.2`.
- Deployment and real semantic consensus: **PASS**; six FINALIZED / MAJORITY_AGREE / SUCCESS transactions. Official Studio built-in signing: **PASS**; product extension-wallet write E2E: **NOT RUN**. See [final onchain report](FINAL_ONCHAIN_REPORT.md).
- Stable RPC schema generation passed. [FINAL_ONCHAIN_REPORT.md](FINAL_ONCHAIN_REPORT.md) is the current deployment and consensus record; [CHECKPOINT.md](CHECKPOINT.md) documents the initial pre-deployment test baseline.

## Test

Python 3.12:

```bash
pip install -r requirements-dev.txt
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest
```

The direct runner downloads official GenVM v0.2.16 SDK artifacts. It uses in-memory storage and explicit web/LLM test responses, **not a Localnet node**. Validator tests invoke the actual captured validator with independent and malicious inputs. These tests do not prove real model accuracy or real network consensus.

## Boundaries

- Up to 8 monitors per owner, with IDs namespaced by lowercase owner address; 256 observations per monitor; 60 seconds between checks; 7-day announcement freshness limit; 24,000-character source limit. There is no shared 128-monitor cap. Per-address quotas isolate ordinary users but do not eliminate Sybil activity across multiple addresses; network-level resource costs still apply.
- Owner-selected source is immutable but not certified official. DNS/redirect safety ultimately depends on the GenLayer web service. Public DNS syntax checks are not a full SSRF firewall.
- Unavailable, oversized, malformed or stale evidence fails closed. Time-varying pages may prevent agreement. Prefer concise announcement pages with explicit UTC dates.
- Manual, faucet-funded checks; no scheduler, paid API, backend, payouts, uptime SLA or source-authenticity claims.
- Prompt injection is mitigated by separating data, strict output validation and independent assessment; it is not proven impossible.

[Technical notes](TECHNICAL.md) · [Product repository](https://github.com/gqzy1/signalledger-genlayer)

MIT licensed.

## Verified Stable Studionet deployment

Contract: `0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247`. Six real finalized transactions establish OUTAGE, recovery to OPERATIONAL and UNKNOWN retention on the same monitor. The first recovery attempt observed an old cached source; its historical failure remains archived. See [final onchain report](FINAL_ONCHAIN_REPORT.md), [raw evidence](evidence/fast2/), and [Intelligent Contracts submission information](SUBMISSION_INTELLIGENT_CONTRACTS.md). Official source SHA256 is unchanged. Portal submission has not been performed.
