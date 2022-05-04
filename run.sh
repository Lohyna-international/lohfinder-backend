#!/usr/bin/bash

pip3 install -r requirements.txt
pre-commit install
python3 -m uvicorn main:app --reload
