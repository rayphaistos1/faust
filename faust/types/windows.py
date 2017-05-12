import abc
from typing import Optional, List, NamedTuple
from ..utils.times import Seconds


class WindowRange(NamedTuple):
    start: float = None
    end: float = None


class WindowT(metaclass=abc.ABCMeta):
    expires: float = None

    @abc.abstractmethod
    def windows(self, timestamp: float) -> List[WindowRange]:
        ...

    @abc.abstractmethod
    def stale_before(self) -> Optional[float]:
        ...

    @abc.abstractmethod
    def current(self, timestamp: float) -> WindowRange:
        ...

    @abc.abstractmethod
    def delta(self, timestamp: float, d: Seconds) -> WindowRange:
        ...
