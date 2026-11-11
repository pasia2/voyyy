# voyyy

This repository is a placeholder. It does not yet contain application source,
dependency manifests, setup scripts, or build/test configuration. There is
currently no application to install, build, test, or run.

## Get a local checkout

You need Git and a terminal. Install Git using the
[official installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
then confirm it is available:

```sh
git --version
```

Clone the repository and enter its directory:

```sh
git clone https://github.com/pasia2/voyyy.git
cd voyyy
git ls-files
```

The last command lists the tracked files. At present these are documentation
only. No language runtime, package manager, environment variables, or external
services are specified. Do not guess an install or build command: a working
build or test run is blocked until the project implementation is added.

## Setup audit

See [the setup audit](docs/setup-audit.md) for the missing steps identified in
the initial checkout and what was verified.

When implementation is added, update this README with the supported operating
systems, exact runtime and package-manager versions, dependency installation,
any configuration or services required, and copyable build/test commands with
their expected results. Those instructions must be verified from a fresh clone
before describing setup as complete.
