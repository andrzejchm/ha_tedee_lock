from dataclasses import dataclass
from typing import Optional, Any, List
from uuid import UUID

from .device import Device
from ..model_utils import from_none, from_union, from_bool, from_int, from_str, from_list, to_class
from ... import DeviceType


@dataclass
class DeviceSettings:
    battery_type: Optional[int] = None
    sound_level: Optional[int] = None
    backlight_level: Optional[int] = None
    bell_button_enabled: Optional[bool] = None
    lock_by_button_enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceSettings':
        assert isinstance(obj, dict)
        battery_type = from_union([from_int, from_none], obj.get("batteryType"))
        sound_level = from_union([from_int, from_none], obj.get("soundLevel"))
        backlight_level = from_union([from_int, from_none], obj.get("backlightLevel"))
        bell_button_enabled = from_union([from_bool, from_none], obj.get("bellButtonEnabled"))
        lock_by_button_enabled = from_union([from_bool, from_none], obj.get("lockByButtonEnabled"))
        return DeviceSettings(battery_type, sound_level, backlight_level, bell_button_enabled, lock_by_button_enabled)

    def to_dict(self) -> dict:
        return {
            "batteryType": from_union([from_int, from_none], self.battery_type),
            "soundLevel": from_union([from_int, from_none], self.sound_level),
            "backlightLevel": from_union([from_int, from_none], self.backlight_level),
            "bellButtonEnabled": from_union([from_bool, from_none], self.bell_button_enabled),
            "lockByButtonEnabled": from_union([from_bool, from_none], self.lock_by_button_enabled)
        }


@dataclass
class Keypad(Device):
    @property
    def device_type(self) -> DeviceType:
        return DeviceType.KEYPAD

    @property
    def list_name(self) -> str:
        return f'Keypad: "{self.name}" (SN: {self.serial_number})'

    organization_id: None
    is_connected: None
    share_details: None
    connected_to_id: Optional[int] = None
    connected_to_lock_id: Optional[int] = None
    device_settings: Optional[DeviceSettings] = None
    id: Optional[int] = None
    serial_number: Optional[str] = None
    mac_address: Optional[str] = None
    name: Optional[str] = None
    user_identity: Optional[UUID] = None
    type: Optional[int] = None
    created: Optional[str] = None
    revision: Optional[int] = None
    device_revision: Optional[int] = None
    target_device_revision: Optional[int] = None
    time_zone: Optional[str] = None
    access_level: Optional[int] = None
    software_versions: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Keypad':
        assert isinstance(obj, dict)
        organization_id = from_none(obj.get("organizationId"))
        is_connected = from_none(obj.get("isConnected"))
        share_details = from_none(obj.get("shareDetails"))
        connected_to_id = from_union([from_int, from_none], obj.get("connectedToId"))
        connected_to_lock_id = from_union([from_int, from_none], obj.get("connectedToLockId"))
        device_settings = from_union([DeviceSettings.from_dict, from_none], obj.get("deviceSettings"))
        _id = from_union([from_int, from_none], obj.get("id"))
        serial_number = from_union([from_str, from_none], obj.get("serialNumber"))
        mac_address = from_union([from_str, from_none], obj.get("macAddress"))
        name = from_union([from_str, from_none], obj.get("name"))
        user_identity = from_union([lambda x: UUID(x), from_none], obj.get("userIdentity"))
        _type = from_union([from_int, from_none], obj.get("type"))
        created = from_union([from_str, from_none], obj.get("created"))
        revision = from_union([from_int, from_none], obj.get("revision"))
        device_revision = from_union([from_int, from_none], obj.get("deviceRevision"))
        target_device_revision = from_union([from_int, from_none], obj.get("targetDeviceRevision"))
        time_zone = from_union([from_str, from_none], obj.get("timeZone"))
        access_level = from_union([from_int, from_none], obj.get("accessLevel"))
        software_versions = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("softwareVersions"))
        return Keypad(organization_id, is_connected, share_details, connected_to_id, connected_to_lock_id,
                      device_settings, _id, serial_number, mac_address, name, user_identity, _type, created, revision,
                      device_revision, target_device_revision, time_zone, access_level, software_versions)

    def to_dict(self) -> dict:
        return {
            "organizationId": from_none(self.organization_id), "isConnected": from_none(self.is_connected),
            "shareDetails": from_none(self.share_details),
            "connectedToId": from_union([from_int, from_none], self.connected_to_id),
            "connectedToLockId": from_union([from_int, from_none], self.connected_to_lock_id),
            "deviceSettings": from_union([lambda x: to_class(DeviceSettings, x), from_none],
                                         self.device_settings),
            "id": from_union([from_int, from_none], self.id),
            "serialNumber": from_union([from_str, from_none], self.serial_number),
            "macAddress": from_union([from_str, from_none], self.mac_address),
            "name": from_union([from_str, from_none], self.name),
            "userIdentity": from_union([lambda x: str(x), from_none], self.user_identity),
            "type": from_union([from_int, from_none], self.type),
            "created": from_union([from_str, from_none], self.created),
            "revision": from_union([from_int, from_none], self.revision),
            "deviceRevision": from_union([from_int, from_none], self.device_revision),
            "targetDeviceRevision": from_union([from_int, from_none], self.target_device_revision),
            "timeZone": from_union([from_str, from_none], self.time_zone),
            "accessLevel": from_union([from_int, from_none], self.access_level),
            "softwareVersions": from_union([lambda x: from_list(lambda y: y, x), from_none],
                                           self.software_versions),
        }
