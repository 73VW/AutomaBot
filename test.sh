#!/bin/sh

set -xe

pycodestyle automabot
pydocstyle --add-ignore=D401 automabot
isort --check-only --diff --recursive automabot
flake8 automabot
rstcheck README.rst
