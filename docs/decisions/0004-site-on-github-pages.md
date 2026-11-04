# 0004. The website is static, on GitHub Pages

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

maytech-labs needs a website beyond the GitHub profile. Some future products will need servers, which GitHub Pages can't run.

## Decision

- The site is the [maytech-labs.github.io](https://github.com/maytech-labs/maytech-labs.github.io) repo: plain HTML and CSS, no build step, served by GitHub Pages from `main`.
- Project docs stay in their own repos and are served as project pages (`/arm-tools/`, `/arm-lessons/`).
- When maytech-labs has a domain, the org site moves to it, and the project pages follow automatically.
- Hosted products get subdomains (for example `app.` or `api.`) pointed at wherever they run. The static site stays on Pages.
- Stylesheet links carry a version query (`style.css?v=N`), bumped with each style change, because Pages lets browsers cache files for ten minutes.

## Consequences

- Free hosting, no build to break, and edits are a pull request.
- Every project card is written by hand. Past about ten projects, generate them from a data file.
- Moving off Pages later changes DNS, not links, once there's a domain.

## Alternatives considered

- **A static site generator (Jekyll, Astro).** Templating and data files, but a build to maintain for one page.
- **A hosting platform (Vercel, Netlify, Cloudflare Pages).** Needed for hosted products, not for a static page.
