# ApplicationServer

A server hosting backend applications to deliver some business logic to clients. The developer can choose to provide the below specified device identifiers: _ `ipv4Address` _ `ipv6Address`

**Properties**

| Name         | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                      |
| :----------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ipv4_address | str  | ❌       | IPv4 address may be specified in form <address/mask> as: - address - an IPv4 number in dotted-quad form 1.2.3.4. Only this exact IP number will match the flow control rule. - address/mask - an IP number as above with a mask width of the form 1.2.3.4/24. In this case, all IP numbers from 1.2.3.0 to 1.2.3.255 will match. The bit width MUST be valid for the IP version. |
| ipv6_address | str  | ❌       | IPv6 address may be specified in form <address/mask> as: - address - The /128 subnet is optional for single addresses: - 2001:db8:85a3:8d3:1319:8a2e:370:7344 - 2001:db8:85a3:8d3:1319:8a2e:370:7344/128 - address/mask - an IP v6 number with a mask: - 2001:db8:85a3:8d3::0/64 - 2001:db8:85a3:8d3::/64                                                                        |
