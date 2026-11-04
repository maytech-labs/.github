# 0002. Every project is licensed under REAL 1.0

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

maytech-labs wrote the [Reciprocal Ethical AI License (REAL) 1.0](https://github.com/maytech-labs/real-license) and moved its projects to it before their first releases (arm-tools [0045](https://github.com/maytech-labs/arm-tools/blob/main/docs/decisions/0045-real-license.md), mochi-donut [0038](https://github.com/maytech-labs/mochi-donut/blob/main/docs/decisions/0038-real-license.md), arm-lessons [0012](https://github.com/maytech-labs/arm-lessons/blob/main/docs/decisions/0012-license-real.md)). [real-check](https://github.com/maytech-labs/real-check) checks a repository against it.

## Decision

- Every maytech-labs repo has REAL 1.0 as `LICENSE.md` in its root, copyright maytech-labs and the year the repo starts. (mochi-donut names its author instead; either passes `real-check`.)
- The text is exactly the [real-license](https://github.com/maytech-labs/real-license/blob/main/LICENSE.md) template with only the copyright line filled in, so `real-check repo .` passes.
- Source files carry `SPDX-License-Identifier: LicenseRef-REAL-1.0`.
- Third-party code keeps its own license, noted beside it.
- Public descriptions call the projects source-available, not open source.

## Consequences

- One license to understand across every project.
- REAL isn't OSI-approved and has no SPDX identifier, so some package indexes and distributions won't carry the projects.
- `real-check` is the check for compliance; [0005](0005-org-state-is-checkable.md) reports any repo whose license isn't REAL 1.0.

## Alternatives considered

- **Per-project choice.** More flexible, but the org exists partly to promote REAL.
- **MIT or Apache-2.0.** Permissive, but they put no conditions on AI training, which is what REAL is for.
