HOST ?= 0.0.0.0
PORT ?= 8000
WORKER ?= 4
TAG ?= 0.1
FILES = project tests manage.py

dev:
	FLASK_ENV=development poetry run python manage.py run -p $(PORT) -h $(HOST) --reload

image:
	make lint || (echo "Error during linting"; exit 1)
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker build -f Dockerfile -t simon7426/portfolio-blog-api:$(TAG) . || true
	rm requirements.txt

test:
	poetry run pytest

flake8:
	@for file in $(FILES); do \
		echo "Checking $$file for error"; \
		poetry run flake8 $$file; \
	done

black:
	@for file in $(FILES); do \
		echo "Formatting $$file"; \
		poetry run black $$file; \
	done

isort:
	@for file in $(FILES); do \
		echo "Sorting $$file"; \
		poetry run isort $$file --profile black; \
	done

audit_dependencies:
	poetry export --without-hashes -f requirements.txt | poetry run safety check --output bare --stdin

dockerfile_linter:
	docker run --rm -e HADOLINT_IGNORE=DL3018,DL4006,SC2086 -i hadolint/hadolint < Dockerfile

coverage:
	poetry run coverage run -m pytest
	poetry run coverage report -m

bandit:
	poetry run bandit -r project

validate_openapi_schema:
	poetry run python manage.py generate-schema
	poetry run openapi-spec-validator docs/api/openapi.yaml

tox:
	poetry run tox

toml_sort:
	poetry run toml-sort pyproject.toml --all --in-place

lint: toml_sort validate_openapi_schema dockerfile_linter isort black flake8 dockerfile_linter

audit: audit_dependencies bandit
