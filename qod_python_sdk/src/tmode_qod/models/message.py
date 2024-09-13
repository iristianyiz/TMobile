from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class Severity(Enum):
    """An enumeration representing different categories.

    :cvar INFO: "INFO"
    :vartype INFO: str
    :cvar WARNING: "WARNING"
    :vartype WARNING: str
    """

    INFO = "INFO"
    WARNING = "WARNING"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Severity._member_map_.values()))


@JsonMap({})
class Message(BaseModel):
    """Message

    :param severity: Message severity
    :type severity: Severity
    :param description: Detailed message text
    :type description: str
    """

    def __init__(self, severity: Severity, description: str):
        """Message

        :param severity: Message severity
        :type severity: Severity
        :param description: Detailed message text
        :type description: str
        """
        self.severity = self._enum_matching(severity, Severity.list(), "severity")
        self.description = description
