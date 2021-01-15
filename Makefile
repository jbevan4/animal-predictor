init-local-dev:
  pip install -r requirements/dev.txt

init-notebook:
  pip install -r requirements/notebook.txt

init-prod:
  pip install -r requirements/prod.txt

test:
  pytest -svv

.PHONE: init-local-dev init-notebook init-prod test
  