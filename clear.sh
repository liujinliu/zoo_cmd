#!/bin/sh
rm -rf V_ENV/
rm -rf build/
rm -rf dist/
pushd src/
rm -rf zoo_cmd.egg-info/
pushd zoo_cmd/
rm -f */*.pyc
rm *.pyc
popd
popd

