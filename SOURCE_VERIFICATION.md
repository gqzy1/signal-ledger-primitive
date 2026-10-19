# Manual source verification and deployment status

FAST-6 documentation sync; no deployment, signature, transaction, merge, Pages publication or Portal submission.

| Dimension | Status | Scope |
|---|---|---|
| Current deployment | DEPLOYED_USER_REPORTED | Stable Studionet 61999, `0x6022e1Dba86A150e420bd4f027c6C2eD4a5487b4`, official RPC https://studio.genlayer.com/api. |
| Source identity | VERIFIED — MANUAL_LOCAL_CHROME | User-performed local Chrome SHA256 comparison, extended to the frozen B candidates through existing repository byte identity. |
| Cloud access | BLOCKED_NOT_REPLICATED | Historical HTTP 403 / Cloudflare 1010 has no demonstrated resolution; no FAST-6 retry. |
| Public website | HISTORICAL_RELEASE | https://gqzy1.github.io/signalledger-genlayer/ still has the previously observed old deployment `0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247`; no new public read-only acceptance. |
| Final integration and release | NOT COMPLETE / NOT AUTHORIZED HERE | All existing candidates remain Draft; source equality is not publication approval. |

## Evidence source and exact comparison

The user reported local Chrome verification in the conversation on **2026-10-19 at 14:07:09 Asia/Shanghai**. That is the report-receipt time; the actual manual execution time was not separately supplied. The Explorer deployment-transaction source and `contracts/signal_ledger.py` in [A fixed commit](https://github.com/gqzy1/signal-ledger-primitive/blob/65da22cdbf3faf46bd104a5ce2e3d9fa4f93c873/contracts/signal_ledger.py) each measured **10,516 characters and 10,516 UTF-8 bytes**, both SHA256:

`c24e2801e3e7266a2858596a248b3fd99801dce993e1398c3bd6840f90321d54`

Evidence package: `SignalLedger_FAST5_Review_Package (1).zip`, SHA256 `f944830c74d1483c45c515eaca5444b272813c4e5f4e599ba229a0c3d41a0208`. Its `manual-source-verification.json` and updated `SIGNALLEDGER_FAST5_GATE_AND_INTEGRATION_PLAN.md` record the manual comparison; `repository-source-identity.json`, `github-review.json` and `ancestry-and-static-checks.json` preserve the A/B identity chain. These are user-provided manual results plus existing GitHub byte evidence, not a newly retrieved cloud RPC response. No new deployment transaction hash or raw manual source export was supplied; none is invented.

A and B candidate source files have identical Git blob `a3d28492b07ad5ef10bb82b8cf9d147d0fbf32a5`, 10,516 bytes and the SHA256 above. Coverage is limited to these frozen versions:

- A #2: `65da22cdbf3faf46bd104a5ce2e3d9fa4f93c873`.
- B #2: `a6d103828c2cb8140a1b24a6377fb8971b45fd9e`.
- B #3: `ae7efbba417c4655c9d7ae9d7ebc59c4b843ba8b`.
- B #4: `1b2242de42f9860e865dc9e077c9a51eb93909d1`.
- B #5: `cf4cfccd1bd276f511402f95b320a836fef7c0b5`.

B #2's contract blob equals A; B #3/#4/#5 contain no intervening contract-source change. FAST-6 rechecked the full candidate heads/file blobs and preserves source bytes, so the documentation-only descendants retain that source identity. This does not verify arbitrary future source revisions or describe the old main/published source as the new deployment.

User-confirmed monitor baseline: owner `0xEB56F245EFEceD0899b7e23697FeE512a39DBdCc`, monitor `cf-peering-20261018`; count 1, owner count 1, OPERATIONAL / revision 1 / checks 1; record 1 returned successfully. This is historical user-confirmed Studio evidence, not a fresh FAST-6 monitor read or proof of present service uptime.

## Historical evidence and remaining gates

Original reports and all six old transaction hashes remain attached only to `0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247`; the archived source SHA256 is `89d4f8e3ee117a9dbe6acd086f3363645cad34ba84fc83e54a1773d291be7daa`. The old recovery/source-lag failure is retained. Neither its receipts nor its old public PASS claims are reassigned to the new contract.

FAST-5's Explorer GET on 2026-10-19 05:20:36 UTC returned HTTP 403, `error code: 1010`, Ray ID `a4cd55a53d986204-ORD`. The earlier RPC POST failures remain historical. Local manual source verification resolves the source-identity gate; it does not establish that cloud access recovered or that a new frontend has been accepted.

Only Markdown is synchronized in FAST-6. B's existing `deployment.json` status fields are intentionally unchanged; its `SOURCE_VERIFICATION_PENDING` field is prior machine-readable metadata awaiting a separately authorized configuration synchronization. This document records the newer manual VERIFIED evidence. Runtime chain/source-hash checks stay enabled.

Before release: review and authorize safe PR integration with actual ancestor/diff checks, preserve the documentation/configuration distinction, validate the actual integrated baseline as needed, then separately authorize Pages publication and one targeted public read-only acceptance. No repeated source tests or cloud RPC retry is required merely to restate this manual identity result. Portal submission remains separate.
