# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: google/api/expr/v1alpha1/checked.proto, google/api/expr/v1alpha1/syntax.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class TypePrimitiveType(betterproto.Enum):
    PRIMITIVE_TYPE_UNSPECIFIED = 0
    BOOL = 1
    INT64 = 2
    UINT64 = 3
    DOUBLE = 4
    STRING = 5
    BYTES = 6


class TypeWellKnownType(betterproto.Enum):
    WELL_KNOWN_TYPE_UNSPECIFIED = 0
    ANY = 1
    TIMESTAMP = 2
    DURATION = 3


@dataclass(eq=False, repr=False)
class ParsedExpr(betterproto.Message):
    """
    An expression together with source information as returned by the parser.
    """

    # The parsed expression.
    expr: "Expr" = betterproto.message_field(2)
    # The source info derived from input that generated the parsed `expr`.
    source_info: "SourceInfo" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class Expr(betterproto.Message):
    """
    An abstract representation of a common expression. Expressions are
    abstractly represented as a collection of identifiers, select statements,
    function calls, literals, and comprehensions. All operators with the
    exception of the '.' operator are modelled as function calls. This makes it
    easy to represent new operators into the existing AST. All references
    within expressions must resolve to a [Decl][google.api.expr.v1alpha1.Decl]
    provided at type-check for an expression to be valid. A reference may
    either be a bare identifier `name` or a qualified identifier
    `google.api.name`. References may either refer to a value or a function
    declaration. For example, the expression
    `google.api.name.startsWith('expr')` references the declaration
    `google.api.name` within a
    [Expr.Select][google.api.expr.v1alpha1.Expr.Select] expression, and the
    function declaration `startsWith`.
    """

    # Required. An id assigned to this node by the parser which is unique in a
    # given expression tree. This is used to associate type information and other
    # attributes to a node in the parse tree.
    id: int = betterproto.int64_field(2)
    # A literal expression.
    const_expr: "Constant" = betterproto.message_field(3, group="expr_kind")
    # An identifier expression.
    ident_expr: "ExprIdent" = betterproto.message_field(4, group="expr_kind")
    # A field selection expression, e.g. `request.auth`.
    select_expr: "ExprSelect" = betterproto.message_field(5, group="expr_kind")
    # A call expression, including calls to predefined functions and operators.
    call_expr: "ExprCall" = betterproto.message_field(6, group="expr_kind")
    # A list creation expression.
    list_expr: "ExprCreateList" = betterproto.message_field(7, group="expr_kind")
    # A map or message creation expression.
    struct_expr: "ExprCreateStruct" = betterproto.message_field(8, group="expr_kind")
    # A comprehension expression.
    comprehension_expr: "ExprComprehension" = betterproto.message_field(
        9, group="expr_kind"
    )


