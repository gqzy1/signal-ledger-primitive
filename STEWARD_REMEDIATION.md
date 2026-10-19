# Steward remediation — owner-scoped monitor capacity

## Finding
The original contract used globally shared monitor IDs and a global 128-monitor ceiling. Any caller could occupy IDs and consume the entire shared capacity; owner-only checks did not prevent creation abuse.

## Candidate fix
- Store each monitor under `lowercase-owner-address::monitor-id`.
- Allow the same human-readable ID for different owners.
- Limit each address to eight monitors and expose `get_owner_count(owner)`.
- Remove the shared 128-monitor ceiling; `get_count()` remains an aggregate informational count.
- Preserve owner-only checks, independent GenLayer validation, evidence digests, revision guards, chronology, cooldown, UNKNOWN retention and 256-record per-monitor history.

## Verification and release status
The candidate test suite covers owner ID isolation, per-owner quota enforcement, and creation beyond 128 aggregate monitors. The new address `0x6022e1Dba86A150e420bd4f027c6C2eD4a5487b4` is DEPLOYED_USER_REPORTED on Stable Studionet 61999. Source identity is VERIFIED through the user-performed local Chrome comparison and existing A/B byte identity; see [the exact evidence scope](SOURCE_VERIFICATION.md). The user confirmed the owner-scoped monitor at OPERATIONAL / revision 1 / checks 1 and record 1. These are not fresh cloud reads.

The old deployment and its six receipts remain historical; no new deployment hash is supplied. Cloud 403/1010 has no demonstrated resolution. Final PR integration, separately authorized publication and new public read-only acceptance remain incomplete. Do not redeploy, retry a write or repeat passed tests merely to update this documentation.

## Candidate source SHA256
`c24e2801e3e7266a2858596a248b3fd99801dce993e1398c3bd6840f90321d54`

## Limitations
Per-address quotas isolate ordinary accounts but do not fully prevent Sybil activity across multiple addresses. The candidate remains permissionless and introduces no administrator allowlist or paid gate.
