from dataclasses import dataclass
from typing import Optional, Any

from .response_metadata import ResponseMetadata
from ..model_utils import from_union, from_none, from_bool, from_list, from_int, to_class
from ..operation_result import OperationResult


@dataclass
class OperationResponse:
    result: Optional[OperationResult]
    metadata: ResponseMetadata

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'OperationResponse':
        assert isinstance(obj, dict)
        result = from_union([OperationResult.from_dict, from_none], obj.get("result"))
        metadata = ResponseMetadata.from_dict(obj)
        return OperationResponse(
            result,
            metadata,
        )

    def to_dict(self) -> dict:
        return {
            "result": from_union([lambda x: to_class(OperationResult, x), from_none], self.result),
            "success": from_union([from_bool, from_none], self.metadata.success),
            "errorMessages": from_union([lambda x: from_list(lambda y: y, x), from_none],
                                        self.metadata.error_messages),
            "statusCode": from_union([from_int, from_none], self.metadata.status_code),
        }
