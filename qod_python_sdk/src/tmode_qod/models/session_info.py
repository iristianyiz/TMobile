from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .device import Device
from .application_server import ApplicationServer
from .ports_spec import PortsSpec
from .qos_status import QosStatus
from .message import Message


@JsonMap(
    {
        "notification_url": "notificationUrl",
        "notification_auth_token": "notificationAuthToken",
    }
)
class SessionInfoWebhook(BaseModel):
    """SessionInfoWebhook

    :param notification_url: Allows asynchronous delivery of session related events, defaults to None
    :type notification_url: str, optional
    :param notification_auth_token: Authentication token for callback API, defaults to None
    :type notification_auth_token: str, optional
    """

    def __init__(
        self, notification_url: str = None, notification_auth_token: str = None
    ):
        """SessionInfoWebhook

        :param notification_url: Allows asynchronous delivery of session related events, defaults to None
        :type notification_url: str, optional
        :param notification_auth_token: Authentication token for callback API, defaults to None
        :type notification_auth_token: str, optional
        """
        self.notification_url = notification_url
        self.notification_auth_token = notification_auth_token


@JsonMap(
    {
        "application_server": "applicationServer",
        "device_ports": "devicePorts",
        "application_server_ports": "applicationServerPorts",
        "qos_profile": "qosProfile",
        "session_id": "sessionId",
        "started_at": "startedAt",
        "expires_at": "expiresAt",
        "qos_status": "qosStatus",
    }
)
class SessionInfo(BaseModel):
    """SessionInfo

    :param device: End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators. The developer can choose to provide the below specified device identifiers: * `ipv4Address` * `ipv6Address` * `phoneNumber` * `networkAccessIdentifier` NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
    :type device: Device
    :param application_server: A server hosting backend applications to deliver some business logic to clients. The developer can choose to provide the below specified device identifiers: * `ipv4Address` * `ipv6Address` , defaults to None
    :type application_server: ApplicationServer, optional
    :param device_ports: device_ports, defaults to None
    :type device_ports: PortsSpec, optional
    :param application_server_ports: application_server_ports, defaults to None
    :type application_server_ports: PortsSpec, optional
    :param qos_profile: A unique name for identifying a specific QoS profile. This may follow different formats depending on the service providers implementation. Some options addresses:   - A UUID style string   - Support for predefined profiles QOS_VC, QOS_XR, QOS_RVM, QOS_POSALE and QOS_BROADCAST   - A searchable descriptive name
    :type qos_profile: str
    :param webhook: webhook, defaults to None
    :type webhook: SessionInfoWebhook, optional
    :param session_id: Session ID in UUID format
    :type session_id: str
    :param duration: duration
    :type duration: int
    :param started_at: Timestamp of session start in seconds since Unix epoch
    :type started_at: int
    :param expires_at: Timestamp of session expiration if the session was not deleted, in seconds since Unix epoch
    :type expires_at: int
    :param qos_status: The current status of the requested QoS session. The status can be one of the following: * `AVAILABLE` - The requested QoS has been provided by the network
    :type qos_status: QosStatus
    :param messages: messages, defaults to None
    :type messages: List[Message], optional
    """

    def __init__(
        self,
        device: Device,
        qos_profile: str,
        session_id: str,
        duration: int,
        started_at: int,
        expires_at: int,
        qos_status: QosStatus,
        application_server: ApplicationServer = None,
        device_ports: PortsSpec = None,
        application_server_ports: PortsSpec = None,
        webhook: SessionInfoWebhook = None,
        messages: List[Message] = None,
    ):
        """SessionInfo

        :param device: End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators. The developer can choose to provide the below specified device identifiers: * `ipv4Address` * `ipv6Address` * `phoneNumber` * `networkAccessIdentifier` NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
        :type device: Device
        :param application_server: A server hosting backend applications to deliver some business logic to clients. The developer can choose to provide the below specified device identifiers: * `ipv4Address` * `ipv6Address` , defaults to None
        :type application_server: ApplicationServer, optional
        :param device_ports: device_ports, defaults to None
        :type device_ports: PortsSpec, optional
        :param application_server_ports: application_server_ports, defaults to None
        :type application_server_ports: PortsSpec, optional
        :param qos_profile: A unique name for identifying a specific QoS profile. This may follow different formats depending on the service providers implementation. Some options addresses:   - A UUID style string   - Support for predefined profiles QOS_VC, QOS_XR, QOS_RVM, QOS_POSALE and QOS_BROADCAST   - A searchable descriptive name
        :type qos_profile: str
        :param webhook: webhook, defaults to None
        :type webhook: SessionInfoWebhook, optional
        :param session_id: Session ID in UUID format
        :type session_id: str
        :param duration: duration
        :type duration: int
        :param started_at: Timestamp of session start in seconds since Unix epoch
        :type started_at: int
        :param expires_at: Timestamp of session expiration if the session was not deleted, in seconds since Unix epoch
        :type expires_at: int
        :param qos_status: The current status of the requested QoS session. The status can be one of the following: * `AVAILABLE` - The requested QoS has been provided by the network
        :type qos_status: QosStatus
        :param messages: messages, defaults to None
        :type messages: List[Message], optional
        """
        self.device = self._define_object(device, Device)
        self.application_server = self._define_object(
            application_server, ApplicationServer
        )
        self.device_ports = self._define_object(device_ports, PortsSpec)
        self.application_server_ports = self._define_object(
            application_server_ports, PortsSpec
        )
        self.qos_profile = self._pattern_matching(
            qos_profile, "^[a-zA-Z0-9_.-]+$", "qos_profile"
        )
        self.webhook = self._define_object(webhook, SessionInfoWebhook)
        self.session_id = session_id
        self.duration = duration
        self.started_at = started_at
        self.expires_at = expires_at
        self.qos_status = self._enum_matching(
            qos_status, QosStatus.list(), "qos_status"
        )
        self.messages = self._define_list(messages, Message)
