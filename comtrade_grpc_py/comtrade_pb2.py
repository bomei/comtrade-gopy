# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comtrade.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='comtrade.proto',
  package='comtrade',
  syntax='proto3',
  serialized_options=b'\n\035io.grpc.examples.comtradegrpcB\021ComtradeGRPCProtoP\001Z\026comtrade-gprc/comtrade',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63omtrade.proto\x12\x08\x63omtrade\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\rAnalogChannel\x12\r\n\x05value\x18\x01 \x03(\x01\"2\n\x06\x41nalog\x12(\n\x07\x63hannel\x18\x01 \x03(\x0b\x32\x17.comtrade.AnalogChannel\"\x1e\n\rStatusChannel\x12\r\n\x05value\x18\x01 \x03(\x05\"2\n\x06Status\x12(\n\x07\x63hannel\x18\x01 \x03(\x0b\x32\x17.comtrade.StatusChannel\"\x15\n\x04Time\x12\r\n\x05value\x18\x01 \x03(\x01\"n\n\rWaveDataReply\x12 \n\x06\x61nalog\x18\x01 \x01(\x0b\x32\x10.comtrade.Analog\x12 \n\x06status\x18\x02 \x01(\x0b\x32\x10.comtrade.Status\x12\x19\n\x01t\x18\x03 \x01(\x0b\x32\x0e.comtrade.Time\"&\n\rSampleRateRow\x12\x15\n\rsampleRateRow\x18\x01 \x03(\x05\"\xf5\x01\n\rDatParseParam\x12\x0f\n\x07\x64\x61tFile\x18\x01 \x01(\t\x12\x10\n\x08timeMult\x18\x02 \x01(\x05\x12\x10\n\x08timeBase\x18\x03 \x01(\x01\x12\x11\n\tachannels\x18\x04 \x01(\x05\x12\x11\n\tschannels\x18\x05 \x01(\x05\x12\t\n\x01\x61\x18\x06 \x03(\x01\x12\t\n\x01\x62\x18\x07 \x03(\x01\x12\x16\n\x0egroupsOf16Bits\x18\x08 \x01(\x05\x12\x13\n\x0btotalSample\x18\t \x01(\x05\x12\x19\n\x11timestampCritical\x18\n \x01(\x08\x12+\n\nsampleRate\x18\x0b \x03(\x0b\x32\x17.comtrade.SampleRateRow2\xc1\x01\n\x07Greeter\x12:\n\x08SayHello\x12\x16.comtrade.HelloRequest\x1a\x14.comtrade.HelloReply\"\x00\x12>\n\x08\x46\x61stLoad\x12\x17.comtrade.DatParseParam\x1a\x17.comtrade.WaveDataReply\"\x00\x12:\n\x0cTestFastLoad\x12\x16.comtrade.HelloRequest\x1a\x10.comtrade.Analog\"\x00\x42L\n\x1dio.grpc.examples.comtradegrpcB\x11\x43omtradeGRPCProtoP\x01Z\x16\x63omtrade-gprc/comtradeb\x06proto3'
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='comtrade.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='comtrade.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=56,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='comtrade.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='comtrade.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=87,
)


_ANALOGCHANNEL = _descriptor.Descriptor(
  name='AnalogChannel',
  full_name='comtrade.AnalogChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='comtrade.AnalogChannel.value', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=119,
)


_ANALOG = _descriptor.Descriptor(
  name='Analog',
  full_name='comtrade.Analog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='comtrade.Analog.channel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=171,
)


_STATUSCHANNEL = _descriptor.Descriptor(
  name='StatusChannel',
  full_name='comtrade.StatusChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='comtrade.StatusChannel.value', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=203,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='comtrade.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='comtrade.Status.channel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=255,
)


_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='comtrade.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='comtrade.Time.value', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=278,
)


_WAVEDATAREPLY = _descriptor.Descriptor(
  name='WaveDataReply',
  full_name='comtrade.WaveDataReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='analog', full_name='comtrade.WaveDataReply.analog', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='comtrade.WaveDataReply.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='t', full_name='comtrade.WaveDataReply.t', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=390,
)


