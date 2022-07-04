from dataclasses import dataclass
from typing import Optional, List, TypeVar, Any, Generic

from ..model_utils import from_union, from_list, from_bool, from_none, from_int

T = TypeVar("T")


@dataclass
class ResponseMetadata(Generic[T]):
    success: Optional[bool] = None
    error_messages: Optional[List[Any]] = None
    status_code: Optional[int] = None

    @staticmethod
    def from_dict(
            obj: dict[str, Any],
    ):
        return ResponseMetadata(
            success=from_union([from_bool, from_none], obj.get("success")),
            error_messages=from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("errorMessages")),
            status_code=from_union([from_int, from_none], obj.get("statusCode")),
        )

    def to_dict(self) -> dict:
        return {
            "success": from_union([from_bool, from_none], self.success),
            "errorMessages": from_union([lambda x: from_list(lambda y: y, x), from_none], self.error_messages),
            "statusCode": from_union([from_int, from_none], self.status_code),
        }
