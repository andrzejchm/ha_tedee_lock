from dataclasses import dataclass
from typing import Optional, Any

from ..device_type import DeviceType
from ..states.device_state import DeviceState
from ..model_utils import from_none, from_union, from_int, from_bool, to_class
from ..devices.lock import LockProperties


@dataclass
class DeviceStateLock(DeviceState):

    @property
    def device_type(self) -> DeviceType:
        return DeviceType.LOCK

    id: Optional[int] = None
    is_connected: Optional[bool] = None
    lock_properties: Optional[LockProperties] = None

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'DeviceStateLock':
        assert isinstance(obj, dict)
        _id = from_union([from_int, from_none], obj.get("id"))
        is_connected = from_union([from_bool, from_none], obj.get("isConnected"))
        lock_properties = from_union([LockProperties.from_dict, from_none], obj.get("lockProperties"))
        return DeviceStateLock(
            _id,
            is_connected,
            lock_properties,
        )

    def to_dict(self) -> dict:
        result: dict = {
            "id": from_union([from_int, from_none], self.id),
            "isConnected": from_union([from_bool, from_none], self.is_connected),
            "lockProperties": from_union([lambda x: to_class(LockProperties, x), from_none], self.lock_properties),
        }
        return result
