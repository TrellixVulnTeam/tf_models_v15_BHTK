# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/stdn.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import anchor_generator_pb2 as object__detection_dot_protos_dot_anchor__generator__pb2
from object_detection.protos import box_coder_pb2 as object__detection_dot_protos_dot_box__coder__pb2
from object_detection.protos import box_predictor_pb2 as object__detection_dot_protos_dot_box__predictor__pb2
from object_detection.protos import hyperparams_pb2 as object__detection_dot_protos_dot_hyperparams__pb2
from object_detection.protos import image_resizer_pb2 as object__detection_dot_protos_dot_image__resizer__pb2
from object_detection.protos import matcher_pb2 as object__detection_dot_protos_dot_matcher__pb2
from object_detection.protos import losses_pb2 as object__detection_dot_protos_dot_losses__pb2
from object_detection.protos import post_processing_pb2 as object__detection_dot_protos_dot_post__processing__pb2
from object_detection.protos import region_similarity_calculator_pb2 as object__detection_dot_protos_dot_region__similarity__calculator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/stdn.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n\"object_detection/protos/stdn.proto\x12\x17object_detection.protos\x1a.object_detection/protos/anchor_generator.proto\x1a\'object_detection/protos/box_coder.proto\x1a+object_detection/protos/box_predictor.proto\x1a)object_detection/protos/hyperparams.proto\x1a+object_detection/protos/image_resizer.proto\x1a%object_detection/protos/matcher.proto\x1a$object_detection/protos/losses.proto\x1a-object_detection/protos/post_processing.proto\x1a:object_detection/protos/region_similarity_calculator.proto\"\xfe\x04\n\x04Stdn\x12\x13\n\x0bnum_classes\x18\x01 \x01(\x05\x12<\n\rimage_resizer\x18\x02 \x01(\x0b\x32%.object_detection.protos.ImageResizer\x12H\n\x11\x66\x65\x61ture_extractor\x18\x03 \x01(\x0b\x32-.object_detection.protos.StdnFeatureExtractor\x12\x34\n\tbox_coder\x18\x04 \x01(\x0b\x32!.object_detection.protos.BoxCoder\x12\x31\n\x07matcher\x18\x05 \x01(\x0b\x32 .object_detection.protos.Matcher\x12R\n\x15similarity_calculator\x18\x06 \x01(\x0b\x32\x33.object_detection.protos.RegionSimilarityCalculator\x12<\n\rbox_predictor\x18\x07 \x01(\x0b\x32%.object_detection.protos.BoxPredictor\x12\x42\n\x10\x61nchor_generator\x18\x08 \x01(\x0b\x32(.object_detection.protos.AnchorGenerator\x12@\n\x0fpost_processing\x18\t \x01(\x0b\x32\'.object_detection.protos.PostProcessing\x12+\n\x1dnormalize_loss_by_num_matches\x18\n \x01(\x08:\x04true\x12+\n\x04loss\x18\x0b \x01(\x0b\x32\x1d.object_detection.protos.Loss\"\xd8\x01\n\x14StdnFeatureExtractor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1b\n\x10\x64\x65pth_multiplier\x18\x02 \x01(\x02:\x01\x31\x12\x15\n\tmin_depth\x18\x03 \x01(\x05:\x02\x31\x36\x12>\n\x10\x63onv_hyperparams\x18\x04 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x1a\n\x0fpad_to_multiple\x18\x05 \x01(\x05:\x01\x31\x12\"\n\x14\x62\x61tch_norm_trainable\x18\x06 \x01(\x08:\x04true')
  ,
  dependencies=[object__detection_dot_protos_dot_anchor__generator__pb2.DESCRIPTOR,object__detection_dot_protos_dot_box__coder__pb2.DESCRIPTOR,object__detection_dot_protos_dot_box__predictor__pb2.DESCRIPTOR,object__detection_dot_protos_dot_hyperparams__pb2.DESCRIPTOR,object__detection_dot_protos_dot_image__resizer__pb2.DESCRIPTOR,object__detection_dot_protos_dot_matcher__pb2.DESCRIPTOR,object__detection_dot_protos_dot_losses__pb2.DESCRIPTOR,object__detection_dot_protos_dot_post__processing__pb2.DESCRIPTOR,object__detection_dot_protos_dot_region__similarity__calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STDN = _descriptor.Descriptor(
  name='Stdn',
  full_name='object_detection.protos.Stdn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='object_detection.protos.Stdn.num_classes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_resizer', full_name='object_detection.protos.Stdn.image_resizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_extractor', full_name='object_detection.protos.Stdn.feature_extractor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_coder', full_name='object_detection.protos.Stdn.box_coder', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matcher', full_name='object_detection.protos.Stdn.matcher', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='similarity_calculator', full_name='object_detection.protos.Stdn.similarity_calculator', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_predictor', full_name='object_detection.protos.Stdn.box_predictor', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchor_generator', full_name='object_detection.protos.Stdn.anchor_generator', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_processing', full_name='object_detection.protos.Stdn.post_processing', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalize_loss_by_num_matches', full_name='object_detection.protos.Stdn.normalize_loss_by_num_matches', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss', full_name='object_detection.protos.Stdn.loss', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=1108,
)


_STDNFEATUREEXTRACTOR = _descriptor.Descriptor(
  name='StdnFeatureExtractor',
  full_name='object_detection.protos.StdnFeatureExtractor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='object_detection.protos.StdnFeatureExtractor.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth_multiplier', full_name='object_detection.protos.StdnFeatureExtractor.depth_multiplier', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_depth', full_name='object_detection.protos.StdnFeatureExtractor.min_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='object_detection.protos.StdnFeatureExtractor.conv_hyperparams', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pad_to_multiple', full_name='object_detection.protos.StdnFeatureExtractor.pad_to_multiple', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_norm_trainable', full_name='object_detection.protos.StdnFeatureExtractor.batch_norm_trainable', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1111,
  serialized_end=1327,
)

_STDN.fields_by_name['image_resizer'].message_type = object__detection_dot_protos_dot_image__resizer__pb2._IMAGERESIZER
_STDN.fields_by_name['feature_extractor'].message_type = _STDNFEATUREEXTRACTOR
_STDN.fields_by_name['box_coder'].message_type = object__detection_dot_protos_dot_box__coder__pb2._BOXCODER
_STDN.fields_by_name['matcher'].message_type = object__detection_dot_protos_dot_matcher__pb2._MATCHER
_STDN.fields_by_name['similarity_calculator'].message_type = object__detection_dot_protos_dot_region__similarity__calculator__pb2._REGIONSIMILARITYCALCULATOR
_STDN.fields_by_name['box_predictor'].message_type = object__detection_dot_protos_dot_box__predictor__pb2._BOXPREDICTOR
_STDN.fields_by_name['anchor_generator'].message_type = object__detection_dot_protos_dot_anchor__generator__pb2._ANCHORGENERATOR
_STDN.fields_by_name['post_processing'].message_type = object__detection_dot_protos_dot_post__processing__pb2._POSTPROCESSING
_STDN.fields_by_name['loss'].message_type = object__detection_dot_protos_dot_losses__pb2._LOSS
_STDNFEATUREEXTRACTOR.fields_by_name['conv_hyperparams'].message_type = object__detection_dot_protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['Stdn'] = _STDN
DESCRIPTOR.message_types_by_name['StdnFeatureExtractor'] = _STDNFEATUREEXTRACTOR

Stdn = _reflection.GeneratedProtocolMessageType('Stdn', (_message.Message,), dict(
  DESCRIPTOR = _STDN,
  __module__ = 'object_detection.protos.stdn_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Stdn)
  ))
_sym_db.RegisterMessage(Stdn)

StdnFeatureExtractor = _reflection.GeneratedProtocolMessageType('StdnFeatureExtractor', (_message.Message,), dict(
  DESCRIPTOR = _STDNFEATUREEXTRACTOR,
  __module__ = 'object_detection.protos.stdn_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.StdnFeatureExtractor)
  ))
_sym_db.RegisterMessage(StdnFeatureExtractor)


# @@protoc_insertion_point(module_scope)
