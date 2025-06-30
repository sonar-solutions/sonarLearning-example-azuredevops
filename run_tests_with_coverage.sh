#!/bin/bash

# Install required packages if not already installed
pip install pytest pytest-cov

# Run the tests with coverage and generate reports
pytest --cov=. --cov-report=xml:coverage.xml --cov-report=html:coverage_html tests/

echo "Coverage report generated in coverage.xml and coverage_html directory"