_SAMPLERATEROW = _descriptor.Descriptor(
  name='SampleRateRow',
  full_name='comtrade.SampleRateRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sampleRateRow', full_name='comtrade.SampleRateRow.sampleRateRow', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=430,
)


_DATPARSEPARAM = _descriptor.Descriptor(
  name='DatParseParam',
  full_name='comtrade.DatParseParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datFile', full_name='comtrade.DatParseParam.datFile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeMult', full_name='comtrade.DatParseParam.timeMult', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeBase', full_name='comtrade.DatParseParam.timeBase', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='achannels', full_name='comtrade.DatParseParam.achannels', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schannels', full_name='comtrade.DatParseParam.schannels', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a', full_name='comtrade.DatParseParam.a', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='comtrade.DatParseParam.b', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupsOf16Bits', full_name='comtrade.DatParseParam.groupsOf16Bits', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalSample', full_name='comtrade.DatParseParam.totalSample', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestampCritical', full_name='comtrade.DatParseParam.timestampCritical', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sampleRate', full_name='comtrade.DatParseParam.sampleRate', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=678,
)

_ANALOG.fields_by_name['channel'].message_type = _ANALOGCHANNEL
_STATUS.fields_by_name['channel'].message_type = _STATUSCHANNEL
_WAVEDATAREPLY.fields_by_name['analog'].message_type = _ANALOG
_WAVEDATAREPLY.fields_by_name['status'].message_type = _STATUS
_WAVEDATAREPLY.fields_by_name['t'].message_type = _TIME
_DATPARSEPARAM.fields_by_name['sampleRate'].message_type = _SAMPLERATEROW
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['AnalogChannel'] = _ANALOGCHANNEL
DESCRIPTOR.message_types_by_name['Analog'] = _ANALOG
DESCRIPTOR.message_types_by_name['StatusChannel'] = _STATUSCHANNEL
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['WaveDataReply'] = _WAVEDATAREPLY
DESCRIPTOR.message_types_by_name['SampleRateRow'] = _SAMPLERATEROW
DESCRIPTOR.message_types_by_name['DatParseParam'] = _DATPARSEPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

AnalogChannel = _reflection.GeneratedProtocolMessageType('AnalogChannel', (_message.Message,), {
  'DESCRIPTOR' : _ANALOGCHANNEL,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.AnalogChannel)
  })
_sym_db.RegisterMessage(AnalogChannel)

Analog = _reflection.GeneratedProtocolMessageType('Analog', (_message.Message,), {
  'DESCRIPTOR' : _ANALOG,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.Analog)
  })
_sym_db.RegisterMessage(Analog)

StatusChannel = _reflection.GeneratedProtocolMessageType('StatusChannel', (_message.Message,), {
  'DESCRIPTOR' : _STATUSCHANNEL,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.StatusChannel)
  })
_sym_db.RegisterMessage(StatusChannel)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.Status)
  })
_sym_db.RegisterMessage(Status)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
  'DESCRIPTOR' : _TIME,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.Time)
  })
_sym_db.RegisterMessage(Time)

WaveDataReply = _reflection.GeneratedProtocolMessageType('WaveDataReply', (_message.Message,), {
  'DESCRIPTOR' : _WAVEDATAREPLY,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.WaveDataReply)
  })
_sym_db.RegisterMessage(WaveDataReply)

SampleRateRow = _reflection.GeneratedProtocolMessageType('SampleRateRow', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLERATEROW,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.SampleRateRow)
  })
_sym_db.RegisterMessage(SampleRateRow)

DatParseParam = _reflection.GeneratedProtocolMessageType('DatParseParam', (_message.Message,), {
  'DESCRIPTOR' : _DATPARSEPARAM,
  '__module__' : 'comtrade_pb2'
  # @@protoc_insertion_point(class_scope:comtrade.DatParseParam)
  })
_sym_db.RegisterMessage(DatParseParam)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='comtrade.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=681,
  serialized_end=874,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='comtrade.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FastLoad',
    full_name='comtrade.Greeter.FastLoad',
    index=1,
    containing_service=None,
    input_type=_DATPARSEPARAM,
    output_type=_WAVEDATAREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestFastLoad',
    full_name='comtrade.Greeter.TestFastLoad',
    index=2,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_ANALOG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)