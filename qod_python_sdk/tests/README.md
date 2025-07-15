# QoD SDK Tests

This directory contains the test suite for the T-Mobile Quality-on-Demand (QoD) Python SDK.

## Setup

1. Install the test dependencies:
   ```bash
   pip install -e ".[test]"
   ```

2. Set up your test credentials (optional):
   ```bash
   export QOD_CLIENT_ID="your_client_id"
   export QOD_CLIENT_SECRET="your_client_secret"
   export QOD_PRIVATE_KEY_PATH="path/to/your/private_key.pem"
   ```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run tests with verbose output:
```bash
pytest -v
```

### Run specific test file:
```bash
pytest tests/test_qod_client.py
```

### Run tests with coverage:
```bash
pytest --cov=src/tmode_qod
```

### Skip slow tests:
```bash
pytest -m "not slow"
```

### Run only integration tests:
```bash
pytest -m integration
```

## Test Structure

- `conftest.py`: Common fixtures and configuration
- `test_qod_client.py`: Tests for the QoD API client functionality

## Test Categories

- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test the interaction between components
- **Slow Tests**: Tests that take longer to run (marked with `@pytest.mark.slow`)

## Mocking

The tests use mocking to avoid making actual API calls during testing. This ensures:
- Tests run quickly and reliably
- No dependency on external services
- Consistent test results
- No accidental charges or side effects

## Adding New Tests

1. Create a new test file with the prefix `test_`
2. Use the fixtures from `conftest.py` when possible
3. Mark slow tests with `@pytest.mark.slow`
4. Mark integration tests with `@pytest.mark.integration`
5. Add appropriate docstrings to describe what each test does

## Test Data

Test data is provided through fixtures in `conftest.py`. This includes:
- Mock credentials
- Mock OAuth tokens
- Mock session responses
- Mock HTTP responses

## Continuous Integration

These tests are designed to run in CI/CD pipelines. They:
- Don't require external dependencies
- Use mocking to avoid API calls
- Provide clear pass/fail results
- Include coverage reporting 