# Steward remediation — owner-scoped monitor capacity

## Finding
The original contract used globally shared monitor IDs and a global 128-monitor ceiling. Any caller could occupy IDs and consume the entire shared capacity; owner-only checks did not prevent creation abuse.

## Candidate fix
- Store each monitor under `lowercase-owner-address::monitor-id`.
- Allow the same human-readable ID for different owners.
- Limit each address to eight monitors and expose `get_owner_count(owner)`.
- Remove the shared 128-monitor ceiling; `get_count()` remains an aggregate informational count.
- Preserve owner-only checks, independent GenLayer validation, evidence digests, revision guards, chronology, cooldown, UNKNOWN retention and 256-record per-monitor history.

## Verification required
The candidate test suite covers owner ID isolation, per-owner quota enforcement, and creation beyond 128 aggregate monitors. The candidate is not deployed. The previous deployment and its original receipts remain historical evidence and do not prove this remediation. Before resubmission, deploy this exact source on Stable Studionet, verify the onchain source hash, create a fresh owner-scoped example, and record successful real consensus outcomes. Do not retry a failed write automatically.

## Candidate source SHA256
`c24e2801e3e7266a2858596a248b3fd99801dce993e1398c3bd6840f90321d54`

## Limitations
Per-address quotas isolate ordinary accounts but do not fully prevent Sybil activity across multiple addresses. The candidate remains permissionless and introduces no administrator allowlist or paid gate.
