# README.md

## Overview
This project contains automated test suites for a user management web application, including:
- API tests (CRUD operations, authentication, data isolation)
- UI automation (user workflows, responsive design)
- Security tests (input validation, authorization)
- Performance tests (load, stress)

## Structure
/test-automation
├── api_tests/
├── ui_tests/
├── security_tests/
├── performance_tests/
├── fixtures/
├── utils/


## Requirements
- Python 3.x
- Selenium
- requests
- JMeter (for performance testing)

## How to Run
- API & security tests: `pytest api_tests/ security_tests/`
- UI tests: `pytest ui_tests/`
- Performance tests: Run JMeter `.jmx` files in `performance_tests/`
