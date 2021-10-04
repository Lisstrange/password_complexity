PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
pyenv_install:
	sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
	libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
	libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
	curl https://pyenv.run | bash

pyenv_setup:
	echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
	echo 'eval "$(pyenv init -)"' >> ~/.bashrc
	export PATH="~/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"
	source ~/.bashrc
	pyenv
virtualenv:
	pyenv install -v 3.9.0
	pyenv virtualenv 3.9.0 password_complexity 
	pyenv local password_complexity

poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
	source $HOME/.poetry/env
requirements: 
	poetry install --no-root
	poetry run python setup.py develop

## download nltk words
downloads:
	poetry run python download.py
