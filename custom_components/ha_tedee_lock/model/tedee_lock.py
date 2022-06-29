# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = tedee_my_locks_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, Optional

from custom_components.ha_tedee_lock.model.python_utils import from_int, from_bool, from_str, from_list, from_union, \
    from_none
from custom_components.ha_tedee_lock.model.tedee_device import TedeeDevice, TedeeDeviceType


@dataclass
class LockProperties:
    state: int
    is_charging: bool
    battery_level: int
    state_change_result: Optional[int]
    last_state_changed_date: str

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'LockProperties':
        assert isinstance(obj, dict)
        state = from_int(obj.get("state"))
        is_charging = from_bool(obj.get("isCharging"))
        battery_level = from_int(obj.get("batteryLevel"))
        state_change_result = from_union([from_int, from_none], obj.get("stateChangeResult"))
        last_state_changed_date = from_str(obj.get("lastStateChangedDate"))
        return LockProperties(state, is_charging, battery_level, state_change_result, last_state_changed_date)


@dataclass
class TedeeLock(TedeeDevice):
    connected_to_id: int = 0
    connected_to_keypad_id: int = 0
    lock_properties: LockProperties = None
    serial_number: str = ''
    name: str = ''
    type: int = 0
    created: str = ''
    revision: int = 0
    device_revision: int = 0
    target_device_revision: int = 0
    time_zone: str = ''
    is_connected: bool = False
    access_level: int = 0

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'TedeeLock':
        assert isinstance(obj, dict)
        connected_to_id = from_int(obj.get("connectedToId"))
        connected_to_keypad_id = from_int(obj.get("connectedToKeypadId"))
        lock_properties = LockProperties.from_dict(obj.get("lockProperties"))
        id = from_int(obj.get("id"))
        serial_number = from_str(obj.get("serialNumber"))
        name = from_str(obj.get("name"))
        type = from_int(obj.get("type"))
        created = from_str(obj.get("created"))
        revision = from_int(obj.get("revision"))
        device_revision = from_int(obj.get("deviceRevision"))
        target_device_revision = from_int(obj.get("targetDeviceRevision"))
        time_zone = from_str(obj.get("timeZone"))
        is_connected = from_bool(obj.get("isConnected"))
        access_level = from_int(obj.get("accessLevel"))
        return TedeeLock(
            connected_to_id=connected_to_id,
            connected_to_keypad_id=connected_to_keypad_id,
            lock_properties=lock_properties,
            id=id,
            serial_number=serial_number,
            name=name,
            type=type,
            created=created,
            revision=revision,
            device_revision=device_revision,
            target_device_revision=target_device_revision,
            time_zone=time_zone,
            is_connected=is_connected,
            access_level=access_level,
            device_type=TedeeDeviceType.LOCK,
        )

    def list_name(self) -> str:
        return f'Lock: "{self.name}" (SN: {self.serial_number})'


@dataclass
class TedeeMyLocksResponse:
    result: List[TedeeLock]
    success: bool
    error_messages: List[Any]
    status_code: int

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'TedeeMyLocksResponse':
        assert isinstance(obj, dict)
        result = from_list(TedeeLock.from_dict, obj.get("result"))
        success = from_bool(obj.get("success"))
        error_messages = from_list(lambda x: x, obj.get("errorMessages"))
        status_code = from_int(obj.get("statusCode"))
        return TedeeMyLocksResponse(
            result=result,
            success=success,
            error_messages=error_messages,
            status_code=status_code,
        )
