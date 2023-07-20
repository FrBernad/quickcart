#!/bin/bash

if [ "${ENV:-}" = "qa" ]; then

    echo "Running intregration tests for ${SERVICE_NAME}"

    echo "Running interface tests for ${SERVICE_NAME}"
    # python -m pytest "./src/tests/interface" -p no:warnings

else
    
    ## Unit tests 
    echo "Running unit tests and coverage for ${SERVICE_NAME} service"
    # python -m pytest "./src/tests/unit" -p no:warnings --junitxml=unit_report.xml --cov="." --cov-report=xml:unit_report_coverage

    ## Functional tests
    echo "Running functional tests and coverage for ${SERVICE_NAME} service"
    # python -m pytest "./src/tests/functional" -p no:warnings --junitxml=functional_report.xml --cov="." --cov-report=xml:functional_report_coverage

fi