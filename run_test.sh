#!/bin/bash

current_dir=$(pwd)
export PYTHONPATH=$PYTHONPATH:$current_dir


pytest --cov-report term-missing:skip-covered --cov -v

