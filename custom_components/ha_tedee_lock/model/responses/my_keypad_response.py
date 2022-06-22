from dataclasses import dataclass
from typing import Any
from typing import List
from typing import Optional

from ..devices.keypad import Keypad
from ..model_utils import from_list
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
