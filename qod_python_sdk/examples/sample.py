# Learning Objectives: Create an application; Verify your QoD setup is working
# using only the SDK’s built‑in session methods
# Use the SDK (TmodeQod): you don’t need QodApiClient at all.

from tmode_qod import TmodeQod, Environment
from tmode_qod.models import CreateSession
from tmode_qod.models.device import Device

# ── CONFIG ───────────────────────────────────────────────────────────
BASE_URL      = Environment.PRODUCTION.value    # or DEFAULT.value for sandbox
CLIENT_ID     = "tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA"
CLIENT_SECRET = "po3169iWK5RGmM2IS"

# Option A: Inline your PEM
# PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
# your-full-private-key-PEM-contents
# -----END PRIVATE KEY-----"""

# Option B: Read from file
with open("private_key.pem", "r", encoding="utf-8") as f:
     PRIVATE_KEY = f.read()

def main():
    sdk = TmodeQod(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        private_key=PRIVATE_KEY,
        base_url=BASE_URL,
        timeout=10_000,
    )

    # 1️⃣ CREATE a QoD session
    create_req = CreateSession(
        device=Device(phone_number="1XXXXXXXXXX"),  # replace with your MSISDN
        qos="QOS_VC",
        duration=30,
    )
    created = sdk.session.create_session(request_body=create_req)
    session_id = created.id
    print(f"Created session: {session_id}")

    # 2️⃣ GET session info
    info = sdk.session.get_session(session_id=session_id)
    print("Session info:", info)

    # 3️⃣ DELETE the session
    resp = sdk.session.delete_session(session_id=session_id)
    if resp == b"":
        print(f"✅ Session {session_id} deleted")
    else:
        print("Delete response:", resp)

if __name__ == "__main__":
    main()


# from tmode_qod import TmodeQod, Environment

# sdk = TmodeQod(
#     client_id="tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA",
#     client_secret="po3169iWK5RGmM2IS",
#     private_key="-----BEGIN PRIVATE KEY-----privatekey",
#     base_url=Environment.DEFAULT.value,
#     timeout=10000,
# )

# # hard coded GET 
# result = sdk.session.get_session(
#     session_id="123e4567-e89b-12d3-a456-426614174000",
#     x_correlator="233b55ed-4a48-4f33-9efe-6fc277f66e8d",
# )

# print(result)

# samples/sample.py