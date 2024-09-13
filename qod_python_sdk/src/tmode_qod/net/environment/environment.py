"""
An enum class containing all the possible environments for the SDK
"""

from enum import Enum


class Environment(Enum):
    """The environments available for the SDK"""

    DEFAULT = "https://naas.t-mobile.com/qod/v0"
    PRODUCTION = "https://naas.t-mobile.com/qod/v0"
    SANDBOX = "https://naas-sandbox.t-mobile.com/qod/v0"
