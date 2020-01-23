
from dataclasses import dataclass
import betterproto


@dataclass
class Any(betterproto.Message):
    type_url: str = betterproto.string_field(1)
    value: bytes = betterproto.bytes_field(2)
    
    
@dataclass
class Struct(betterproto.Message):
    fields: betterproto.Dict[str, "Value"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass
class Value(betterproto.Message):
    null_value: "NullValue" = betterproto.enum_field(1, group="kind")
    number_value: float = betterproto.double_field(2, group="kind")
    string_value: str = betterproto.string_field(3, group="kind")
    bool_value: bool = betterproto.bool_field(4, group="kind")
    struct_value: "Struct" = betterproto.message_field(5, group="kind")
    list_value: "ListValue" = betterproto.message_field(6, group="kind")


@dataclass
class ListValue(betterproto.Message):
    values: betterproto.List["Value"] = betterproto.message_field(1)
    

@dataclass
class Empty(betterproto.Message):
    pass


class NullValue(betterproto.Enum):
    NULL_VALUE = 0
