# MayTech Labs

[![License: REAL 1.0](https://img.shields.io/badge/License-REAL_1.0-blue.svg)](https://github.com/maytech-labs/real-license)

Small, careful tools for low-level code and AI-era licensing. Everything here is source-available under [REAL 1.0](https://github.com/maytech-labs/real-license).

## Projects

| Repo | What it is |
|---|---|
| [arm-tools](https://github.com/maytech-labs/arm-tools) | Language server, linter, and formatter for AArch64 assembly on Apple silicon and Linux, checked against clang. |
| [arm-lessons](https://github.com/maytech-labs/arm-lessons) | A slow, hands-on ARM64 assembly course for Linux and Apple silicon. Every example and solution is tested on both. |
| [mochi-donut](https://github.com/maytech-labs/mochi-donut) | Evidence-backed CLI tools for AI coding agents: house style, stale docs, passing checks, and the right cluster or account. |
| [godo](https://github.com/maytech-labs/godo) | make, but every run is a detachable, logged, watchable job. Also home to clapsmith, a companion to clap. Early. |
| [real-license](https://github.com/maytech-labs/real-license) | The Reciprocal Ethical AI License: open weights and ethical limits for AI models trained on licensed code. |
| [real-check](https://github.com/maytech-labs/real-check) | Checks that a repository and its dependencies are compatible with REAL 1.0. |
| [homebrew-tap](https://github.com/maytech-labs/homebrew-tap) | Homebrew formulae for the tools above. |

## Install

```sh
brew tap maytech-labs/tap
brew trust maytech-labs/tap
brew install arm-tools real-check
```

## License

Projects use the [Reciprocal Ethical AI License (REAL) 1.0](https://github.com/maytech-labs/real-license). Use, modify, and share freely; training an AI model on the code obliges you to release the model's weights and training pipeline under the same terms. It's source-available, not OSI-approved, so read it before you depend on the code.
