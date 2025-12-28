.PHONY: help install test demo example

PYTHON ?= python
PIP ?= pip
PYTEST ?= pytest
STREAMLIT ?= streamlit

help:
	@echo "Available commands:"
	@echo "  make install    Install dependencies"
	@echo "  make test       Run unit tests"
	@echo "  make example    Run example script"
	@echo "  make demo       Run Streamlit demo app"
	@echo "  make clean      Remove __pycache__ and pytest cache"

install:
	$(PIP) install -r requirements.txt

test:
	PYTHONPATH=. $(PYTEST)

example:
	PYTHONPATH=. $(PYTHON) example.py

demo:
	PYTHONPATH=. $(STREAMLIT) run demo.py

clean:
	@echo "Cleaning __pycache__ and pytest cache..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache

