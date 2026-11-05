# 0007. Site sections appear when they have something in them

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

Two sections are planned for the site: one for research projects, which aren't ready to publish, and a light-hearted one that turns ideas a young child has had over the years into obviously-not-real "products".

## Decision

- A section goes on the site only once it has at least one real entry. No empty or "coming soon" sections, cards, or tabs.
- Research gets a section and pages built from the same template as [0006](0006-closed-source-projects-on-the-site.md) when there's a first project to describe.
- The kids' ideas section:
  - is clearly labeled as made-up and not real products, on the section and on every page;
  - has its own lighter, playful look, kept visibly separate from the real tools;
  - names the child by first name or a nickname at most, with no photos and nothing else that identifies him.

## Consequences

- The site never looks unfinished, at the cost of the research section not existing until it has content.
- The playful section needs its own styles, so `style.css`'s version bumps when it lands.

## Alternatives considered

- **Placeholder sections now.** Signals what's coming, but makes the whole site look half-built.
- **A separate site for the kids' ideas.** Fully isolated, but loses the charm of it living beside the real work.
