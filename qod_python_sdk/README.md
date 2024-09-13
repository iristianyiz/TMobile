# TmodeQod Python SDK 1.0.0

Welcome to the TmodeQod SDK documentation. This guide will help you get started with integrating and using the TmodeQod SDK in your project.

## Versions

- API version: `0.10.1`
- SDK version: `1.0.0`

## About the API

The Quality-On-Demand (QoD) API provides programmable interface for developers and other users (capabilities consumers) to request stable latency or throughput managed by Telco networks without the necessity to have an in-depth knowledge of the 4G/5G system or the overall complexity of the Telecom Systems.

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Environments](#environments)
  - [Setting an Environment](#setting-an-environment)
- [Setting a custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install tmode-qod
```

## Environments

The SDK supports different environments for various stages of development and deployment.

Here are the available environments:

```py
production = "https://naas.t-mobile.com/qod/v0"
sandbox = "https://naas-sandbox.t-mobile.com/qod/v0"
```

## Setting an Environment

To configure the SDK to use a specific environment, you can set the base URL as follows:

```py
from tmode_qod import Environment

sdk.set_base_url(Environment.production.value)
```

## Setting a custom Timeout

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from tmode_qod import TmodeQod

sdk = TmodeQod(timeout=10000)
```

# Sample Usage

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
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

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                       |
| :--------------------------------------------------------- |
| [SessionService](documentation/services/SessionService.md) |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CreateSession](documentation/models/CreateSession.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [SessionInfo](documentation/models/SessionInfo.md)                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Device](documentation/models/Device.md)                             | End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators. The developer can choose to provide the below specified device identifiers: _ `ipv4Address` _ `ipv6Address` _ `phoneNumber` _ `networkAccessIdentifier` NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device                                                                                                                                                                                                                                                                                                                                                                                      |
| [ApplicationServer](documentation/models/ApplicationServer.md)       | A server hosting backend applications to deliver some business logic to clients. The developer can choose to provide the below specified device identifiers: _ `ipv4Address` _ `ipv6Address`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [PortsSpec](documentation/models/PortsSpec.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [CreateSessionWebhook](documentation/models/CreateSessionWebhook.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [DeviceIpv4Addr](documentation/models/DeviceIpv4Addr.md)             | The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers). If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then the same address should be specified for both publicAddress and privateAddress. If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object) In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone. |
| [Ranges](documentation/models/Ranges.md)                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [SessionInfoWebhook](documentation/models/SessionInfoWebhook.md)     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [QosStatus](documentation/models/QosStatus.md)                       | The current status of the requested QoS session. The status can be one of the following: \* `AVAILABLE` - The requested QoS has been provided by the network                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Message](documentation/models/Message.md)                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Severity](documentation/models/Severity.md)                         | Message severity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

</details>
