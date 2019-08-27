# Poetry Talk

## TODOs

- Should I convert this back to rst?
- Convert long polling to SSI

## Installing Poetry

Per [poetry.eustace.io](https://poetry.eustace.io/docs/#installation)

``` bash
[cig@nzxt talk]$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

$HOME/.poetry/bin

This path will then be added to your `PATH` environment variable by
modifying the profile files located at:

$HOME/.profile
$HOME/.bash_profile

You can uninstall at any time with `poetry self:uninstall`,
or by executing this script with the --uninstall option,
and these changes will be reverted.

Installing version: 0.12.12
  - Downloading poetry-0.12.12-linux.tar.gz (8.24MB)

Poetry (0.12.12) is installed now. Great!

To get started you need Poetry's bin directory ($HOME/.poetry/bin) in your `PATH`
environment variable. Next time you log in this will be done
automatically.

To configure your current shell run `source $HOME/.poetry/env`
```

## What does that give me

``` bash
[cig@nzxt talk]$ poetry
Poetry 0.12.12

Usage:
  command [options] [arguments]

Options:
  -h, --help                      Display this help message
  -q, --quiet                     Do not output any message
  -V, --version                   Display this application version
      --ansi                      Force ANSI output
      --no-ansi                   Disable ANSI output
  -n, --no-interaction            Do not ask any interactive question
  -v|vv|vvv, --verbose[=VERBOSE]  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  about          Short information about Poetry.
  add            Add a new dependency to pyproject.toml.
  build          Builds a package, as a tarball and a wheel by default.
  check          Checks the validity of the pyproject.toml file.
  config         Sets/Gets config options.
  develop        Installs the current project in development mode. (Deprecated)
  help           Displays help for a command
  init           Creates a basic pyproject.toml file in the current directory.
  install        Installs the project dependencies.
  list           Lists commands
  lock           Locks the project dependencies.
  new            Creates a new Python project at <path>
  publish        Publishes a package to a remote repository.
  remove         Removes a package from the project dependencies.
  run            Runs a command in the appropriate environment.
  script         Executes a script defined in pyproject.toml. (Deprecated)
  search         Searches for packages on remote repositories.
  shell          Spawns a shell within the virtual environment.
  show           Shows information about packages.
  update         Update dependencies as according to the pyproject.toml file.
  version        Bumps the version of the project.
 cache
  cache:clear    Clears poetry's cache.
 debug
  debug:info     Shows debug information.
  debug:resolve  Debugs dependency resolution.
 self
  self:update    Updates poetry to the latest version.
```

## Let's make a thing

``` bash
[cig@nzxt talk]$ poetry new talk
Created package talk in talk
```

And then this

``` bash
(py3) [cig@nzxt talk]$ poetry add whitenoise
Using version ^4.1 for whitenoise

Updating dependencies
Resolving dependencies... (3.5s)

Writing lock file


Package operations: 0 installs, 2 updates, 0 removals

  - Updating more-itertools (6.0.0 -> 7.0.0)
  - Updating pytest (4.3.0 -> 3.10.1)
(py3) [cig@nzxt talk]$ poetry add falcon
Using version ^1.4 for falcon

Updating dependencies
Resolving dependencies... (0.8s)

Writing lock file

Nothing to install or update

(py3) [cig@nzxt talk]$
```

## Add dev dependencies

``` bash
(py3) [cig@nzxt talk]$ poetry add --dev pylint
Using version ^2.3 for pylint

Updating dependencies
Resolving dependencies... (2.5s)

Writing lock file


Package operations: 7 installs, 1 update, 0 removals

  - Installing lazy-object-proxy (1.4.0)
  - Installing typed-ast (1.3.5)
  - Installing wrapt (1.11.1)
  - Installing astroid (2.2.5)
  - Installing isort (4.3.18)
  - Installing mccabe (0.6.1)
  - Installing pylint (2.3.1)
  - Updating pytest (4.4.1 -> 3.10.1)
(py3) [cig@nzxt talk]$
```