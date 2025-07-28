.PHONY: test coverage clean run test-clean

PYTHON = python
COVERAGE = coverage

test-clean:
	rm -f profiles/migrations/0002_copy_data_from_old_models.py
	$(PYTHON) manage.py test lettings oc_lettings_site profiles

test:
	$(PYTHON) manage.py test lettings oc_lettings_site profiles

test-coverage:
	$(COVERAGE) run --source='.' manage.py test lettings oc_lettings_site profiles
	$(COVERAGE) report
	$(COVERAGE) html

run:
	$(PYTHON) manage.py runserver

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +

all: test-clean 