@dataclass(eq=False, repr=False)
class ExprIdent(betterproto.Message):
    """An identifier expression. e.g. `request`."""

    # Required. Holds a single, unqualified identifier, possibly preceded by a
    # '.'. Qualified names are represented by the
    # [Expr.Select][google.api.expr.v1alpha1.Expr.Select] expression.
    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ExprSelect(betterproto.Message):
    """A field selection expression. e.g. `request.auth`."""

    # Required. The target of the selection expression. For example, in the
    # select expression `request.auth`, the `request` portion of the expression
    # is the `operand`.
    operand: "Expr" = betterproto.message_field(1)
    # Required. The name of the field to select. For example, in the select
    # expression `request.auth`, the `auth` portion of the expression would be
    # the `field`.
    field: str = betterproto.string_field(2)
    # Whether the select is to be interpreted as a field presence test. This
    # results from the macro `has(request.auth)`.
    test_only: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class ExprCall(betterproto.Message):
    """
    A call expression, including calls to predefined functions and operators.
    For example, `value == 10`, `size(map_value)`.
    """

    # The target of an method call-style expression. For example, `x` in `x.f()`.
    target: "Expr" = betterproto.message_field(1)
    # Required. The name of the function or method being called.
    function: str = betterproto.string_field(2)
    # The arguments.
    args: List["Expr"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class ExprCreateList(betterproto.Message):
    """
    A list creation expression. Lists may either be homogenous, e.g. `[1, 2,
    3]`, or heterogeneous, e.g. `dyn([1, 'hello', 2.0])`
    """

    # The elements part of the list.
    elements: List["Expr"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ExprCreateStruct(betterproto.Message):
    """
    A map or message creation expression. Maps are constructed as `{'key_name':
    'value'}`. Message construction is similar, but prefixed with a type name
    and composed of field ids: `types.MyType{field_id: 'value'}`.
    """

    # The type name of the message to be created, empty when creating map
    # literals.
    message_name: str = betterproto.string_field(1)
    # The entries in the creation expression.
    entries: List["ExprCreateStructEntry"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ExprCreateStructEntry(betterproto.Message):
    """Represents an entry."""

    # Required. An id assigned to this node by the parser which is unique in a
    # given expression tree. This is used to associate type information and other
    # attributes to the node.
    id: int = betterproto.int64_field(1)
    # The field key for a message creator statement.
    field_key: str = betterproto.string_field(2, group="key_kind")
    # The key expression for a map creation statement.
    map_key: "Expr" = betterproto.message_field(3, group="key_kind")
    # Required. The value assigned to the key.
    value: "Expr" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ExprComprehension(betterproto.Message):
    """
    A comprehension expression applied to a list or map. Comprehensions are not
    part of the core syntax, but enabled with macros. A macro matches a
    specific call signature within a parsed AST and replaces the call with an
    alternate AST block. Macro expansion happens at parse time. The following
    macros are supported within CEL: Aggregate type macros may be applied to
    all elements in a list or all keys in a map: *  `all`, `exists`,
    `exists_one` -  test a predicate expression against    the inputs and
    return `true` if the predicate is satisfied for all,    any, or only one
    value `list.all(x, x < 10)`. *  `filter` - test a predicate expression
    against the inputs and return    the subset of elements which satisfy the
    predicate:    `payments.filter(p, p > 1000)`. *  `map` - apply an
    expression to all elements in the input and return the    output aggregate
    type: `[1, 2, 3].map(i, i * i)`. The `has(m.x)` macro tests whether the
    property `x` is present in struct `m`. The semantics of this macro depend
    on the type of `m`. For proto2 messages `has(m.x)` is defined as 'defined,
    but not set`. For proto3, the macro tests whether the property is set to
    its default. For map and struct types, the macro tests whether the property
    `x` is defined on `m`.
    """

    # The name of the iteration variable.
    iter_var: str = betterproto.string_field(1)
    # The range over which var iterates.
    iter_range: "Expr" = betterproto.message_field(2)
    # The name of the variable used for accumulation of the result.
    accu_var: str = betterproto.string_field(3)
    # The initial value of the accumulator.
    accu_init: "Expr" = betterproto.message_field(4)
    # An expression which can contain iter_var and accu_var. Returns false when
    # the result has been computed and may be used as a hint to short-circuit the
    # remainder of the comprehension.
    loop_condition: "Expr" = betterproto.message_field(5)
    # An expression which can contain iter_var and accu_var. Computes the next
    # value of accu_var.
    loop_step: "Expr" = betterproto.message_field(6)
    # An expression which can contain accu_var. Computes the result.
    result: "Expr" = betterproto.message_field(7)


@dataclass(eq=False, repr=False)
class Constant(betterproto.Message):
    """
    Represents a primitive literal. Named 'Constant' here for backwards
    compatibility. This is similar as the primitives supported in the well-
    known type `google.protobuf.Value`, but richer so it can represent CEL's
    full range of primitives. Lists and structs are not included as constants
    as these aggregate types may contain [Expr][google.api.expr.v1alpha1.Expr]
    elements which require evaluation and are thus not constant. Examples of
    literals include: `"hello"`, `b'bytes'`, `1u`, `4.2`, `-2`, `true`, `null`.
    """

    # null value.
    null_value: "betterproto_lib_google_protobuf.NullValue" = betterproto.enum_field(
        1, group="constant_kind"
    )
    # boolean value.
    bool_value: bool = betterproto.bool_field(2, group="constant_kind")
    # int64 value.
    int64_value: int = betterproto.int64_field(3, group="constant_kind")
    # uint64 value.
    uint64_value: int = betterproto.uint64_field(4, group="constant_kind")
    # double value.
    double_value: float = betterproto.double_field(5, group="constant_kind")
    # string value.
    string_value: str = betterproto.string_field(6, group="constant_kind")
    # bytes value.
    bytes_value: bytes = betterproto.bytes_field(7, group="constant_kind")
    # protobuf.Duration value. Deprecated: duration is no longer considered a
    # builtin cel type.
    duration_value: timedelta = betterproto.message_field(8, group="constant_kind")
    # protobuf.Timestamp value. Deprecated: timestamp is no longer considered a
    # builtin cel type.
    timestamp_value: datetime = betterproto.message_field(9, group="constant_kind")

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.duration_value:
            warnings.warn("Constant.duration_value is deprecated", DeprecationWarning)
        if self.timestamp_value:
            warnings.warn("Constant.timestamp_value is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class SourceInfo(betterproto.Message):
    """Source information collected at parse time."""

    # The syntax version of the source, e.g. `cel1`.
    syntax_version: str = betterproto.string_field(1)
    # The location name. All position information attached to an expression is
    # relative to this location. The location could be a file, UI element, or
    # similar. For example, `acme/app/AnvilPolicy.cel`.
    location: str = betterproto.string_field(2)
    # Monotonically increasing list of code point offsets where newlines `\n`
    # appear. The line number of a given position is the index `i` where for a
    # given `id` the `line_offsets[i] < id_positions[id] < line_offsets[i+1]`.
    # The column may be derivd from `id_positions[id] - line_offsets[i]`.
    line_offsets: List[int] = betterproto.int32_field(3)
    # A map from the parse node id (e.g. `Expr.id`) to the code point offset
    # within the source.
    positions: Dict[int, int] = betterproto.map_field(
        4, betterproto.TYPE_INT64, betterproto.TYPE_INT32
    )
    # A map from the parse node id where a macro replacement was made to the call
    # `Expr` that resulted in a macro expansion. For example, `has(value.field)`
    # is a function call that is replaced by a `test_only` field selection in the
    # AST. Likewise, the call `list.exists(e, e > 10)` translates to a
    # comprehension expression. The key in the map corresponds to the expression
    # id of the expanded macro, and the value is the call `Expr` that was
    # replaced.
    macro_calls: Dict[int, "Expr"] = betterproto.map_field(
        5, betterproto.TYPE_INT64, betterproto.TYPE_MESSAGE
    )


@dataclass(eq=False, repr=False)
class SourcePosition(betterproto.Message):
    """A specific position in source."""

    # The soucre location name (e.g. file name).
    location: str = betterproto.string_field(1)
    # The UTF-8 code unit offset.
    offset: int = betterproto.int32_field(2)
    # The 1-based index of the starting line in the source text where the issue
    # occurs, or 0 if unknown.
    line: int = betterproto.int32_field(3)
    # The 0-based index of the starting position within the line of source text
    # where the issue occurs.  Only meaningful if line is nonzero.
    column: int = betterproto.int32_field(4)


@dataclass(eq=False, repr=False)
class CheckedExpr(betterproto.Message):
    """A CEL expression which has been successfully type checked."""

    # A map from expression ids to resolved references. The following entries are
    # in this table: - An Ident or Select expression is represented here if it
    # resolves to a   declaration. For instance, if `a.b.c` is represented by
    # `select(select(id(a), b), c)`, and `a.b` resolves to a declaration,   while
    # `c` is a field selection, then the reference is attached to the   nested
    # select expression (but not to the id or or the outer select).   In turn, if
    # `a` resolves to a declaration and `b.c` are field selections,   the
    # reference is attached to the ident expression. - Every Call expression has
    # an entry here, identifying the function being   called. - Every
    # CreateStruct expression for a message has an entry, identifying   the
    # message.
    reference_map: Dict[int, "Reference"] = betterproto.map_field(
        2, betterproto.TYPE_INT64, betterproto.TYPE_MESSAGE
    )
    # A map from expression ids to types. Every expression node which has a type
    # different than DYN has a mapping here. If an expression has type DYN, it is
    # omitted from this map to save space.
    type_map: Dict[int, "Type"] = betterproto.map_field(
        3, betterproto.TYPE_INT64, betterproto.TYPE_MESSAGE
    )
    # The source info derived from input that generated the parsed `expr` and any
    # optimizations made during the type-checking pass.
    source_info: "SourceInfo" = betterproto.message_field(5)
    # The expr version indicates the major / minor version number of the `expr`
    # representation. The most common reason for a version change will be to
    # indicate to the CEL runtimes that transformations have been performed on
    # the expr during static analysis. In some cases, this will save the runtime
    # the work of applying the same or similar transformations prior to
    # evaluation.
    expr_version: str = betterproto.string_field(6)
    # The checked expression. Semantically equivalent to the parsed `expr`, but
    # may have structural differences.
    expr: "Expr" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class Type(betterproto.Message):
    """Represents a CEL type."""

    # Dynamic type.
    dyn: "betterproto_lib_google_protobuf.Empty" = betterproto.message_field(
        1, group="type_kind"
    )
    # Null value.
    null: "betterproto_lib_google_protobuf.NullValue" = betterproto.enum_field(
        2, group="type_kind"
    )
    # Primitive types: `true`, `1u`, `-2.0`, `'string'`, `b'bytes'`.
    primitive: "TypePrimitiveType" = betterproto.enum_field(3, group="type_kind")
    # Wrapper of a primitive type, e.g. `google.protobuf.Int64Value`.
    wrapper: "TypePrimitiveType" = betterproto.enum_field(4, group="type_kind")
    # Well-known protobuf type such as `google.protobuf.Timestamp`.
    well_known: "TypeWellKnownType" = betterproto.enum_field(5, group="type_kind")
    # Parameterized list with elements of `list_type`, e.g. `list<timestamp>`.
    list_type: "TypeListType" = betterproto.message_field(6, group="type_kind")
    # Parameterized map with typed keys and values.
    map_type: "TypeMapType" = betterproto.message_field(7, group="type_kind")
    # Function type.
    function: "TypeFunctionType" = betterproto.message_field(8, group="type_kind")
    # Protocol buffer message type. The `message_type` string specifies the
    # qualified message type name. For example, `google.plus.Profile`.
    message_type: str = betterproto.string_field(9, group="type_kind")
    # Type param type. The `type_param` string specifies the type parameter name,
    # e.g. `list<E>` would be a `list_type` whose element type was a `type_param`
    # type named `E`.
    type_param: str = betterproto.string_field(10, group="type_kind")
    # Type type. The `type` value specifies the target type. e.g. int is type
    # with a target type of `Primitive.INT`.
    type: "Type" = betterproto.message_field(11, group="type_kind")
    # Error type. During type-checking if an expression is an error, its type is
    # propagated as the `ERROR` type. This permits the type-checker to discover
    # other errors present in the expression.
    error: "betterproto_lib_google_protobuf.Empty" = betterproto.message_field(
        12, group="type_kind"
    )
    # Abstract, application defined type.
    abstract_type: "TypeAbstractType" = betterproto.message_field(14, group="type_kind")


@dataclass(eq=False, repr=False)
class TypeListType(betterproto.Message):
    """List type with typed elements, e.g. `list<example.proto.MyMessage>`."""

    # The element type.
    elem_type: "Type" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class TypeMapType(betterproto.Message):
    """
    Map type with parameterized key and value types, e.g. `map<string, int>`.
    """

    # The type of the key.
    key_type: "Type" = betterproto.message_field(1)
    # The type of the value.
    value_type: "Type" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class TypeFunctionType(betterproto.Message):
    """Function type with result and arg types."""

    # Result type of the function.
    result_type: "Type" = betterproto.message_field(1)
    # Argument types of the function.
    arg_types: List["Type"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class TypeAbstractType(betterproto.Message):
    """Application defined abstract type."""

    # The fully qualified name of this abstract type.
    name: str = betterproto.string_field(1)
    # Parameter types for this abstract type.
    parameter_types: List["Type"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Decl(betterproto.Message):
    """
    Represents a declaration of a named value or function. A declaration is
    part of the contract between the expression, the agent evaluating that
    expression, and the caller requesting evaluation.
    """

    # The fully qualified name of the declaration. Declarations are organized in
    # containers and this represents the full path to the declaration in its
    # container, as in `google.api.expr.Decl`. Declarations used as [FunctionDecl
    # .Overload][google.api.expr.v1alpha1.Decl.FunctionDecl.Overload] parameters
    # may or may not have a name depending on whether the overload is function
    # declaration or a function definition containing a result
    # [Expr][google.api.expr.v1alpha1.Expr].
    name: str = betterproto.string_field(1)
    # Identifier declaration.
    ident: "DeclIdentDecl" = betterproto.message_field(2, group="decl_kind")
    # Function declaration.
    function: "DeclFunctionDecl" = betterproto.message_field(3, group="decl_kind")


@dataclass(eq=False, repr=False)
class DeclIdentDecl(betterproto.Message):
    """
    Identifier declaration which specifies its type and optional `Expr` value.
    An identifier without a value is a declaration that must be provided at
    evaluation time. An identifier with a value should resolve to a constant,
    but may be used in conjunction with other identifiers bound at evaluation
    time.
    """

    # Required. The type of the identifier.
    type: "Type" = betterproto.message_field(1)
    # The constant value of the identifier. If not specified, the identifier must
    # be supplied at evaluation time.
    value: "Constant" = betterproto.message_field(2)
    # Documentation string for the identifier.
    doc: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class DeclFunctionDecl(betterproto.Message):
    """
    Function declaration specifies one or more overloads which indicate the
    function's parameter types and return type. Functions have no observable
    side-effects (there may be side-effects like logging which are not
    observable from CEL).
    """

    # Required. List of function overloads, must contain at least one overload.
    overloads: List["DeclFunctionDeclOverload"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DeclFunctionDeclOverload(betterproto.Message):
    """
    An overload indicates a function's parameter types and return type, and may
    optionally include a function body described in terms of
    [Expr][google.api.expr.v1alpha1.Expr] values. Functions overloads are
    declared in either a function or method call-style. For methods, the
    `params[0]` is the expected type of the target receiver. Overloads must
    have non-overlapping argument types after erasure of all parameterized type
    variables (similar as type erasure in Java).
    """

    # Required. Globally unique overload name of the function which reflects the
    # function name and argument types. This will be used by a
    # [Reference][google.api.expr.v1alpha1.Reference] to indicate the
    # `overload_id` that was resolved for the function `name`.
    overload_id: str = betterproto.string_field(1)
    # List of function parameter [Type][google.api.expr.v1alpha1.Type] values.
    # Param types are disjoint after generic type parameters have been replaced
    # with the type `DYN`. Since the `DYN` type is compatible with any other
    # type, this means that if `A` is a type parameter, the function types
    # `int<A>` and `int<int>` are not disjoint. Likewise, `map<string, string>`
    # is not disjoint from `map<K, V>`. When the `result_type` of a function is a
    # generic type param, the type param name also appears as the `type` of on at
    # least one params.
    params: List["Type"] = betterproto.message_field(2)
    # The type param names associated with the function declaration. For example,
    # `function ex<K,V>(K key, map<K, V> map) : V` would yield the type params of
    # `K, V`.
    type_params: List[str] = betterproto.string_field(3)
    # Required. The result type of the function. For example, the operator
    # `string.isEmpty()` would have `result_type` of `kind: BOOL`.
    result_type: "Type" = betterproto.message_field(4)
    # Whether the function is to be used in a method call-style `x.f(...)` of a
    # function call-style `f(x, ...)`. For methods, the first parameter
    # declaration, `params[0]` is the expected type of the target receiver.
    is_instance_function: bool = betterproto.bool_field(5)
    # Documentation string for the overload.
    doc: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class Reference(betterproto.Message):
    """Describes a resolved reference to a declaration."""

    # The fully qualified name of the declaration.
    name: str = betterproto.string_field(1)
    # For references to functions, this is a list of `Overload.overload_id`
    # values which match according to typing rules. If the list has more than one
    # element, overload resolution among the presented candidates must happen at
    # runtime because of dynamic types. The type checker attempts to narrow down
    # this list as much as possible. Empty if this is not a reference to a
    # [Decl.FunctionDecl][google.api.expr.v1alpha1.Decl.FunctionDecl].
    overload_id: List[str] = betterproto.string_field(3)
    # For references to constants, this may contain the value of the constant if
    # known at compile time.
    value: "Constant" = betterproto.message_field(4)


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
