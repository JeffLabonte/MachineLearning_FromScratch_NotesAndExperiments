SHELL := /bin/bash

create_dev_env:
	python3.7 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt
