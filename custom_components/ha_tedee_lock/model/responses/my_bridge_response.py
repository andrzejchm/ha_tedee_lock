from dataclasses import dataclass
from typing import Any
from typing import List
from typing import Optional

from ..devices.bridge import Bridge
from ..model_utils import from_list
from .response_metadata import ResponseMetadata


@dataclass
class MyBridgeResponse:
    result: Optional[List[Bridge]]
    metadata: ResponseMetadata

    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> 'MyBridgeResponse':
        return MyBridgeResponse(
            metadata=ResponseMetadata.from_dict(dictionary),
            result=from_list(Bridge.from_dict, dictionary.get("result")),
        )
