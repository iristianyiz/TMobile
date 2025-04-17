# ApplicationServer

A server hosting backend applications to deliver some business logic to clients. The developer can choose to provide the below specified device identifiers: 
_ `ipv4Address` _ `ipv6Address`

**Properties**                                                                                                                                                                   Name        | Type | Required | Description
ipv4_address | str | ❌ | The IPv4 address may be specified in the form <address/mask>, as:  - address: an IPv4 number in dotted-quad form, e.g., 1.2.3.4. Only this exact IP number will match the flow control rule.  - address/mask: an IP number with a mask, e.g., 1.2.3.4/24. In this case, all IP numbers from 1.2.3.0 to 1.2.3.255 will match. The bit width must be valid for the IP version.

ipv6_address | str | ❌ | The IPv6 address may be specified in the form <address/mask>, as:  - address: The /128 subnet is optional for single addresses. For example:  2001:db8:85a3:8d3:1319:8a2e:370:7344 or 2001:db8:85a3:8d3:1319:8a2e:370:7344/128  - address/mask: an IPv6 address with a mask, e.g., 2001:db8:85a3:8d3::0/64 or 2001:db8:85a3:8d3::/64.