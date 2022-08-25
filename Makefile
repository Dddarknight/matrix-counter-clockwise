lint:
	poetry run flake8 matrix_loader

install:
	poetry install

test-coverage:
	poetry run pytest --cov=matrix_loader --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest

package-install:
	python3 -m pip install dist/matrix_counter_clockwise-0.1.0-py3-none-any.whl