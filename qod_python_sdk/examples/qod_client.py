# qod_client.py
# Making Your Second 5G QoD App Using Direct API Calls

from base64 import b64encode, urlsafe_b64encode
from math import floor
from random import random
from hashlib import sha256
from time import time
from json import dumps
from authlib.jose import JsonWebSignature
from qod_python_sdk.src.tmode_qod.net.environment.environment import Environment

base_url = Environment.PRODUCTION.value
client_secret = "po3169iWK5RGmM2IS"
client_id = "tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA"

with open("private_key-pem", mode="r", encoding="utf-8", closefd=True) as private_pem_file:
    private_key = private_pem_file.read()

# ── Step 2: Add BASIC Auth token function
# The value returned by basic_auth_token() will be passed
# as the Authorization header when generating OAuth tokens. 
def basic_auth_token(client_id: str, client_secret: str) -> str:
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    token = b64encode(raw).decode("ascii")
    return f"Basic {token}"

# ── Step 3: Add supporting functions for GUID generation
# random_str() is used within create_guid(). citeturn1file1
def random_str(length: int = 4) -> str:
    return hex(floor((1 + random()) * 0x10000))[3:]

def create_guid() -> str:
    # returns xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    return "".join([
        random_str() + random_str() + "-",
        random_str() + "-",
        random_str() + "-",
        random_str() + "-",
        random_str() + random_str() + random_str(),
    ])

# ── Step 4a: Load your private_key.pem once
# The private_key value will be used for PoPToken generation. citeturn1file2
with open("../private_key.pem", "r", encoding="utf-8") as f:
    PRIVATE_KEY = f.read()

# ── Step 4b: Add low‑level PoPToken generator
def create_pop_token(obj_header_map, str_private_key_pem: str):
    # !! do NOT divide by 1000, time is already in seconds (NOT milliseconds)
    current_time_seconds = floor(time())
    exp_time = current_time_seconds + (2 * 60) # token is valid for 2 minutes
    str_headers = ''
    str_to_hash = ''
    
    for key in obj_header_map:
        value = obj_header_map[key]
        
        if len(str_headers) > 0:
            str_headers = str_headers + ";"
            
        str_headers = str_headers + key
        str_to_hash = str_to_hash + value
        
    str_hash = sha256(str_to_hash.encode())
    str_hash_hex = str_hash.hexdigest()
    str_header_values_hash_b64 = urlsafe_b64encode(bytes.fromhex(str_hash_hex)).decode()
    str_unique = create_guid()
    
    # !! NOTE - encode/decode leaves equals sign at end due to fixed length
    # more info - https://stackoverflow.com/a/6916831 or https://stackoverflow.com/a/9020716
    if str_header_values_hash_b64.endswith("="):
        str_header_values_hash_b64 = str_header_values_hash_b64[:-1]
        
    obj_claim = {}
    obj_claim["exp"] = exp_time
    obj_claim["iat"] = int(time())
    obj_claim["v"] = '1'
    
    if len(str_header_values_hash_b64) > 0:
        obj_claim["edts"] = str_header_values_hash_b64
        
    if len(str_headers) > 0:
        obj_claim["ehts"] = str_headers
        
    if len(str_unique) > 0:
        obj_claim["jti"] = str_unique
        
    str_claim = dumps(obj_claim, separators=(',', ':'))
    
    alg = 'RS256'
    obj_protected_headers = { 'alg': alg, 'typ': 'JWT' }
    jws = JsonWebSignature(algorithms=[alg])
    
    str_token = jws.serialize_compact(obj_protected_headers, str_claim, str_private_key_pem)
    
    return str_token

# 4d – Add PoPToken wrapper function 
# for convenience to make PoPToken generation simpler for future API calls
def create_url_pop_token(uri: str, method: str):
    return create_pop_token(
        {
            "Content-Type" : "application/json",
            "http-method" : method,
            "uri" : uri,
        },
        private_key,
    )
