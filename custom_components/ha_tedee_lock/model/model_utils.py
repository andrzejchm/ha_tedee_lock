from typing import Any, List, TypeVar, Type, cast, Callable

T = TypeVar("T")


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def to_class(cls: Type[T], x: Any) -> dict:
    assert isinstance(x, cls)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], json_list: Any) -> List[T]:
    assert isinstance(json_list, list)
    return [f(item) for item in json_list]
