# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Keras backend API.

"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.framework.ops import name_scope_v1 as name_scope
from tensorflow.python.keras.backend import abs
from tensorflow.python.keras.backend import all
from tensorflow.python.keras.backend import any
from tensorflow.python.keras.backend import arange
from tensorflow.python.keras.backend import argmax
from tensorflow.python.keras.backend import argmin
from tensorflow.python.keras.backend import backend
from tensorflow.python.keras.backend import batch_dot
from tensorflow.python.keras.backend import batch_flatten
from tensorflow.python.keras.backend import batch_get_value
from tensorflow.python.keras.backend import batch_normalization
from tensorflow.python.keras.backend import batch_set_value
from tensorflow.python.keras.backend import bias_add
from tensorflow.python.keras.backend import binary_crossentropy
from tensorflow.python.keras.backend import cast
from tensorflow.python.keras.backend import cast_to_floatx
from tensorflow.python.keras.backend import categorical_crossentropy
from tensorflow.python.keras.backend import clear_session
from tensorflow.python.keras.backend import clip
from tensorflow.python.keras.backend import concatenate
from tensorflow.python.keras.backend import constant
from tensorflow.python.keras.backend import conv1d
from tensorflow.python.keras.backend import conv2d
from tensorflow.python.keras.backend import conv2d_transpose
from tensorflow.python.keras.backend import conv3d
from tensorflow.python.keras.backend import cos
from tensorflow.python.keras.backend import count_params
from tensorflow.python.keras.backend import ctc_batch_cost
from tensorflow.python.keras.backend import ctc_decode
from tensorflow.python.keras.backend import ctc_label_dense_to_sparse
from tensorflow.python.keras.backend import cumprod
from tensorflow.python.keras.backend import cumsum
from tensorflow.python.keras.backend import depthwise_conv2d
from tensorflow.python.keras.backend import dot
from tensorflow.python.keras.backend import dropout
from tensorflow.python.keras.backend import dtype
from tensorflow.python.keras.backend import elu
from tensorflow.python.keras.backend import equal
from tensorflow.python.keras.backend import eval
from tensorflow.python.keras.backend import exp
from tensorflow.python.keras.backend import expand_dims
from tensorflow.python.keras.backend import eye
from tensorflow.python.keras.backend import flatten
from tensorflow.python.keras.backend import foldl
from tensorflow.python.keras.backend import foldr
from tensorflow.python.keras.backend import function
from tensorflow.python.keras.backend import gather
from tensorflow.python.keras.backend import get_session
from tensorflow.python.keras.backend import get_uid
from tensorflow.python.keras.backend import get_value
from tensorflow.python.keras.backend import gradients
from tensorflow.python.keras.backend import greater
from tensorflow.python.keras.backend import greater_equal
from tensorflow.python.keras.backend import hard_sigmoid
from tensorflow.python.keras.backend import in_test_phase
from tensorflow.python.keras.backend import in_top_k
from tensorflow.python.keras.backend import in_train_phase
from tensorflow.python.keras.backend import int_shape
from tensorflow.python.keras.backend import is_keras_tensor
from tensorflow.python.keras.backend import is_sparse
from tensorflow.python.keras.backend import l2_normalize
from tensorflow.python.keras.backend import learning_phase
from tensorflow.python.keras.backend import learning_phase_scope
from tensorflow.python.keras.backend import less
from tensorflow.python.keras.backend import less_equal
from tensorflow.python.keras.backend import local_conv1d
from tensorflow.python.keras.backend import local_conv2d
from tensorflow.python.keras.backend import log
from tensorflow.python.keras.backend import manual_variable_initialization
from tensorflow.python.keras.backend import map_fn
from tensorflow.python.keras.backend import max
from tensorflow.python.keras.backend import maximum
from tensorflow.python.keras.backend import mean
from tensorflow.python.keras.backend import min
from tensorflow.python.keras.backend import minimum
from tensorflow.python.keras.backend import moving_average_update
from tensorflow.python.keras.backend import ndim
from tensorflow.python.keras.backend import normalize_batch_in_training
from tensorflow.python.keras.backend import not_equal
from tensorflow.python.keras.backend import one_hot
from tensorflow.python.keras.backend import ones
from tensorflow.python.keras.backend import ones_like
from tensorflow.python.keras.backend import permute_dimensions
from tensorflow.python.keras.backend import placeholder
from tensorflow.python.keras.backend import pool2d
from tensorflow.python.keras.backend import pool3d
from tensorflow.python.keras.backend import pow
from tensorflow.python.keras.backend import print_tensor
from tensorflow.python.keras.backend import prod
from tensorflow.python.keras.backend import random_binomial
from tensorflow.python.keras.backend import random_normal
from tensorflow.python.keras.backend import random_normal_variable
from tensorflow.python.keras.backend import random_uniform
from tensorflow.python.keras.backend import random_uniform_variable
from tensorflow.python.keras.backend import relu
from tensorflow.python.keras.backend import repeat
from tensorflow.python.keras.backend import repeat_elements
from tensorflow.python.keras.backend import reset_uids
from tensorflow.python.keras.backend import reshape
from tensorflow.python.keras.backend import resize_images
from tensorflow.python.keras.backend import resize_volumes
from tensorflow.python.keras.backend import reverse
from tensorflow.python.keras.backend import rnn
from tensorflow.python.keras.backend import round
from tensorflow.python.keras.backend import separable_conv2d
from tensorflow.python.keras.backend import set_learning_phase
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.backend import set_value
from tensorflow.python.keras.backend import shape
from tensorflow.python.keras.backend import sigmoid
from tensorflow.python.keras.backend import sign
from tensorflow.python.keras.backend import sin
from tensorflow.python.keras.backend import softmax
from tensorflow.python.keras.backend import softplus
from tensorflow.python.keras.backend import softsign
from tensorflow.python.keras.backend import sparse_categorical_crossentropy
from tensorflow.python.keras.backend import spatial_2d_padding
from tensorflow.python.keras.backend import spatial_3d_padding
from tensorflow.python.keras.backend import sqrt
from tensorflow.python.keras.backend import square
from tensorflow.python.keras.backend import squeeze
from tensorflow.python.keras.backend import stack
from tensorflow.python.keras.backend import std
from tensorflow.python.keras.backend import stop_gradient
from tensorflow.python.keras.backend import sum
from tensorflow.python.keras.backend import switch
from tensorflow.python.keras.backend import tanh
from tensorflow.python.keras.backend import temporal_padding
from tensorflow.python.keras.backend import tile
from tensorflow.python.keras.backend import to_dense
from tensorflow.python.keras.backend import transpose
from tensorflow.python.keras.backend import truncated_normal
from tensorflow.python.keras.backend import update
from tensorflow.python.keras.backend import update_add
from tensorflow.python.keras.backend import update_sub
from tensorflow.python.keras.backend import var
from tensorflow.python.keras.backend import variable
from tensorflow.python.keras.backend import zeros
from tensorflow.python.keras.backend import zeros_like
from tensorflow.python.keras.backend_config import epsilon
from tensorflow.python.keras.backend_config import floatx
from tensorflow.python.keras.backend_config import image_data_format
from tensorflow.python.keras.backend_config import set_epsilon
from tensorflow.python.keras.backend_config import set_floatx
from tensorflow.python.keras.backend_config import set_image_data_format

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.backend", public_apis=None, deprecation=True,
      has_lite=False)
