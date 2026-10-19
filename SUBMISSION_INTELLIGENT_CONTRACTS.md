> **Steward remediation candidate — NOT DEPLOYED.** Do not resubmit this draft until the updated source has been deployed and the deployed source hash and transaction evidence have been refreshed.

# Intelligent Contracts — SignalLedger Primitive

## Name
SignalLedger — Scope-Bound Service Announcement Ledger

## Description
A reusable Intelligent Contract that interprets explicitly dated service announcements for one immutable component/region scope and stores an evidence-grounded transition history. A leader classifies the source and independent validators re-fetch, reclassify and verify its exact excerpt and rendered-source digest. UNKNOWN records an insufficient-evidence observation while retaining the last accepted state. Deterministic guards enforce owner-scoped IDs, per-owner creation quotas, revision concurrency, chronology, cooldown and bounded history.

This measures the meaning of an announcement, not actual network uptime. The semantic task includes component applicability, negation, recovery and planned versus ongoing maintenance; keyword or HTTP-success checks cannot supply the same acceptance boundary.

## Network and contract
- Stable Studionet, Chain ID 61999, RPC https://studio.genlayer.com/api
- Contract: https://explorer-studio.genlayer.com/address/0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247
- Empty constructor; 2 write and 4 view methods.
- The previous deployed source hash and address below describe the pre-remediation deployment; the candidate source must be deployed and re-verified before final submission.
- MIT License. No paid infrastructure or private-key disclosure is required.

## Evidence and supplementary URLs for this track
1. https://github.com/gqzy1/signal-ledger-primitive/blob/main/FINAL_ONCHAIN_REPORT.md
2. https://github.com/gqzy1/signal-ledger-primitive/blob/main/contracts/signal_ledger.py
3. https://github.com/gqzy1/signal-ledger-primitive/blob/main/TECHNICAL.md
4. https://explorer-studio.genlayer.com/tx/0xad010dbb93a50af9674658311f8f100aca36022e596c6149bcd7daa5fc2bb4b8

These links document the contract implementation, independent consensus mechanism and completed onchain acceptance. The Projects repository provides product-specific evidence separately. The canonical deployed contract address is shared by both submissions. Portal submission status is not inferred from this repository.
