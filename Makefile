install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	
	python -m pytest --nbval *.ipynb
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

add_commit_push:
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add updated_BQ.csv; \
		git commit -m "Add generated plot image"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
