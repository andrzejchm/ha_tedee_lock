from dataclasses import dataclass
from typing import Any
from typing import List
from typing import Optional

from ..devices.lock import Lock
from ..model_utils import from_list
from .response_metadata import ResponseMetadata


@dataclass
class MyLockResponse:
    result: Optional[List[Lock]]
    metadata: ResponseMetadata

    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> 'MyLockResponse':
        return MyLockResponse(
            metadata=ResponseMetadata.from_dict(dictionary),
            result=from_list(Lock.from_dict, dictionary.get("result")),
        )
