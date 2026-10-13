# FAST-1 checkpoint — 2026-10-13

| Check actually executed | Result |
|---|---|
| Stable RPC eth_chainId | PASS: 0xf22f = 61999 |
| Stable RPC gen_getContractSchemaForCode | PASS: 5 methods, empty constructor |
| GenVM v0.2.16 direct SDK tests | PASS: 42 cases |
| Independent validator tests | PASS: agree, disagree, exceptions, forged excerpt/digest, independent-source failure |
| Deterministic protection tests | PASS: permissions, revisions, cooldown, stale/future evidence, conflicts, capacities, UNKNOWN retention |
| Consensus closure cloudpickle serialization | PASS |
| genvm-lint 0.11.0 AST checks | PASS: 3 checks |
| genvm-lint SDK semantic validation, pinned v0.2.16 | PASS: SignalLedger, 3 view + 2 write |
| Full source SHA256 match with Repository B | PASS |
| Actual deployment / live model consensus / wallet signing | NOT RUN, not authorized in FAST-1 |
| Portal submission | NOT RUN |

Source SHA256: `89d4f8e3ee117a9dbe6acd086f3363645cad34ba84fc83e54a1773d291be7daa`.

Reproduce tests with README.md. Read-only Studio schema output is in evidence/stable-schema.json. No real model quality, network agreement, FINALIZED live transaction or deployed address is claimed. Earlier test failures were corrected; the final complete suite passed without skips.

Ready for the approved deployment-and-acceptance phase, not ready to claim onchain completion or submit the Portal. Browser frontend visual QA remains NOT RUN due to the current browser environment; Repository B records that limitation.
