.PHONY: dependencies dist pypi test coverage coverage-report install install-dev

dependencies:
	@echo "Installing dependencies:"
	pip3 install -r requirements.txt
	pip3 install flake8 pytest

dist:
	pip3 install wheel
	rm -rf build dist edxml_bricks_computing_networking.egg-info
	python3 setup.py sdist bdist_wheel

pypi: dist
	# NOTE: twine will read TWINE_USERNAME and TWINE_PASSWORD from environment
	pip3 install twine
	twine check dist/*
	@echo "Uploading to PyPI:"
	twine upload dist/*

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
