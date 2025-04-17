# The QodApiClient class encapsulates all the logic needed to authenticate with 
# T-Mobile’s QoD API, including generating OAuth and PoP tokens. It also provides 
# convenience methods to create, retrieve, and delete QoD sessions, so your main 
# script can interact with the API using simple, high-level calls.

from qod_client import QodApiClient
from tmode_qod import Environment

def main():
    client = QodApiClient(
        base_url      = Environment.PRODUCTION.value,
        client_id     = "tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA",
        client_secret = "po3169iWK5RGmM2IS",
        private_key_pem = open("../private_key.pem","r").read(),
    )

    tokens   = client.create_oauth_tokens()
    session  = client.qod_create_session(tokens, "1XXXXXXXXXX", "QOS_VC")
    sid      = session["sessionId"]
    print("Created:", sid)

    info     = client.qod_get_session(tokens, sid)
    print("Info:", info)

    deleted  = client.qod_end_session(tokens, sid)
    print("Deleted:", deleted)

if __name__ == "__main__":
    main()