from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .device_ipv4_addr import DeviceIpv4Addr


@JsonMap(
    {
        "phone_number": "phoneNumber",
        "network_access_identifier": "networkAccessIdentifier",
        "ipv4_address": "ipv4Address",
        "ipv6_address": "ipv6Address",
    }
)
class Device(BaseModel):
    """End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

    The developer can choose to provide the below specified device identifiers:

    * `ipv4Address`
    * `ipv6Address`
    * `phoneNumber`
    * `networkAccessIdentifier`

    NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device


    :param phone_number: A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, optionally prefixed with '+'.
    :type phone_number: str
    :param network_access_identifier: A public identifier addressing a subscription in a mobile network. In 3GPP terminology, it corresponds to the GPSI formatted with the External Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone number, the network access identifier is not subjected to portability ruling in force, and is individually managed by each operator., defaults to None
    :type network_access_identifier: str, optional
    :param ipv4_address: The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers). If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress. If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object) In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone. , defaults to None
    :type ipv4_address: DeviceIpv4Addr, optional
    :param ipv6_address: The device should be identified by the observed IPv6 address, or by any single IPv6 address from within the subnet allocated to the device (e.g. adding ::0 to the /64 prefix). The session shall apply to all IP flows between the device subnet and the specified application server, unless further restricted by the optional parameters devicePorts or applicationServerPorts. , defaults to None
    :type ipv6_address: str, optional
    """

    def __init__(
        self,
        phone_number: str,
        network_access_identifier: str = None,
        ipv4_address: DeviceIpv4Addr = None,
        ipv6_address: str = None,
    ):
        """End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

        The developer can choose to provide the below specified device identifiers:

        * `ipv4Address`
        * `ipv6Address`
        * `phoneNumber`
        * `networkAccessIdentifier`

        NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device


        :param phone_number: A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, optionally prefixed with '+'.
        :type phone_number: str
        :param network_access_identifier: A public identifier addressing a subscription in a mobile network. In 3GPP terminology, it corresponds to the GPSI formatted with the External Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone number, the network access identifier is not subjected to portability ruling in force, and is individually managed by each operator., defaults to None
        :type network_access_identifier: str, optional
        :param ipv4_address: The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers). If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress. If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object) In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone. , defaults to None
        :type ipv4_address: DeviceIpv4Addr, optional
        :param ipv6_address: The device should be identified by the observed IPv6 address, or by any single IPv6 address from within the subnet allocated to the device (e.g. adding ::0 to the /64 prefix). The session shall apply to all IP flows between the device subnet and the specified application server, unless further restricted by the optional parameters devicePorts or applicationServerPorts. , defaults to None
        :type ipv6_address: str, optional
        """
        self.phone_number = self._pattern_matching(
            phone_number, "^\+?[0-9]{5,15}$", "phone_number"
        )
        self.network_access_identifier = network_access_identifier
        self.ipv4_address = self._define_object(ipv4_address, DeviceIpv4Addr)
        self.ipv6_address = ipv6_address
