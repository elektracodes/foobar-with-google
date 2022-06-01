#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 ]] ; then
    echo 'Error: no target directory provided!'
    exit 1
fi

if [[ ! -d $1 ]] ; then
    echo "Error: Directory \"$1\" does not exist!"
    exit 1
fi

cd $1

docker run --interactive \
    --tty \
    --rm \
    --name foobar-with-google \
    --volume "$PWD":/usr/src/foobar-with-google \
    --workdir /usr/src/foobar-with-google \
    python:2.7.13 python solution.py