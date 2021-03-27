#!/bin/bash

# this works with GitBash terminal

python -m venv venv
# for Windows
source venv/Scripts/activate
# for mac or linux
# source venv/bin/activate

python -m pip install -U pip
pip install -r requirements.txt

django-admin startproject online_store .