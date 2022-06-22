from dataclasses import dataclass
from typing import Any
from typing import List

from ..model_utils import from_list
from ..states.device_state_lock import DeviceStateLock
from .response_metadata import ResponseMetadata


@dataclass
class MyLockSyncResponse:
    result: List[DeviceStateLock]
    metadata: ResponseMetadata

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'MyLockSyncResponse':
        assert isinstance(obj, dict)
        return MyLockSyncResponse(
            result=from_list(DeviceStateLock.from_dict, obj.get("result")),
            metadata=ResponseMetadata.from_dict(obj),
        )
