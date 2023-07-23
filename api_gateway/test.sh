#!/bin/bash

if [[ "${ENV:-}" =~ ^qa ]]; then

    echo "Running integration tests for ${SERVICE_NAME}"
    python -m pytest "./src/tests/integration" -p no:warnings
    integration_tests_exit_status=$?

    if [ $integration_tests_exit_status -eq 0 ]; then
        exit 0
    else
        exit 1
    fi
