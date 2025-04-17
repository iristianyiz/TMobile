# Features: 
# Uninterrupted service
# Giving status updates and real-time alerts of work
# Power outage alerts
# Out of range pH/temperature alerts
# Optional Features:
# High resolution of microscopic photo uploads for research purposes.
    
from http.client import HTTPSConnection
from json import dumps, loads
from qod_python_sdk.examples.qod_client import create_oauth_tokens

# ── Hackathon Example: QoD Request from Smart Incubator
# use QOS_RVM - real-time urgency
def trigger_qod_session_for_alert(base_url, client_id, client_secret, phone_number, qos_profile="QOS_RVM"):
    tokens = create_oauth_tokens(base_url, client_id, client_secret)

    uri = "/qod/v0/sessions"
    method = "POST"
    headers = {
        "Authorization": tokens["access_token"],
        "X-Authorization": tokens["id_token"],
        "Content-Type": "application/json"
    }
    # dumps converts a Python object (like a dictionary) into a JSON-formatted string, 
    # which is what HTTP APIs typically expect in the body of a request
    body = dumps({ 
        "device": {"phoneNumber": phone_number},
        "qosProfile": qos_profile,
        "duration": 30
    })

    conn = HTTPSConnection(base_url, timeout=10_000)
    conn.request(method, uri, body, headers)
    res = conn.getresponse()
    data = res.read().decode()
    print("QoD Session Triggered:", data)
    return loads(data)

# Example usage for smart incubator alert
if __name__ == "__main__":
    BASE_URL = "api-ue1.tmowebservices.com"
    CLIENT_ID = "<YOUR_CLIENT_ID>"
    CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
    PHONE_NUMBER = "1XXXXXXXXXX"

    # Simulate an emergency: pH too low, alert lab
    # VC: video calling - media-optimized throughput
    trigger_qod_session_for_alert(BASE_URL, CLIENT_ID, CLIENT_SECRET, PHONE_NUMBER, qos_profile="QOS_VC")
