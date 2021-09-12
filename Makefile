PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: 
	poetry install --no-root
	poetry run python setup.py develop

## download nltk words
downloads:
	poetry run python download.py
