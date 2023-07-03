#!/bin/bash -e 


if [ "${ENV:-}" = "qa" ]; then

    echo "Initializing ${SERVICE_NAME} for interface and integration testing"
    gunicorn -b 0.0.0.0:5000 main:app &

    app_pid = $!

    echo "Waiting for the app to initialize..."
    sleep 3
    echo "${SERVICE_NAME} initialized"

    echo "Running interface tests for ${SERVICE_NAME}"
    python -m pytest "./src/tests/interface" -p no:warnings

    kill $app_pid

    gunicorn -b 0.0.0.0:5000 main:app &

    wait $!

else
    
    ## Unit tests 
    echo "Running unit tests and coverage for ${SERVICE_NAME} service"
    python -m pytest "./src/tests/unit" -p no:warnings --junitxml=report.xml --cov="." --cov-report xml

    ## Functional tests
    echo "Running functional tests and coverage for ${SERVICE_NAME} service"
    python -m pytest "./src/tests/functional" -p no:warnings --junitxml=report.xml --cov="." --cov-report xml

    ## Linting TODO:   
    # echo "Running linter for ${SERVICE_NAME} service"
    # flake8 . --extend-ignore E221

fi