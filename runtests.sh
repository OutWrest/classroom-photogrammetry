#!/usr/bin/env bash

py -m pip install --upgrade pip
py -m pip install flake8 pytest

if [ -f requirements.txt ]; then 
    py -m pip install -r requirements.txt; 
fi

mkdir temp
cp -R src/* temp/
cp -R tests/* temp/
cd temp
pytest . 
cd ..
rm -r temp