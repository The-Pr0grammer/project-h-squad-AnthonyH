#!/bin/bash

cd ./flask-template
source env_main/bin/activate
python -m unittest discover -v tests