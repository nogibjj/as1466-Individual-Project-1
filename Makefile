install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval test_*.ipynb
	python -m pytest -vv --cov=.lib
	python -m pytest -vv  test_*.py

format:	
	black *.py
	nbqa black *.ipynb 

lint:
	nbqa ruff *.ipynb
	ruff check *.py
		
all: install lint test format
