install:
	poetry install
	poetry build
	python3 -m pip install --force-reinstall --user dist/*.whl
	poetry publish --dry-run

uninstall:
	python3 -m pip uninstall hexlet-code
	rm -rf ../python-project-50/

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: gendiff
