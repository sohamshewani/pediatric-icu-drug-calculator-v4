.PHONY: test build clean

TESTS = tests
REQUIREMENTS = requirements.txt

all: test

test:
	pip install -r $(REQUIREMENTS)
	make test_runner

test_runner:
	@echo Running tests...
	python -m unittest discover -s tests -p 'test_*.py'

build:
	@echo Building...
	python src/main.py

clean:
	@echo Cleaning...
	rm -rf build dist