install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:	
	python -m py.test --nbval jupyter_notebook/*.ipynb 
	python -m py.test -vv --cov=python_script python_script/*.py
	python -m py.test -vv --cov=lib

format:
	nbqa black  \jupyter_notebook/*.ipynb &&\
		black \python_script/*.py &&\
			black \src/*.py

lint:
	nbqa ruff \jupyter_notebook/*.ipynb &&\
		ruff check \python_script/*.py &&\
			ruff check \src/*.py

all: install test format lint