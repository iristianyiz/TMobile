import time
import os
import pytest
import sys
from unittest.mock import patch, Mock

from tmode_qod import TmodeQod
from tmode_qod.net.environment import Environment
from tmode_qod.net.qod_api_client import QodApiClient


client = QodApiClient(
    base_url=Environment.PRODUCTION.value,
    client_id="<YOUR_CLIENT_ID>",
    client_secret="<YOUR_CLIENT_SECRET>",
    private_key_pem=open("private_key.pem", "r").read(),
)

@pytest.fixture(scope="module")
def tokens():
    return client.create_oauth_tokens()

def test_create_session(tokens):
    session = client.qod_create_session(tokens, "1XXXXXXXXXX", "QOS_RVM")
    assert "sessionId" in session
    global session_id
    session_id = session["sessionId"]

def test_get_session(tokens):
    info = client.qod_get_session(tokens, session_id)
    assert info is not None

def test_expired_token_behavior(tokens):
    print("Simulating token expiration...")
    time.sleep(130)
    with pytest.raises(Exception):
        client.qod_end_session(tokens, session_id)

def test_delete_with_fresh_token():
    new_tokens = client.create_oauth_tokens()
    result = client.qod_end_session(new_tokens, session_id)
    assert result == True or result == b""
