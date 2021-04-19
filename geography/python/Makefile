.PHONY: dependencies dist pypi test coverage coverage-report install install-dev

dependencies:
	@echo "Installing dependencies:"
	pip3 install -r requirements.txt

dist:
	python3 setup.py sdist bdist_wheel

pypi:
	python3 setup.py sdist bdist_wheel upload

test: dependencies
	flake8 --max-line-length=120
	pytest .

coverage: dependencies
	coverage run --source=edxml_bricks pytest .

coverage-report: coverage
	coverage report

install:
	pip install .

install-dev:
	pip install -e .[dev]
