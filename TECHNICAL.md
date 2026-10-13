# Design and bounded topic assessment

## Why this topic passes

The bounded comparison examined GenLayer's [UptimeMonitor](https://github.com/genlayer-foundation/uptime/blob/main/contracts/uptime_monitor.py), which checks HTTP success or a JSON-RPC response. Its existence rules out “HTTP check + chain record” as a sufficient distinction.

SignalLedger instead resolves whether the latest **natural-language announcement applies to a fixed component/region**, distinguishes planned work from current maintenance, accepts explicit recovery, and protects the transition history against stale or ambiguous evidence. Example: an HTTP-200 page describing US-only disruption cannot change an EU payment monitor. This is a scoped original implementation, not a claim to be the world's first semantic monitor.

A deterministic keyword classifier cannot reliably resolve negation, component applicability, planned versus ongoing work and recovery wording across arbitrary announcements. GenLayer provides the nondeterministic reasoning and independent acceptance boundary. The [official equivalence-principle guide](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle) requires substantive independent verification; this contract re-fetches and reclassifies the evidence.

No previous user repository was read or reused. No competitor code was copied.

## Acceptance boundary

`run_nondet_unsafe(leader, validator)` captures only plain URL/scope/time values. Validators reject exceptions, malformed output, fabricated excerpts, source digest mismatch, status disagreement and update-time disagreement. Excerpt wording may differ between models, but every leader excerpt must be grounded in the independently fetched page. Exact digest equality deliberately favors failure over silently mixing source versions.

The model must return only signal, canonical UTC update time and a literal excerpt. Structured decisions are normalized and bounded. The deterministic path handles permissions, revision concurrency, chronology, cooldown and capacities before updating both the record and monitor.

| Evidence | Deterministic outcome |
|---|---|
| Newer valid scoped status differs | TRANSITION |
| Same/newer status matches | CONFIRMED |
| UNKNOWN | INSUFFICIENT_EVIDENCE; retain accepted state |
| Earlier update | Revert |
| Different status at identical time | Revert |
| Web/model error or rejected consensus | No committed mutation |

UNKNOWN retaining a state does not make that state fresh: consumers must inspect last_event, last_checked and the most recent record. No elapsed-time inference silently changes state.

## Test limitations and next verification

Direct mode executes the production storage SDK but supplies explicit test web/LLM responses. It normally captures a leader result before running a validator separately; a separate test installs a rejecting consensus boundary and asserts no deterministic mutation. This verifies code behavior, not network consensus. Live tests must check actual FINALIZED, MAJORITY_AGREE, successful execution, substantive validator evidence and finalized reads.

The test package's `warp` does not refresh the SDK's message_raw datetime cache, so test helper `advance` updates that cache explicitly. Production reads transaction datetime from the pinned SDK's `gl.message_raw['datetime']`, never machine wall-clock time.

There is no payout, escrow, agent scheduling, dynamic policy language or extra network adapter. The primitive is deployable as one source file and the product runs as a static client.
