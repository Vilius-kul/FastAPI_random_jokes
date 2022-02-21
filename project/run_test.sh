#!/bin/bash

current_dir=$(pwd)
export PYTHONPATH=$PYTHONPATH:$current_dir


pytest --cov -v