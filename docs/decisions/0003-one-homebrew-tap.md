# 0003. One Homebrew tap for every tool

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

arm-tools and mochi-donut each started as their own tap, then moved to the shared [maytech-labs/homebrew-tap](https://github.com/maytech-labs/homebrew-tap) (arm-tools [0047](https://github.com/maytech-labs/arm-tools/blob/main/docs/decisions/0047-org-homebrew-tap.md), mochi-donut [0039](https://github.com/maytech-labs/mochi-donut/blob/main/docs/decisions/0039-org-homebrew-tap.md)).

## Decision

- Every installable tool has a formula in `maytech-labs/homebrew-tap`, named after its repo.
- Installing is `brew tap maytech-labs/tap`, `brew trust maytech-labs/tap`, `brew install <tool>`.
- Each tool's release workflow bumps its own formula, committing `chore(<formula>): X.Y.Z` to the tap's `main` with a token scoped to the tap.

## Consequences

- One set of install instructions for the profile, the site, and every README.
- Each tool's repo holds a token that can write to the tap; it expires and has to be renewed.

## Alternatives considered

- **A tap per tool.** Longer install commands, and `brew install` becomes ambiguous with more than one tapped.
- **homebrew-core.** Requires an OSI license, which REAL isn't ([0002](0002-real-license.md)).
