import collections.abc as t

from envoy_data_plane.google.protobuf import ListValue, Struct, Value


AcceptedTypes = (
    str
    | int
    | bool
    | t.Sequence["AcceptedTypes"]
    | t.MutableMapping[str, "AcceptedTypes"]
    | None
)


def dict_to_struct(d: dict[str, AcceptedTypes]) -> Struct:
    return Struct(fields={k: to_value(v) for k, v in d.items()})


def to_value(o: AcceptedTypes) -> Value:
    if isinstance(o, bool):
        return Value(bool_value=o)
    elif isinstance(o, str):
        return Value(string_value=o)
    elif isinstance(o, int):
        return Value(number_value=o)
    elif isinstance(o, type(None)):
        return Value(null_value=None)
    elif isinstance(o, t.Sequence):
        return Value(list_value=ListValue(values=[to_value(v) for v in o]))
    else:
        return Value(struct_value=Struct(fields={k: to_value(v) for k, v in o.items()}))
