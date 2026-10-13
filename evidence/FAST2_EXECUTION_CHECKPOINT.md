# FAST-2 execution checkpoint — four transactions; recovery blocked

Network: Stable Studionet 61999, https://studio.genlayer.com/api. Official Studio built-in signer: 0xf38Fd10816b18FfAc55b4c523cE40D2DB313fc33. Browser/UI signing was used; no private key or seed was requested or exported. Preflight balance was 0 GEN, gasPrice 0, value 0; no paid service or paid funds were used.

Canonical deployed contract: 0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247.
Source SHA256 (canonical, Repository B copy and RPC-retrieved deployed source): 89d4f8e3ee117a9dbe6acd086f3363645cad34ba84fc83e54a1773d291be7daa.

## Actual transactions

All four below are FINALIZED, last_round.result 6 (MAJORITY_AGREE), leader execution SUCCESS, one round, zero rotations. Every preceding transaction was finalized before the next was sent.

| Action | Hash | Votes | Scenario result |
|---|---|---|---|
| Deploy | 0xad010dbb93a50af9674658311f8f100aca36022e596c6149bcd7daa5fc2bb4b8 | 5 AGREE | PASS; source digest independently matched |
| Create monitor | 0x54a33fb918fa30fe6d2dd81118af820f34c2ae397550800c5e20461b3fd8eec8 | 3 AGREE, 2 IDLE | PASS; finalized UNKNOWN, revision 0 |
| Outage check | 0x46ff47e9634e470b3b96195c54d2ddcde7b9a1fd309c925f0da435afa742ca44 | 3 AGREE, 2 IDLE | PASS; UNKNOWN -> OUTAGE, revision 1 |
| Recovery check | 0x0c56b26891f8f5fcff818b6c24a2de781b09ab7bbf0d7d4ed65a73fec360e9b9 | 3 AGREE, 2 IDLE | FAIL; observed old outage, OUTAGE -> OUTAGE, revision 2 |

The IDLE validators are recorded honestly; the four transactions reached majority agreement, not unanimous agreement except deployment. Raw receipts preserve validator errors and model configurations.

Explorer address: https://explorer-studio.genlayer.com/address/0x468aCd1d9B4db1527d92Bc41Fc76d4016eb11247
Explorer transaction URLs use https://explorer-studio.genlayer.com/tx/ followed by each complete hash above.

## Recovery failure and source evidence

Fixed monitor: fast2-eu-api. Fixed scope: SignalLedger Test Service / EU API.
Fixed source: https://raw.githubusercontent.com/gqzy1/signal-ledger-primitive/main/evidence/test-announcement.txt

The outage source timestamp was 2026-10-13T05:40:00Z. The outage check datetime was 05:56:05Z.
After outage finality, source commit 6d0edb593a4d793709f17cd3c439c386362d2a68 published an explicit OPERATIONAL recovery with timestamp 05:58:00Z. Direct HTTP retrieval verified the new text before the recovery transaction at 05:59:23Z. This satisfied the 60-second cooldown and timestamp ordering. The source was not edited during either consensus execution.

However the finalized recovery record retained signal OUTAGE, old updated_at 05:40:00Z and old rendered-source digest 36e02e752ee10bfc85c04fd4b6cfa92f7061f4dab3fb133c72dbe15ac65c741a. The exact same old quote and digest appear in its real leader nondeterministic output. Thus the transaction succeeded on the earlier observed bulletin; it did not establish recovery. No PASS is claimed for this scenario.

A later direct HTTP fetch confirmed the intended recovery text and returned Cache-Control max-age=300 and X-Cache HIT. Source-fetch cache lag is the leading explanation, an inference rather than proof of the exact infrastructure layer or cache lifetime. There is no evidence here that a model saw recovery wording and incorrectly classified it as outage. The initial render-path digest differs from a plain HTTP body digest because rendered text may be normalized.

The current recovery bulletin remains frozen. Before any retry, wait beyond the published caching window and confirm source freshness as far as read-only diagnostics allow. Source changes, signature approval and transaction time must remain distinct. No contract/security change is proposed.

## Honest acceptance status

- Deployment, source match, creation and real OUTAGE consensus/transition: PASS.
- Recovery scenario: FAIL, despite successful transaction finality.
- UNKNOWN observation retaining OPERATIONAL: NOT RUN, because OPERATIONAL has not been established.
- Product extension-wallet connection/live writes/browser visual QA: NOT RUN. Studio UI live signing is PASS and is distinct from the product frontend.
- GitHub Pages source was configured to GitHub Actions, but no release workflow was triggered and no public site acceptance is claimed.
- Neither submission track is ready under the requested complete three-scenario acceptance criterion. Portal submission: NOT RUN.

The original authorization allowed five specific transactions. Four were sent. The remaining fifth is an insufficient-evidence check, not a recovery retry. No sixth or substitute transaction was sent. Completing the intended sequence requires explicit authorization for one additional recovery check, followed by the originally authorized insufficient-evidence check after recovery succeeds. Stop on any new failure; no automatic extra transactions.

## Code and evidence checkpoint

Contract source unchanged. A minimal frontend fix normalizes lowercase votes from the real Studio RPC, preserving finality, majority and execution requirements. Targeted domain tests: 24 PASS, including the regression; production build PASS. The baseline contract CI log confirms 42 PASS; the frontend baseline had 30 PASS. Current frontend CI will run the resulting 31-case suite.

Raw receipts, finalized reads, the original outage bulletin, intended recovery bulletin and public-fetch headers are archived alongside this report. The intended recovery snapshot is not misrepresented as what GenVM actually observed.

No product redesign, network switch, paid service or Portal submission occurred.