# 5. Add create_oauth_tokens function
# combines Auth token and PoPToken generation
def create_oauth_tokens(base_url: str, client_id: str, client_secret: str):
    method = "POST"
    uri = "/oauth2/v2/tokens"
    payload = ""
    
    authToken = basic_auth_token(client_id, client_secret)
    popToken = create_url_pop_token(uri, method)
    
    headers = {
        'Authorization': authToken,
        'Content-Type': 'application/json',
        'X-Authorization': popToken,
    }
    
    conn = HTTPSConnection(base_url)
    conn.request(method, uri, payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = loads(data.decode())
    
    return {
        "access_token": json_data['access_token'],
        "id_token": json_data['id_token'],
    }

# 6. Add qod_create_session function
# creates a QoD session, The value returned is a dict containing session info
def qod_create_session(oauth_tokens, phone_number: str, qos_profile: str, duration_secs = 30):
    method = "POST"
    uri = "/qod/v0/sessions"
    sessions_poptoken = create_url_pop_token(uri, method)
    headers = {
        'Authorization': "Bearer " + oauth_tokens["access_token"],
        'Content-Type': 'application/json',
        'X-Authorization': sessions_poptoken,
    }
    
    create_session_payload = dumps({
        # required params first - device, qosProfile
        "device": {
            "phoneNumber": phone_number,
        },
        "qosProfile": qos_profile,
        # optional params below
        "duration": duration_secs, # optional, default is 86400
    })
    
    print(
        "Creating session using",
        "qos='" + qos_profile + "'",
        "duration=" + str(duration_secs),
        "phoneNumber='" + phone_number + "'\n",
    )
    
    conn = HTTPSConnection(base_url)
    conn.request(method, uri, create_session_payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = loads(data)
    
    return json_data

# 7. Add qod_get_session function 
# retrieves a QoD session, the value returned is a dict containing session info
def qod_get_session(oauth_tokens, session_id: str):
    method = "GET"
    uri = "/qod/v0/sessions/" + session_id
    sessions_poptoken = create_url_pop_token(uri, method)
    headers = {
        'Authorization': "Bearer " + oauth_tokens["access_token"],
        'Content-Type': 'application/json',
        'X-Authorization': sessions_poptoken,
    }
    
    get_session_payload = ''
    print(
        "Retrieving session using",
        "session_id='" + session_id + "'\n",
    )
    
    conn = HTTPSConnection(base_url)
    conn.request(method, uri, get_session_payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = loads(data)
    
    return json_data

# 8. add qod_end_session function
# The value returned is a Boolean – 
# True if session was successfully ended, False otherwise
def qod_end_session(oauth_tokens, session_id: str):
    method = "DELETE"
    uri = "/qod/v0/sessions/" + session_id
    sessions_poptoken = create_url_pop_token(uri, method)
    headers = {
        'Authorization': "Bearer " + oauth_tokens["access_token"],
        'Content-Type': 'application/json',
        'X-Authorization': sessions_poptoken,
    }
    
    get_session_payload = ''
    print(
        "Ending session using",
        "session_id='" + session_id + "'\n",
    )
    
    conn = HTTPSConnection(base_url)
    conn.request(method, uri, get_session_payload, headers)
    res = conn.getresponse()
    data = res.read()
    str_data = data.decode()
    
    return str_data == ""

def main():
    oauth_tokens = create_oauth_tokens(base_url, client_id, client_secret)
    
    # create session below
    phone_number = "14253008314"
    session_resp = qod_create_session(oauth_tokens, phone_number, "QOS_VC")
    session_id = None
    
    try:
        session_id = session_resp['id']
    except KeyError:
        print(session_resp)
        print("❌ Unable to determine session ID, quitting program")
        return
    except:
        print("❌ Unknown error, quitting program")
        return
    else:
        print(f"\n✅ Created Session w/ ID = '{session_id}'\n")
    
    session_data = qod_get_session(oauth_tokens, session_id)
    print("\n✅ Session data retrieved\n")
    
    deletion_result = qod_end_session(oauth_tokens, session_id)
    
    if deletion_result:
        print(f"\n✅ Session w/ ID '{session_id}' has been deleted\n")
    else:
        print(f"Failed to delete session w/ ID '{session_id}'\n")
    
    print("🎉 Demo complete 🎉")

if __name__ == "__main__":
    main()