#!/bin/sh
virtualenv -p /opt/rh/python27/root/usr/bin/python V_ENV_TMP
source V_ENV_TMP/bin/activate
pip install wheel
#python setup.py build_py bdist_wheel upload -r daling
python setup.py build_py bdist_wheel
deactivate

