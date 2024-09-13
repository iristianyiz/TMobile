from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .device import Device
from .application_server import ApplicationServer
from .ports_spec import PortsSpec


@JsonMap(
    {
        "notification_url": "notificationUrl",
        "notification_auth_token": "notificationAuthToken",
    }
)
class CreateSessionWebhook(BaseModel):
    """CreateSessionWebhook

    :param notification_url: Allows asynchronous delivery of session related events, defaults to None
    :type notification_url: str, optional
    :param notification_auth_token: Authentication token for callback API, defaults to None
    :type notification_auth_token: str, optional
    """

    def __init__(
        self, notification_url: str = None, notification_auth_token: str = None
    ):
        """CreateSessionWebhook

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
    }
)
class CreateSession(BaseModel):
    """CreateSession

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
    :type webhook: CreateSessionWebhook, optional
    :param duration: Session duration in seconds. Minimum value is 60 seconds and Maximal value of 24 hours is used if not set. , defaults to None
    :type duration: int, optional
    """

    def __init__(
        self,
        device: Device,
        qos_profile: str,
        application_server: ApplicationServer = None,
        device_ports: PortsSpec = None,
        application_server_ports: PortsSpec = None,
        webhook: CreateSessionWebhook = None,
        duration: int = None,
    ):
        """CreateSession

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
        :type webhook: CreateSessionWebhook, optional
        :param duration: Session duration in seconds. Minimum value is 60 seconds and Maximal value of 24 hours is used if not set. , defaults to None
        :type duration: int, optional
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
        self.webhook = self._define_object(webhook, CreateSessionWebhook)
        self.duration = duration
