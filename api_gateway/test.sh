#!/bin/bash

if [[ "${ENV:-}" =~ ^qa ]]; then

    echo "Running integration tests for ${SERVICE_NAME}"
    python -m pytest "./tests/integration" -p no:warnings --junitxml=integration_${SERVICE_NAME}_report.xml
    integration_tests_exit_status=$?

    echo "Running interface tests for ${SERVICE_NAME}"
    export BUILD_ID=$(date +%Y%m%d%H%M%S)
    python -m pytest "./tests/interface" -p no:warnings --junitxml=interface_${SERVICE_NAME}_report.xml
    interface_tests_exit_status=$?
    
    if [ $integration_tests_exit_status -eq 0 ] && [ $interface_tests_exit_status -eq 0 ]; then
        exit 0
    else
        exit 1
    fi

fi
