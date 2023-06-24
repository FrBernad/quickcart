#!/bin/bash -e 


if [ "${TEST_TARGET:-}" = "INTEGRATION" ]; then
    # Execute your command here
    /usr/app/.venv/bin/gunicorn manage:app
else
    ## pytest
    echo "Running tests for ${SERVICE_NAME} service"
    python -m pytest "/usr/app/tests/" -v --junitxml=report.xml

    ## Coverage
    echo "Running coverage for ${SERVICE_NAME} service"
    python -m pytest "/usr/app/tests/" -v -p no:warnings --cov="." --cov-report xml

    ## Linting
    echo "Running linter for ${SERVICE_NAME} service"
    flake8 . --extend-ignore E221
    # black src --check
    # isort src --check

    ## Security
    # bandit -c .bandit.yml -r .
fi