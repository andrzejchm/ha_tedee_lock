from dataclasses import dataclass
from typing import Optional, List, Any

from ..model_utils import from_list
from ..devices.keypad import Keypad
from .response_metadata import ResponseMetadata


@dataclass
class MyKeypadResponse:
    result: Optional[List[Keypad]]
    metadata: ResponseMetadata

    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> 'MyKeypadResponse':
        return MyKeypadResponse(
            metadata=ResponseMetadata.from_dict(dictionary),
            result=from_list(Keypad.from_dict, dictionary.get("result")),
        )
