# FAST-2 deployment preflight checkpoint

## Verified

- Stable Studionet only: eth_chainId = 0xf22f (61999), RPC https://studio.genlayer.com/api.
- Both baseline main commits matched: A dd84d715210d0c0369749af53a427d32923556cf; B fa6738a0111105e6bf0209c1a7f2df500fe4b7eb.
- Both complete official source files SHA256 = 89d4f8e3ee117a9dbe6acd086f3363645cad34ba84fc83e54a1773d291be7daa. Contract code was not modified.
- Current getContractSchemaForCode: empty constructor; create_monitor and check writes; get_monitor, get_record and get_count views.
- A baseline CI https://github.com/gqzy1/signal-ledger-primitive/actions/runs/38351335949 succeeded; actual job log confirms 42 passed in 48.27s.
- B baseline CI https://github.com/gqzy1/signalledger-genlayer/actions/runs/38351347527 succeeded. FAST-2 locally reran source verification, all 30 frontend tests and production build successfully.
- eth_gasPrice returned 0x0. A read-only SDK pre-sign preparation for the browser-visible Studio address 0xf38Fd10816b18FfAc55b4c523cE40D2DB313fc33 produced gas 0x7a120 (500000), value 0, chain 0xf22f, consensus recipient 0xb7278A61aa25c888815aFC32Ad3cC52fF24fE575. A custom provider blocked eth_sendTransaction before network transmission. No transaction hash exists. Estimates must be refreshed for the actual approved signer and are not a guarantee of future fees.

## Controlled source

Public source: https://raw.githubusercontent.com/gqzy1/signal-ledger-primitive/main/evidence/test-announcement.txt

Verified direct HTTP 200 and 504 characters. Explicit SYNTHETIC TEST DATA; scope SignalLedger Test Service / EU API; UTC update 2026-10-13T05:40:00Z; explicit current OUTAGE. URL satisfies canonical source_url rules and body is below 24000 characters. Actual GenVM web-render accessibility remains NOT RUN until a real check. Refresh timestamp if older than seven days; keep source immutable throughout consensus.

Minimum planned execution is five transactions: deploy, create fast2-eu-api, then checks at expected revisions 0, 1, 2 for OUTAGE, OPERATIONAL, UNKNOWN retention. Update the same source only between finalized checks; recovery must have a newer timestamp. Enforce 60-second cooldown from last_checked. Intentional failure transactions are excluded unless necessary and specifically approved.

## Actual status

| Check | Status |
|---|---|
| Network/schema/source/CI verification | PASS |
| Frontend unit tests and production build | PASS |
| Real deployment/address/deployed source verification | NOT RUN |
| Real model judgment and consensus | NOT RUN |
| Three live E2E cases and finalized reads | NOT RUN |
| Browser-wallet frontend E2E and visual QA | NOT RUN |
| GitHub Pages publication/public chain reads | NOT RUN |
| Portal submission | NOT RUN |

## Execution gate

The user's FAST-2 section B explicitly prohibits deployment and writes without explicit approval. No deployment or contract write was submitted. The cloud Studio currently shows its own built-in account with 0 GEN and an available Connect Wallet control; it does not establish access to the user's funded local wallet. A usable user-approved signer is still needed. Do not request private keys or seed phrases. No faucet or paid service is required merely to record this checkpoint.

Neither track is submission ready: real finalized evidence and public frontend chain-read acceptance remain outstanding. deployment.json remains truthfully NOT DEPLOYED / NOT RUN. Resume from this checkpoint; if any future transaction is sent, archive and track its original hash before considering a retry. No product redesign or network change was made.
