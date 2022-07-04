"""Tedee devices model"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Tuple

from ..device_type import DeviceType


@dataclass
class Device(ABC):
    """data class storing info regarding tedee device"""

    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def device_type(self) -> DeviceType:
        pass

    @property
    @abstractmethod
    def list_name(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def data_key(self) -> Tuple[str, int]:
        return self.device_type.value, self.id

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        pass
