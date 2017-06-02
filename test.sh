#!/bin/sh

set -xe

pycodestyle mybot
pydocstyle --add-ignore=D401 mybot
isort --check-only --diff --recursive mybot
flake8 mybot
rstcheck README.rst
