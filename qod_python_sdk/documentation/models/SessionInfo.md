# SessionInfo

**Properties**

Name | Type | Required | Description
device | Device | ✅ | End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators. The developer can choose to provide the following device identifiers:  - ipv4Address  - ipv6Address  - phoneNumber  - networkAccessIdentifier  NOTE: The MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. These identifiers must belong to the same device.
qos_profile | str | ✅ | A unique name for identifying a specific QoS profile. This may follow different formats depending on the service provider's implementation. Some options include:  - A UUID-style string  - Predefined profiles: QOS_VC, QOS_XR, QOS_RVM, QOS_POSALE, QOS_BROADCAST  - A searchable descriptive name
session_id | str | ✅ | Session ID in UUID format
duration | int | ✅ | The duration of the session in seconds
started_at | int | ✅ | Timestamp of session start, in seconds since the Unix epoch
expires_at | int | ✅ | Timestamp of session expiration if the session was not deleted, in seconds since the Unix epoch
qos_status | QosStatus | ✅ | The current status of the requested QoS session. The status can be one of the following:  - AVAILABLE - The requested QoS has been provided by the network
application_server | ApplicationServer | ❌ | A server hosting backend applications to deliver business logic to clients. The developer can choose to provide the following device identifiers:  - ipv4Address  - ipv6Address
device_ports | PortsSpec | ❌ | 
application_server_ports | PortsSpec | ❌ | 
webhook | SessionInfoWebhook | ❌ | 
messages | List[Message] | ❌ | 


# SessionInfoWebhook

**Properties**

Name | Type | Required | Description
notification_url | str | ❌ | Allows asynchronous delivery of session-related events.
notification_auth_token | str | ❌ | Authentication token for the callback API.
