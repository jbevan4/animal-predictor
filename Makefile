init-local-dev: 
	python -m venv dev-venv
	pip install -r requirements/dev.txt

init-notebook:
	python -m venv notebook-venv
	pip install -r requirements/notebook.txt

init-prod:
	python -m venv prod-venv
	pip install -r requirements/prod.txt

test:
	pytest -svv

.PHONE: init-local-dev init-notebook init-prod test
