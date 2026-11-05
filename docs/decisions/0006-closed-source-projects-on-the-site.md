# 0006. The site can show closed-source projects from outside the org

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

Some projects worth showing aren't maytech-labs repos: [Tolarian Machine](https://maytech-labs.github.io/tolarian-machine/), a Magic: The Gathering engine whose AI agents play live on [Twitch](https://www.twitch.tv/jogzonx), and [Urza's Binder](https://maytech-labs.github.io/urzas-binder/), a trading-card portfolio. Both are closed source and private, so they have no public README or project page to link to, and [0002](0002-real-license.md) doesn't apply to them. [0004](0004-site-on-github-pages.md) assumes project docs are served from each project's own repo.

## Decision

- The site may list closed-source projects that live outside the org. They go in their own section (today, "Magic: The Gathering"), never among the source-available tools, and each card carries a `closed source` badge.
- Their cards link to a page on the org site itself (`/tolarian-machine/`, `/urzas-binder/`), since there's no repo to link to. Those pages copy `tolarian-machine/index.html`, share `style.css`, and use root-relative paths.
- They never link to a private repo. Pages describe what the project does and where it is, using only what's fine to make public; numbers are dated or easy to re-check.
- Pages for fan projects end with a fan-content notice naming the rights holders (Wizards of the Coast; The Pokémon Company).
- Copy says "source-available" only of REAL 1.0 projects. The hero and footer say so explicitly now that not everything is.
- The Twitch channel is linked from the top bar ("Watch live") and from the projects it shows.

## Consequences

- The site shows the whole lab, not just the org's repos, with a clear line between what's source-available and what isn't.
- These pages are written by hand and go stale: Tolarian Machine's card and precon counts come from its roadmap and need refreshing.
- `org-status.py` doesn't check these projects. They aren't org repos, so the site never trips its private-repo check, but nothing flags their drift either.
- A future org repo named `tolarian-machine` or `urzas-binder` with its own Pages site would collide with the org site's folder; move the page to that repo if that happens.

## Alternatives considered

- **Leave them off the site.** Keeps the site purely REAL 1.0, but hides the projects people can actually watch.
- **Link straight to Twitch.** What the first version did; with the stream offline, visitors land on an empty channel with no context.
- **Make them org repos.** They're closed source, so they'd be private org repos, which [0002](0002-real-license.md) and `org-status.py` would then treat as licensing drift.
