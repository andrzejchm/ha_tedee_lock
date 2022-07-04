from dataclasses import dataclass
from typing import Optional, Any

from .model_utils import from_union, from_str, from_none


@dataclass
class OperationResult:
    operation_id: Optional[str] = None
    last_state_changed_date: Optional[str] = None

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> 'OperationResult':
        assert isinstance(obj, dict)
        operation_id = from_union([from_str, from_none], obj.get("operationId"))
        last_state_changed_date = from_union([from_str, from_none], obj.get("lastStateChangedDate"))
        return OperationResult(operation_id, last_state_changed_date)

    def to_dict(self) -> dict:
        return {
            "operationId": from_union([from_str, from_none], self.operation_id),
            "lastStateChangedDate": from_union([from_str, from_none], self.last_state_changed_date),
        }
