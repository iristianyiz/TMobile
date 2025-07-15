"""
Common pytest configuration and fixtures for the QoD SDK tests.
"""
import pytest
import os
import sys
from unittest.mock import Mock, patch

# Add the src directory to the path so we can import the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


@pytest.fixture(scope="session")
def test_credentials():
    """
    Fixture to provide test credentials.
    In a real environment, these would be loaded from environment variables or config files.
    """
    return {
        "client_id": os.getenv("QOD_CLIENT_ID", "<YOUR_CLIENT_ID>"),
        "client_secret": os.getenv("QOD_CLIENT_SECRET", "<YOUR_CLIENT_SECRET>"),
        "private_key_path": os.getenv("QOD_PRIVATE_KEY_PATH", "private_key.pem"),
    }


@pytest.fixture(scope="session")
def mock_private_key():
    """
    Fixture to provide a mock private key for testing.
    """
    return """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7VJTUt9Us8cKB
AgEAAoIBAQC7VJTUt9Us8cKB
-----END PRIVATE KEY-----"""


@pytest.fixture(scope="session")
def mock_oauth_tokens():
    """
    Fixture to provide mock OAuth tokens for testing.
    """
    return {
        "access_token": "mock_access_token_12345",
        "id_token": "mock_id_token_12345",
        "token_type": "Bearer",
        "expires_in": 3600
    }


@pytest.fixture(scope="session")
def mock_session_response():
    """
    Fixture to provide mock session response for testing.
    """
    return {
        "sessionId": "test_session_id_12345",
        "id": "test_session_id_12345",
        "status": "active",
        "device": {
            "phoneNumber": "1XXXXXXXXXX"
        },
        "qosProfile": "QOS_RVM",
        "duration": 30
    }


@pytest.fixture(autouse=True)
def mock_environment(monkeypatch):
    """
    Automatically mock environment variables for testing.
    """
    # Mock environment variables that might be used
    monkeypatch.setenv("QOD_CLIENT_ID", "test_client_id")
    monkeypatch.setenv("QOD_CLIENT_SECRET", "test_client_secret")
    monkeypatch.setenv("QOD_PRIVATE_KEY_PATH", "test_private_key.pem")


@pytest.fixture
def mock_http_requests(monkeypatch):
    """
    Fixture to mock HTTP requests for testing.
    """
    with patch('requests.Session.request') as mock_request:
        # Configure default responses
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success"}
        mock_response.text = '{"status": "success"}'
        mock_request.return_value = mock_response
        
        yield mock_request 