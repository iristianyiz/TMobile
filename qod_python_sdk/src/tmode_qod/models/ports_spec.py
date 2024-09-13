from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"from_": "from"})
class Ranges(BaseModel):
    """Ranges

    :param from_: TCP or UDP port number
    :type from_: int
    :param to: TCP or UDP port number
    :type to: int
    """

    def __init__(self, from_: int, to: int):
        """Ranges

        :param from_: TCP or UDP port number
        :type from_: int
        :param to: TCP or UDP port number
        :type to: int
        """
        self.from_ = from_
        self.to = to


@JsonMap({})
class PortsSpec(BaseModel):
    """PortsSpec

    :param ranges: ranges, defaults to None
    :type ranges: List[Ranges], optional
    :param ports: ports, defaults to None
    :type ports: List[int], optional
    """

    def __init__(self, ranges: List[Ranges] = None, ports: List[int] = None):
        """PortsSpec

        :param ranges: ranges, defaults to None
        :type ranges: List[Ranges], optional
        :param ports: ports, defaults to None
        :type ports: List[int], optional
        """
        self.ranges = self._define_list(ranges, Ranges)
        self.ports = ports
