# SessionService

A list of all methods in the `SessionService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                                                                                                                                                                                                        |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_session](#create_session) | Create QoS Session to manage latency/throughput priorities If the qosStatus in the API response is "AVAILABLE" means the QoS Session created successfully. IMPORTANT: Callback Notifiications functionality will be implemented in future releases |
| [get_session](#get_session)       | Retrieves information for a specific QoS session using the session ID. This endpoint allows you to get the current status and details of the session created via the createSession operation. It is useful for monitoring and debugging purposes.  |
| [delete_session](#delete_session) | Deletes a specific QoS session using the session ID, freeing up any resources associated with the session. This endpoint is useful for terminating sessions that are no longer needed, ensuring efficient resource management.                     |

## create_session

Create QoS Session to manage latency/throughput priorities If the qosStatus in the API response is "AVAILABLE" means the QoS Session created successfully. IMPORTANT: Callback Notifiications functionality will be implemented in future releases

- HTTP Method: `POST`
- Endpoint: `/sessions`

**Parameters**

| Name         | Type                                        | Required | Description                                                                       |
| :----------- | :------------------------------------------ | :------- | :-------------------------------------------------------------------------------- |
| request_body | [CreateSession](../models/CreateSession.md) | ✅       | The request body.                                                                 |
| x_correlator | str                                         | ❌       | The transaction ID is GUID. Represents the API transaction, for use in debugging. |

**Return Type**

`SessionInfo`

**Example Usage Code Snippet**

```python
from tmode_qod import TmodeQod, Environment
from tmode_qod.models import CreateSession

sdk = TmodeQod(
    client_id="tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA",
    client_secret="po3169iWK5RGmM2IS",
    private_key="-----BEGIN PRIVATE KEY-----privatekey",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateSession(
    device={
        "phone_number": "123456789",
        "network_access_identifier": "123456789@domain.com",
        "ipv4_address": {
            "public_address": "84.125.93.10",
            "private_address": "84.125.93.10",
            "public_port": 47698
        },
        "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
    },
    application_server={
        "ipv4_address": "192.168.0.1/24",
        "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
    },
    device_ports={
        "ranges": [
            {
                "from_": 15584,
                "to": 21894
            }
        ],
        "ports": [
            40225
        ]
    },
    application_server_ports={
        "ranges": [
            {
                "from_": 15584,
                "to": 21894
            }
        ],
        "ports": [
            40225
        ]
    },
    qos_profile="QOS_VC",
    webhook={
        "notification_url": "https://application-server.com",
        "notification_auth_token": "c8974e592c2fa383d4a3960714"
    },
    duration=86400
)

result = sdk.session.create_session(
    request_body=request_body,
    x_correlator="233b55ed-4a48-4f33-9efe-6fc277f66e8d"
)

print(result)
```

## get_session

Retrieves information for a specific QoS session using the session ID. This endpoint allows you to get the current status and details of the session created via the createSession operation. It is useful for monitoring and debugging purposes.

- HTTP Method: `GET`
- Endpoint: `/sessions/{sessionId}`

**Parameters**

| Name         | Type | Required | Description                                                                       |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------- |
| session_id   | str  | ✅       | Session ID that was obtained from the createSession operation                     |
| x_correlator | str  | ❌       | The transaction ID is GUID. Represents the API transaction, for use in debugging. |

**Return Type**

`SessionInfo`

**Example Usage Code Snippet**

```python
from tmode_qod import TmodeQod, Environment

sdk = TmodeQod(
    client_id="tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA",
    client_secret="po3169iWK5RGmM2IS",
    private_key="-----BEGIN PRIVATE KEY-----privatekey",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.session.get_session(
    session_id="123e4567-e89b-12d3-a456-426614174000",
    x_correlator="233b55ed-4a48-4f33-9efe-6fc277f66e8d"
)

print(result)
```

## delete_session

Deletes a specific QoS session using the session ID, freeing up any resources associated with the session. This endpoint is useful for terminating sessions that are no longer needed, ensuring efficient resource management.

- HTTP Method: `DELETE`
- Endpoint: `/sessions/{sessionId}`

**Parameters**

| Name         | Type | Required | Description                                                                       |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------- |
| session_id   | str  | ✅       | Session ID that was obtained from the createSession operation                     |
| x_correlator | str  | ❌       | The transaction ID is GUID. Represents the API transaction, for use in debugging. |

**Example Usage Code Snippet**

```python
from tmode_qod import TmodeQod, Environment

sdk = TmodeQod(
    client_id="tmon-i98Bo7GwLDnAtyROcw44kNQA4vEUoVMA",
    client_secret="po3169iWK5RGmM2IS",
    private_key="-----BEGIN PRIVATE KEY-----privatekey",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.session.delete_session(
    session_id="123e4567-e89b-12d3-a456-426614174000",
    x_correlator="233b55ed-4a48-4f33-9efe-6fc277f66e8d"
)

print(result)
```
