# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/pandas/series.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/pandas/series.proto",
    package="syft.lib.pandas",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1dproto/lib/pandas/series.proto\x12\x0fsyft.lib.pandas"9\n\x0cPandasSeries\x12\x0e\n\x06series\x18\x01 \x01(\x0c\x12\x19\n\x11\x64\x65\x63ompressed_size\x18\x02 \x01(\x04\x62\x06proto3',
)


_PANDASSERIES = _descriptor.Descriptor(
    name="PandasSeries",
    full_name="syft.lib.pandas.PandasSeries",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="series",
            full_name="syft.lib.pandas.PandasSeries.series",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="decompressed_size",
            full_name="syft.lib.pandas.PandasSeries.decompressed_size",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=50,
    serialized_end=107,
)

DESCRIPTOR.message_types_by_name["PandasSeries"] = _PANDASSERIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PandasSeries = _reflection.GeneratedProtocolMessageType(
    "PandasSeries",
    (_message.Message,),
    {
        "DESCRIPTOR": _PANDASSERIES,
        "__module__": "proto.lib.pandas.series_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.pandas.PandasSeries)
    },
)
_sym_db.RegisterMessage(PandasSeries)


# @@protoc_insertion_point(module_scope)