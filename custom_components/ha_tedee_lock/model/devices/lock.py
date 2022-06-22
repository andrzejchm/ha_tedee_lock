from dataclasses import dataclass
from enum import Enum
from typing import Optional

from ...model.model_utils import from_bool
from ...model.model_utils import from_int
from ...model.model_utils import from_none
from ...model.model_utils import from_str
from ...model.model_utils import from_union
from ...model.model_utils import to_class
from .device import Device
from .device import DeviceType


class LockState(Enum):
    Uncalibrated = 0
    Calibrating = 1
    Unlocked = 2
    SemiLocked = 3
    Unlocking = 4
    Locking = 5
    Locked = 6
    Pulled = 7
    Pulling = 8
    Unknown = 9
    Updating = 10


@dataclass
class LockProperties:
    state: LockState = None
    is_charging: Optional[bool] = None
    battery_level: Optional[int] = None
    state_change_result: Optional[int] = None
    last_state_changed_date: Optional[str] = None

    @staticmethod
    def from_dict(obj: dict) -> 'LockProperties':
        state = LockState(from_union([from_int, from_none], obj.get("state")) or LockState.Unknown.value)
        is_charging = from_union([from_bool, from_none], obj.get("isCharging"))
        battery_level = from_union([from_int, from_none], obj.get("batteryLevel"))
        state_change_result = from_union([from_int, from_none], obj.get("stateChangeResult"))
        last_state_changed_date = from_union([from_str, from_none], obj.get("lastStateChangedDate"))
        return LockProperties(state, is_charging, battery_level, state_change_result, last_state_changed_date)

    def to_dict(self) -> dict:
        result: dict = {
            "state": from_union([from_int, from_none], self.state.value),
            "isCharging": from_union([from_bool, from_none], self.is_charging),
            "batteryLevel": from_union([from_int, from_none], self.battery_level),
            "stateChangeResult": from_union([from_int, from_none], self.state_change_result),
            "lastStateChangedDate": from_union([from_str, from_none], self.last_state_changed_date),
        }
        return result


@dataclass
class Lock(Device):

    @property
    def device_type(self) -> DeviceType:
        return DeviceType.LOCK

    @property
    def list_name(self) -> str:
        return f'Lock: "{self.name}" (SN: {self.serial_number})'

    connected_to_id: Optional[int] = None
    connected_to_keypad_id: Optional[int] = None
    lock_properties: Optional[LockProperties] = None
    id: Optional[int] = None
    serial_number: Optional[str] = None
    name: Optional[str] = None
    type: Optional[int] = None
    created: Optional[str] = None
    revision: Optional[int] = None
    device_revision: Optional[int] = None
    target_device_revision: Optional[int] = None
    time_zone: Optional[str] = None
    is_connected: Optional[bool] = None
    access_level: Optional[int] = None

    @staticmethod
    def from_dict(obj: dict) -> 'Lock':
        connected_to_id = from_union([from_int, from_none], obj.get("connectedToId"))
        connected_to_keypad_id = from_union([from_int, from_none], obj.get("connectedToKeypadId"))
        lock_properties = from_union([LockProperties.from_dict, from_none], obj.get("lockProperties"))
        _id = from_union([from_int, from_none], obj.get("id"))
        serial_number = from_union([from_str, from_none], obj.get("serialNumber"))
        name = from_union([from_str, from_none], obj.get("name"))
        _type = from_union([from_int, from_none], obj.get("type"))
        created = from_union([from_str, from_none], obj.get("created"))
        revision = from_union([from_int, from_none], obj.get("revision"))
        device_revision = from_union([from_int, from_none], obj.get("deviceRevision"))
        target_device_revision = from_union([from_int, from_none], obj.get("targetDeviceRevision"))
        time_zone = from_union([from_str, from_none], obj.get("timeZone"))
        is_connected = from_union([from_bool, from_none], obj.get("isConnected"))
        access_level = from_union([from_int, from_none], obj.get("accessLevel"))
        return Lock(connected_to_id, connected_to_keypad_id, lock_properties, _id, serial_number, name, _type,
                    created, revision, device_revision, target_device_revision, time_zone, is_connected,
                    access_level, )

    def to_dict(self) -> dict:
        result: dict = {
            "connectedToId": from_union([from_int, from_none], self.connected_to_id),
            "connectedToKeypadId": from_union([from_int, from_none], self.connected_to_keypad_id),
            "lockProperties": from_union([lambda x: to_class(LockProperties, x), from_none],
                                         self.lock_properties),
            "id": from_union([from_int, from_none], self.id),
            "serialNumber": from_union([from_str, from_none], self.serial_number),
            "name": from_union([from_str, from_none], self.name),
            "type": from_union([from_int, from_none], self.type),
            "created": from_union([from_str, from_none], self.created),
            "revision": from_union([from_int, from_none], self.revision),
            "deviceRevision": from_union([from_int, from_none], self.device_revision),
            "targetDeviceRevision": from_union([from_int, from_none], self.target_device_revision),
            "timeZone": from_union([from_str, from_none], self.time_zone),
            "isConnected": from_union([from_bool, from_none], self.is_connected),
            "accessLevel": from_union([from_int, from_none], self.access_level),
        }
        return result
