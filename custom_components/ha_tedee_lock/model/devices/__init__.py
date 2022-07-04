from .lock import Lock
from ..device_type import DeviceType


def device_from_dict(
        device_info: dict,
        device_type: DeviceType,
) -> 'Device':
    if device_type == DeviceType.LOCK:
        return Lock.from_dict(device_info)
    else:
        raise f"Could not parse device_info, unknown type: {device_type}"
