#!/bin/bash

if [[ "${ENV:-}" =~ ^qa ]]; then

    echo "Running integration tests for ${SERVICE_NAME}"
    python -m pytest "./tests/integration" -p no:warnings --junitxml=integration_${SERVICE_NAME}_report.xml
    integration_tests_exit_status=$?

    echo "No interface tests needed" > interface_${SERVICE_NAME}_report.xml

    if [ $integration_tests_exit_status -eq 0 ]; then
        exit 0
    else
        exit 1
    fi

fi
