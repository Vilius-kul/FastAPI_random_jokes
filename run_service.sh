#!/bin/bash

current_dir=$(pwd)
export PYTHONPATH=$PYTHONPATH:$current_dir

python src/main.py

