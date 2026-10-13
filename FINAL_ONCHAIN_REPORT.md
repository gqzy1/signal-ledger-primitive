# SignalLedger — final Stable Studionet onchain report

## Result
The minimum three real scenarios passed on the SAME fixed monitor and URL: UNKNOWN -> OUTAGE, OUTAGE -> OPERATIONAL, and UNKNOWN / INSUFFICIENT_EVIDENCE retaining OPERATIONAL. Six real transactions were submitted in total, including the original recovery observation and the later recovery recheck. All transaction hashes and outcomes are preserved. Portal submission status is separate from onchain verification.

- Network: Stable Studionet 61999; RPC https://studio.genlayer.com/api
- Canonical contract: 0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247
- Explorer: https://explorer-studio.genlayer.com/address/0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247
- Official Studio built-in signer: 0xf38Fd10816b18FfAc55b4c523cE40D2DB313fc33
- Source SHA256: 89d4f8e3ee117a9dbe6acd086f3363645cad34ba84fc83e54a1773d291be7daa
- Canonical source, complete Repository B copy and RPC-retrieved deployed source match byte for byte. The deployed business logic matches the canonical source.
- Preflight balance 0 GEN, gasPrice 0, value 0; archived execution receipts report zero gas use. Cash cost was zero. No private key or seed phrase was requested or exported.

## Six actual transactions

All six are FINALIZED / MAJORITY_AGREE / SUCCESS, one round each. Votes are preserved exactly; majority agreement is not represented as unanimous agreement.

| # | Action | Explorer | Votes | Scenario |
|---|---|---|---|---|
| 1 | Deploy | [0xad010dbb…](https://explorer-studio.genlayer.com/tx/0xad010dbb93a50af9674658311f8f100aca36022e596c6149bcd7daa5fc2bb4b8) | AGREE, AGREE, AGREE, AGREE, AGREE | PASS |
| 2 | Create monitor | [0x54a33fb9…](https://explorer-studio.genlayer.com/tx/0x54a33fb918fa30fe6d2dd81118af820f34c2ae397550800c5e20461b3fd8eec8) | AGREE, AGREE, AGREE, IDLE, IDLE | PASS |
| 3 | Outage | [0x46ff47e9…](https://explorer-studio.genlayer.com/tx/0x46ff47e9634e470b3b96195c54d2ddcde7b9a1fd309c925f0da435afa742ca44) | IDLE, AGREE, IDLE, AGREE, AGREE | PASS |
| 4 | First recovery attempt | [0x0c56b268…](https://explorer-studio.genlayer.com/tx/0x0c56b26891f8f5fcff818b6c24a2de781b09ab7bbf0d7d4ed65a73fec360e9b9) | AGREE, AGREE, IDLE, IDLE, AGREE | Historical recovery scenario FAIL; old outage source |
| 5 | Recovery recheck | [0xb752d130…](https://explorer-studio.genlayer.com/tx/0xb752d13010d5f8a81dfa5de93cf1a06e7e23dc9f1ca4a49c7d3ab4277b1b5489) | AGREE, AGREE, IDLE, AGREE, DISAGREE | PASS |
| 6 | Insufficient evidence | [0x4a5d1d1f…](https://explorer-studio.genlayer.com/tx/0x4a5d1d1f7cc99ae7bdd34c0144d7b3f668eab52e0b8926d64a33471df903a5a2) | IDLE, AGREE, IDLE, AGREE, AGREE | PASS |

## Finalized semantic records

| Revision | Observation | Before -> after | Disposition | Source update | Checked UTC |
|---|---|---|---|---|---|
| 1 | OUTAGE | UNKNOWN -> OUTAGE | TRANSITION | 2026-10-13T05:40:00Z | 2026-10-13T05:56:05Z |
| 2 | OUTAGE, old source | OUTAGE -> OUTAGE | CONFIRMED | 2026-10-13T05:40:00Z | 2026-10-13T05:59:23Z |
| 3 | OPERATIONAL | OUTAGE -> OPERATIONAL | TRANSITION | 2026-10-13T05:58:00Z | 2026-10-13T06:24:42Z |
| 4 | UNKNOWN | OPERATIONAL -> OPERATIONAL | INSUFFICIENT_EVIDENCE | empty | 2026-10-13T06:34:42Z |

Fixed ID: fast2-eu-api. Fixed scope: SignalLedger Test Service / EU API.
Fixed URL: https://raw.githubusercontent.com/gqzy1/signal-ledger-primitive/main/evidence/test-announcement.txt
All bulletins are explicitly SYNTHETIC TEST DATA. They do not claim the status of a real service.

The source was unchanged during each consensus execution. Recovery established a strictly newer accepted update, and all checks respected the 60-second cooldown. UNKNOWN has empty updated_at and quote; last_event remains the accepted recovery time, while last_checked advances. The retained OPERATIONAL state is not a fresh uptime guarantee.

## Cache diagnosis and recovery

The first recovery transaction succeeded on the prior outage bulletin and failed the intended semantic scenario. Its original hash and revision-2 record remain preserved. Direct HTTP headers showed max-age=300. Cache lag was the leading inference; the exact cache layer was not proven.

Before the approved recovery retry, the unchanged recovery bulletin had aged over 20 minutes. A real, non-persisting sim_call at current UTC time returned SUCCESS and OPERATIONAL with the new source digest cb318bc56e2bfd579a64a8051a8dd535e9ded15137ff0e784a80ce47657b31de. The subsequent real finalized record matches that digest and quote.

For the out-of-scope bulletin, publication completed at approximately 06:26:52Z. A first HTTP fetch at 06:29:35Z and a GenLayer sim_call at 06:33:54Z confirmed the US Dashboard notice. This waited over six minutes before the final diagnostic and real transaction. The actual final record has source digest f57a6c61a71cc544894d5628b20cb1760719c2b8353db46db9c1eed7c5f3a880, signal UNKNOWN and retained OPERATIONAL.

The initial SDK gen_call diagnostic was stopped by the cooldown guard because its default execution datetime was unsuitable. The official sim_call interface with sim_config.genvm_datetime set to the actual current UTC time was then used ONLY for non-persisting diagnostics, not for real transactions. No source, scope, URL, ownership or contract state was overridden. No simulated output is counted as an onchain PASS.

## Evidence archive and reproduction

The evidence directory contains a machine-readable ONCHAIN_EVIDENCE_INDEX.json, six losslessly compressed original JSON receipts (.json.gz), finalized monitor/record reads, source snapshots and diagnostic receipts. Decompress .json.gz with gzip before reading. The two read-only .mjs helpers in Repository B use the pinned SDK and never send a transaction.

Raw receipts include real leader model configuration, nondeterministic outputs, independent validator votes and execution results, including disagreements/timeouts. Some nodes did not agree; the resulting majority did. The evidence is a bounded controlled acceptance, not a claim about arbitrary announcement accuracy.

Contract baseline CI: 42 tests PASS. Frontend: 34 tests after actual-RPC lowercase-vote and mixed leader/validator receipt compatibility regressions. All code and MIT licenses required for both tracks are included. Product browser-wallet coverage and public-site verification are recorded separately in Repository B's PRODUCT_ACCEPTANCE_REPORT.md.
