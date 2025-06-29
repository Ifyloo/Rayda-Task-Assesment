# TEST_STRATEGY.md

## Scope
Covers API, UI, performance, and security testing for the user management system.

## Approach
- Use `pytest` and `requests` for API and security tests.
- Use Selenium WebDriver (Python) for browser-based UI automation.
- Use Apache JMeter for performance testing.

## Test Types
- **API Tests:** CRUD, auth, data isolation.
- **UI Tests:** User workflows, responsive design checks.
- **Security Tests:** Input validation (XSS, SQLi), auth bypass attempts.
- **Performance Tests:** Load/stress tests using JMeter.

## Execution
- Run API/UI/security tests with `pytest`.
- Run JMeter tests by opening the `.jmx` files in JMeter GUI or via command line.
- Review logs and reports generated in console or files.

## Tools
- Python
- Pytest
- Selenium
- JMeter
- Requests

## Deliverables
- Test scripts in appropriate folders
- Test data in fixtures
- Utilities in utils
- This strategy document
