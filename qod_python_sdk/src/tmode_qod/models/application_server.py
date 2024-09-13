from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"ipv4_address": "ipv4Address", "ipv6_address": "ipv6Address"})
class ApplicationServer(BaseModel):
    """A server hosting backend applications to deliver some business logic to clients.

    The developer can choose to provide the below specified device identifiers:

    * `ipv4Address`
    * `ipv6Address`


    :param ipv4_address: IPv4 address may be specified in form <address/mask> as:   - address - an IPv4 number in dotted-quad form 1.2.3.4. Only this exact IP number will match the flow control rule.   - address/mask - an IP number as above with a mask width of the form 1.2.3.4/24.     In this case, all IP numbers from 1.2.3.0 to 1.2.3.255 will match. The bit width MUST be valid for the IP version. , defaults to None
    :type ipv4_address: str, optional
    :param ipv6_address: IPv6 address may be specified in form <address/mask> as:   - address - The /128 subnet is optional for single addresses:     - 2001:db8:85a3:8d3:1319:8a2e:370:7344     - 2001:db8:85a3:8d3:1319:8a2e:370:7344/128   - address/mask - an IP v6 number with a mask:     - 2001:db8:85a3:8d3::0/64     - 2001:db8:85a3:8d3::/64 , defaults to None
    :type ipv6_address: str, optional
    """

    def __init__(self, ipv4_address: str = None, ipv6_address: str = None):
        """A server hosting backend applications to deliver some business logic to clients.

        The developer can choose to provide the below specified device identifiers:

        * `ipv4Address`
        * `ipv6Address`


        :param ipv4_address: IPv4 address may be specified in form <address/mask> as:   - address - an IPv4 number in dotted-quad form 1.2.3.4. Only this exact IP number will match the flow control rule.   - address/mask - an IP number as above with a mask width of the form 1.2.3.4/24.     In this case, all IP numbers from 1.2.3.0 to 1.2.3.255 will match. The bit width MUST be valid for the IP version. , defaults to None
        :type ipv4_address: str, optional
        :param ipv6_address: IPv6 address may be specified in form <address/mask> as:   - address - The /128 subnet is optional for single addresses:     - 2001:db8:85a3:8d3:1319:8a2e:370:7344     - 2001:db8:85a3:8d3:1319:8a2e:370:7344/128   - address/mask - an IP v6 number with a mask:     - 2001:db8:85a3:8d3::0/64     - 2001:db8:85a3:8d3::/64 , defaults to None
        :type ipv6_address: str, optional
        """
        self.ipv4_address = ipv4_address
        self.ipv6_address = ipv6_address
