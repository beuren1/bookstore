.PHONY: check
check: check-py

.PHONY: check-py
check-py: check-py-flake8 check-py-black check-py-mypy

.PHONY: check-py-flake8
check-py-flake8:
	poetry run flake8 .

.PHONY: check-py-black
check-py-black:
	poetry run black --check --line-length 118 --fast .

.PHONY: check-py-mypy
check-py-mypy:
	poetry run mypy .

.PHONY: format-py
format-py:
	poetry run black .

.PHONY: format-autopep8
format-autopep8:
	poetry run autopep8 --in-place --recursive .

.PHONY: format-isort
format-isort:
	poetry run isort .
