install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

.PHONY: gendiff
