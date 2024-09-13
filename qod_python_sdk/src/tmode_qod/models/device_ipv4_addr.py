from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "public_address": "publicAddress",
        "private_address": "privateAddress",
        "public_port": "publicPort",
    }
)
class DeviceIpv4Addr(BaseModel):
    """The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers).

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object)

    In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone.


    :param public_address: A single IPv4 address with no subnet mask, defaults to None
    :type public_address: str, optional
    :param private_address: A single IPv4 address with no subnet mask, defaults to None
    :type private_address: str, optional
    :param public_port: TCP or UDP port number, defaults to None
    :type public_port: int, optional
    """

    def __init__(
        self,
        public_address: str = None,
        private_address: str = None,
        public_port: int = None,
    ):
        """The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers).

        If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress.

        If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object)

        In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone.


        :param public_address: A single IPv4 address with no subnet mask, defaults to None
        :type public_address: str, optional
        :param private_address: A single IPv4 address with no subnet mask, defaults to None
        :type private_address: str, optional
        :param public_port: TCP or UDP port number, defaults to None
        :type public_port: int, optional
        """
        self.public_address = public_address
        self.private_address = private_address
        self.public_port = public_port
