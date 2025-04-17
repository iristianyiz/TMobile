# CreateSession

**Properties**

Name | Type | Required | Description
device | Device | ✅ | End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators. The developer can choose to provide the following device identifiers:  - ipv4Address  - ipv6Address  - phoneNumber  - networkAccessIdentifier  NOTE: The MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. These identifiers must belong to the same device.
qos_profile | str | ✅ | A unique name for identifying a specific QoS profile. This may follow different formats depending on the service provider's implementation. Examples include:  - A UUID-style string  - Support for predefined profiles: QOS_VC, QOS_XR, QOS_RVM, QOS_POSALE, and QOS_BROADCAST  - A searchable descriptive name
application_server | ApplicationServer | ❌ | A server hosting backend applications to deliver business logic to clients. The developer can choose to provide the following device identifiers:  - ipv4Address  - ipv6Address
device_ports | PortsSpec | ❌ | 
application_server_ports | PortsSpec | ❌ | 
webhook | CreateSessionWebhook | ❌ | 
duration | int | ❌ | Session duration in seconds. The minimum value is 60 seconds, and if not set, the maximum value of 24 hours will be used.

# CreateSessionWebhook

**Properties**

Name | Type | Required | Description
notification_url | str | ❌ | Allows asynchronous delivery of session-related events.
notification_auth_token | str | ❌ | Authentication token for the callback API.