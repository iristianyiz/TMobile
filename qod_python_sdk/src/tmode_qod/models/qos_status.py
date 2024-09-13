from enum import Enum


class QosStatus(Enum):
    """An enumeration representing different categories.

    :cvar AVAILABLE: "AVAILABLE"
    :vartype AVAILABLE: str
    """

    AVAILABLE = "AVAILABLE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, QosStatus._member_map_.values()))
