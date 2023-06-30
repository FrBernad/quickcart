#!/bin/bash -e 


if [ "${TEST_TARGET:-}" = "INTEGRATION" ]; then
    # Execute your command here
    /usr/app/.venv/bin/gunicorn manage:app
else
    
    ## pytest
    echo "Running tests for ${SERVICE_NAME} service"
    python -m pytest "./src/tests" --junitxml=report.xml

    ## Coverage
    echo "Running coverage for ${SERVICE_NAME} service"
    python -m pytest "./src/tests" -p no:warnings --cov="." --cov-report xml
    
    ## Linting FIXME:   
    # echo "Running linter for ${SERVICE_NAME} service"
    # flake8 . --extend-ignore E221

fi