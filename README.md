# maytech-labs/.github

The [maytech-labs](https://github.com/maytech-labs) organization profile, org-wide decisions, and default community health files.

- [`profile/README.md`](profile/README.md): the org profile page.
- [`docs/decisions/`](docs/decisions/README.md): decisions that apply across every repo.
- [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md): defaults for any repo without its own.

## Checking the org

```sh
scripts/org-status.py          # table of repos, then any drift
scripts/org-status.py --json   # same data as JSON
```

It lists every repo's latest release, license, and last push, and reports where the profile or the [website](https://github.com/maytech-labs/maytech-labs.github.io) is out of date. It exits 1 on drift. Run it before editing either, and after creating, archiving, or releasing a repo ([0005](docs/decisions/0005-org-state-is-checkable.md)). It reads the site from `../maytech-labs.github.io` if you have it cloned beside this repo, or from GitHub otherwise.

## License

[REAL 1.0](LICENSE.md)
