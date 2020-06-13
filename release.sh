#!/bin/sh
# TODO: Add verison argument, edit osewb.version, commit, tag, and push.
# https://github.com/plyint/encpass.sh
. encpass.sh

export TWINE_PASSWORD=$(get_secret pypi password)

# exit when any command fails
set -e

# print commands before executing
set -x
twine upload --username gbroques dist/*

# Set conda to always upload a successful build to Anaconda.org with the command:
#     conda config --set anaconda_upload yes
conda build .
