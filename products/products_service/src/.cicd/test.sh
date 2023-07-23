#!/bin/bash

if [[ "${ENV:-}" =~ ^qa ]]; then

    echo "Running integration tests for ${SERVICE_NAME}"
    python -m pytest "./src/tests/integration" -p no:warnings
    integration_tests_exit_status=$?

    echo "Running interface tests for ${SERVICE_NAME}"
    python -m pytest "./src/tests/interface" -p no:warnings
    interface_tests_exit_status=$?

    if [ $integration_tests_exit_status -eq 0 ] && [ $interface_tests_exit_status -eq 0 ]; then
        exit 0
    else
        exit 1
    fi


else
    
    ## Unit tests 
    echo "Running unit tests and coverage for ${SERVICE_NAME} service"
    python -m pytest "./src/tests/unit" -p no:warnings --junitxml=unit_report.xml --cov="." --cov-report=xml:unit_report_coverage
    unit_tests_exit_status=$?

    ## Functional tests
    echo "Running functional tests and coverage for ${SERVICE_NAME} service"
    python -m pytest "./src/tests/functional" -p no:warnings --junitxml=functional_report.xml --cov="." --cov-report=xml:functional_report_coverage
    functional_tests_exit_status=$?

    if [ $unit_tests_exit_status -eq 0 ] && [ $functional_tests_exit_status -eq 0 ]; then
        exit 0
    else
        exit 1
    fi

fi