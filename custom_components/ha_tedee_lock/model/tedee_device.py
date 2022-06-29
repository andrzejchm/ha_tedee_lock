"""Tedee devices model"""
import abc
from abc import ABC
from dataclasses import dataclass
from enum import Enum


class TedeeDeviceType(Enum):
    LOCK = "Lock"
    BRIDGE = "Bridge"
    pass


@dataclass
class TedeeDevice(ABC):
    """data class storing info regarding tedee device"""

    id: int

    device_type: TedeeDeviceType

    @abc.abstractmethod
    def list_name(self) -> str:
        pass

    @abc.abstractmethod
    def name(self) -> str:
        pass


class TedeeBridge(TedeeDevice):
    """data class storing info regarding tedee bridge"""
    pass  # TODO implement this


class TedeeKeypad(TedeeDevice):
    """data class storing info regarding tedee keypad"""
    pass  # TODO implement this
