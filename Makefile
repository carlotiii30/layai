PYTHON := python3
POETRY := poetry
BACKEND_DIR := backend

.PHONY: install test lint

install:
	cd $(BACKEND_DIR) && $(POETRY) install

test:
	cd $(BACKEND_DIR) && $(POETRY) run pytest -s

lint:
	cd $(BACKEND_DIR) && $(POETRY) run flake8

serve:
	cd $(BACKEND_DIR) && $(POETRY) run uvicorn app.main:app --reload