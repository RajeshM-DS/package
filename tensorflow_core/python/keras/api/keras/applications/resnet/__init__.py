# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""ResNet models for Keras.

"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.keras.applications.resnet import ResNet101
from tensorflow.python.keras.applications.resnet import ResNet152
from tensorflow.python.keras.applications.resnet import ResNet50
from tensorflow.python.keras.applications.resnet import decode_predictions
from tensorflow.python.keras.applications.resnet import preprocess_input

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.applications.resnet", public_apis=None, deprecation=True,
      has_lite=False)
