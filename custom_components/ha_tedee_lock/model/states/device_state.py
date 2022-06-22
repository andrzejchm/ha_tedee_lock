from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Tuple

from ..device_type import DeviceType


@dataclass
class DeviceState(ABC):
    @property
    @abstractmethod
    def device_type(self) -> DeviceType:
        pass

    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    def data_key(self) -> Tuple[str, int]:
        return self.device_type.value, self.id
