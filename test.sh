#!/bin/sh

set -xe

pycodestyle source
pydocstyle --add-ignore=D401 source
isort --check-only --diff --recursive source
flake8 source
