#!/bin/sh
virtualenv -p V_ENV_TMP
source V_ENV_TMP/bin/activate
python setup.py develop

