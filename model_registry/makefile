SHELL := /bin/bash
include .env
export

lint:
	black model_registry
	autoflake -r -i model_registry
	black tests
	autoflake -r -i tests

mypy:
	mypy model_registry

isort:
	isort --profile black model_registry
	isort --profile black tests

neat: isort lint

test: neat
	pytest --cov=model_registry --cov-report term-missing --ignore=setup.py -vv

coverage:
	coverage run --source model_registry -m pytest
	coverage report -m
	coverage xml

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

requirements:
	python -m pip install -r requirements/requirements.txt
	python -m pip install -r requirements/requirements-test.txt

create-venv: ## crie um ambiente virtual
	rm -rf venv
	python3 -m venv venv

prepare-variables: ## crie as variáveis de ambiente do projeto
	cp -f .env.example .env

prepare-requirements-build:
	python3 -m pip install -r requirements/requirements_build.txt 

prepare-requirements-dev:
	python3 -m pip install -r requirements/requirements_dev.txt

prepare-requirements-test:
	python3 -m pip install -r requirements/requirements_setup.txt
	python3 -m pip install -r requirements/requirements_test.txt

prepare-requirements: ## instale ou atualize os requisitos do projeto
	@echo "Installing project's python requirements..."
	make prepare-requirements-build
	make prepare-requirements-dev
	make prepare-requirements-test

prepare-environment: ## crie e prepare o ambiente de desenvolvimento do projeto
	make create-venv \
	&& source venv/bin/activate \
	&& pip install --upgrade pip \
 	&& make prepare-requirements \
	&& echo "Environment ready!"

up:
	 uvicorn owl.main:application --host 0.0.0.0 --port 8090

deploy:
	rm -r -f ./build
	rm -r -f ./dist
	rm -r -f ./*.egg-info
	python setup.py sdist bdist_wheel
	(python -m pip install --upgrade pip \
	&& python -m pip install twine \
	&& twine upload dist/* )

export_env:
	set -o allexport; source .env; set +o allexport 