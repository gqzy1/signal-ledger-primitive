> **Draft: NOT READY FOR RESUBMISSION.** Deployment is user-confirmed and source identity is VERIFIED by local Chrome manual comparison. Cloud access, final integration, publication authorization and new public acceptance are separate unresolved gates; see [source evidence](SOURCE_VERIFICATION.md).

# Intelligent Contracts — SignalLedger Primitive

## Name
SignalLedger — Scope-Bound Service Announcement Ledger

## Description
A reusable Intelligent Contract that interprets explicitly dated service announcements for one immutable component/region scope and stores an evidence-grounded transition history. A leader classifies the source and independent validators re-fetch, reclassify and verify its exact excerpt and rendered-source digest. UNKNOWN records an insufficient-evidence observation while retaining the last accepted state. Deterministic guards enforce owner-scoped IDs, per-owner creation quotas, revision concurrency, chronology, cooldown and bounded history.

This measures the meaning of an announcement, not actual network uptime. The semantic task includes component applicability, negation, recovery and planned versus ongoing maintenance; keyword or HTTP-success checks cannot supply the same acceptance boundary.

## Network and contract
- Stable Studionet, Chain ID 61999, RPC https://studio.genlayer.com/api
- Current contract (DEPLOYED_USER_REPORTED): https://explorer-studio.genlayer.com/address/0x6022e1Dba86A150e420bd4f027c6C2eD4a5487b4
- Historical contract and old receipts only: https://explorer-studio.genlayer.com/address/0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247
- Empty constructor; 2 write and 4 view methods.
- Source identity: VERIFIED (manual), SHA256 `c24e2801e3e7266a2858596a248b3fd99801dce993e1398c3bd6840f90321d54`, A candidate `65da22cdbf3faf46bd104a5ce2e3d9fa4f93c873`. No cloud independent retrieval or new deployment transaction hash is asserted.
- MIT License. No paid infrastructure or private-key disclosure is required.

## Evidence and supplementary URLs for this track
1. https://github.com/gqzy1/signal-ledger-primitive/blob/main/FINAL_ONCHAIN_REPORT.md
2. https://github.com/gqzy1/signal-ledger-primitive/blob/65da22cdbf3faf46bd104a5ce2e3d9fa4f93c873/contracts/signal_ledger.py
3. https://github.com/gqzy1/signal-ledger-primitive/blob/main/TECHNICAL.md
4. https://explorer-studio.genlayer.com/tx/0xad010dbb93a50af9674658311f8f100aca36022e596c6149bcd7daa5fc2bb4b8

The implementation link is pinned to the manually compared source. FINAL_ONCHAIN_REPORT.md and the transaction URL document only the historical deployment; they are not new-deployment acceptance. [SOURCE_VERIFICATION.md](SOURCE_VERIFICATION.md) records the manual evidence and remaining gates. The Projects website remains the old release. Portal submission is not performed or authorized by this draft.
