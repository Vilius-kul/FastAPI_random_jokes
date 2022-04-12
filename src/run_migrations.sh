#!/bin/bash

piccolo migrations new jokes --auto

piccolo migrations forwards all

