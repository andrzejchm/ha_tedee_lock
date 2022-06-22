from dataclasses import dataclass
from typing import Any
from typing import Optional
from uuid import UUID

from ..device_type import DeviceType
from ..model_utils import from_bool
from ..model_utils import from_int
from ..model_utils import from_none
from ..model_utils import from_str
from ..model_utils import from_union
from .device import Device


@dataclass
class Bridge(Device):
    @property
    def device_type(self) -> DeviceType:
        return DeviceType.BRIDGE

    @property
    def list_name(self) -> str:
        return f'Bridge: "{self.name}" (SN: {self.serial_number})'

    organization_id: None
    share_details: None
    was_configured: Optional[bool] = None
    beacon_major: Optional[int] = None
    beacon_minor: Optional[int] = None
    is_updating: Optional[bool] = None
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
    is_connected: Optional[bool] = None
    access_level: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Bridge':
        assert isinstance(obj, dict)
        organization_id = from_none(obj.get("organizationId"))
        share_details = from_none(obj.get("shareDetails"))
        was_configured = from_union([from_bool, from_none], obj.get("wasConfigured"))
        beacon_major = from_union([from_int, from_none], obj.get("beaconMajor"))
        beacon_minor = from_union([from_int, from_none], obj.get("beaconMinor"))
        is_updating = from_union([from_bool, from_none], obj.get("isUpdating"))
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
        is_connected = from_union([from_bool, from_none], obj.get("isConnected"))
        access_level = from_union([from_int, from_none], obj.get("accessLevel"))
        return Bridge(
            organization_id, share_details, was_configured, beacon_major, beacon_minor, is_updating, _id, serial_number,
            mac_address, name, user_identity, _type, created, revision, device_revision, target_device_revision,
            time_zone, is_connected, access_level,
        )

    def to_dict(self) -> dict:
        return {
            "organizationId": from_none(self.organization_id),
            "shareDetails": from_none(self.share_details),
            "wasConfigured": from_union([from_bool, from_none], self.was_configured),
            "beaconMajor": from_union([from_int, from_none], self.beacon_major),
            "beaconMinor": from_union([from_int, from_none], self.beacon_minor),
            "isUpdating": from_union([from_bool, from_none], self.is_updating),
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
            "isConnected": from_union([from_bool, from_none], self.is_connected),
            "accessLevel": from_union([from_int, from_none], self.access_level),
        }

    def to_state(self):
        pass
