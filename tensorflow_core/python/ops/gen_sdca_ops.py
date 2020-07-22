"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
"""

import collections

from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util import dispatch as _dispatch
from tensorflow.python.util.tf_export import tf_export


@_dispatch.add_dispatch_list
@tf_export(v1=['train.sdca_fprint'])
@deprecated_endpoints('train.sdca_fprint')
def sdca_fprint(input, name=None):
  r"""Computes fingerprints of the input strings.

  Args:
    input: A `Tensor` of type `string`.
      vector of strings to compute fingerprints on.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "SdcaFprint", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return sdca_fprint_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              sdca_fprint, input=input, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "SdcaFprint", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          sdca_fprint, input=input, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "SdcaFprint", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

SdcaFprint = tf_export("raw_ops.SdcaFprint")(_ops.to_raw_op(sdca_fprint))


def sdca_fprint_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.string)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"SdcaFprint", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "SdcaFprint", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_SdcaOptimizerOutput = collections.namedtuple(
    "SdcaOptimizer",
    ["out_example_state_data", "out_delta_sparse_weights", "out_delta_dense_weights"])


@_dispatch.add_dispatch_list
@tf_export(v1=['train.sdca_optimizer'])
@deprecated_endpoints('train.sdca_optimizer')
def sdca_optimizer(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptative=True, name=None):
  r"""Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

  linear models with L1 + L2 regularization. As global optimization objective is
  strongly-convex, the optimizer optimizes the dual objective at each step. The
  optimizer applies each update one example at a time. Examples are sampled
  uniformly, and the optimizer is learning rate free and enjoys linear convergence
  rate.

  [Proximal Stochastic Dual Coordinate Ascent](http://arxiv.org/pdf/1211.2717v1.pdf).<br>
  Shai Shalev-Shwartz, Tong Zhang. 2012

  $$Loss Objective = \sum f_{i} (wx_{i}) + (l2 / 2) * |w|^2 + l1 * |w|$$

  [Adding vs. Averaging in Distributed Primal-Dual Optimization](http://arxiv.org/abs/1502.03508).<br>
  Chenxin Ma, Virginia Smith, Martin Jaggi, Michael I. Jordan,
  Peter Richtarik, Martin Takac. 2015

  [Stochastic Dual Coordinate Ascent with Adaptive Probabilities](https://arxiv.org/abs/1502.08053).<br>
  Dominik Csiba, Zheng Qu, Peter Richtarik. 2015

  Args:
    sparse_example_indices: A list of `Tensor` objects with type `int64`.
      a list of vectors which contain example indices.
    sparse_feature_indices: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
      a list of vectors which contain feature indices.
    sparse_feature_values: A list of `Tensor` objects with type `float32`.
      a list of vectors which contains feature value
      associated with each feature group.
    dense_features: A list of `Tensor` objects with type `float32`.
      a list of matrices which contains the dense feature values.
    example_weights: A `Tensor` of type `float32`.
      a vector which contains the weight associated with each
      example.
    example_labels: A `Tensor` of type `float32`.
      a vector which contains the label/target associated with each
      example.
    sparse_indices: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
      a list of vectors where each value is the indices which has
      corresponding weights in sparse_weights. This field maybe omitted for the
      dense approach.
    sparse_weights: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
      a list of vectors where each value is the weight associated with
      a sparse feature group.
    dense_weights: A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
      a list of vectors where the values are the weights associated
      with a dense feature group.
    example_state_data: A `Tensor` of type `float32`.
      a list of vectors containing the example state data.
    loss_type: A `string` from: `"logistic_loss", "squared_loss", "hinge_loss", "smooth_hinge_loss", "poisson_loss"`.
      Type of the primal loss. Currently SdcaSolver supports logistic,
      squared and hinge losses.
    l1: A `float`. Symmetric l1 regularization strength.
    l2: A `float`. Symmetric l2 regularization strength.
    num_loss_partitions: An `int` that is `>= 1`.
      Number of partitions of the global loss function.
    num_inner_iterations: An `int` that is `>= 1`.
      Number of iterations per mini-batch.
    adaptative: An optional `bool`. Defaults to `True`.
      Whether to use Adaptive SDCA for the inner loop.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (out_example_state_data, out_delta_sparse_weights, out_delta_dense_weights).

    out_example_state_data: A `Tensor` of type `float32`.
    out_delta_sparse_weights: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
    out_delta_dense_weights: A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "SdcaOptimizer", name,
        tld.op_callbacks, sparse_example_indices, sparse_feature_indices,
        sparse_feature_values, dense_features, example_weights,
        example_labels, sparse_indices, sparse_weights, dense_weights,
        example_state_data, "loss_type", loss_type, "adaptative", adaptative,
        "l1", l1, "l2", l2, "num_loss_partitions", num_loss_partitions,
        "num_inner_iterations", num_inner_iterations)
      _result = _SdcaOptimizerOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return sdca_optimizer_eager_fallback(
            sparse_example_indices, sparse_feature_indices,
            sparse_feature_values, dense_features, example_weights,
            example_labels, sparse_indices, sparse_weights, dense_weights,
            example_state_data, loss_type=loss_type, adaptative=adaptative,
            l1=l1, l2=l2, num_loss_partitions=num_loss_partitions,
            num_inner_iterations=num_inner_iterations, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              sdca_optimizer, sparse_example_indices=sparse_example_indices,
                              sparse_feature_indices=sparse_feature_indices,
                              sparse_feature_values=sparse_feature_values,
                              dense_features=dense_features,
                              example_weights=example_weights,
                              example_labels=example_labels,
                              sparse_indices=sparse_indices,
                              sparse_weights=sparse_weights,
                              dense_weights=dense_weights,
                              example_state_data=example_state_data,
                              loss_type=loss_type, l1=l1, l2=l2,
                              num_loss_partitions=num_loss_partitions,
                              num_inner_iterations=num_inner_iterations,
                              adaptative=adaptative, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if not isinstance(sparse_example_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_example_indices' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_example_indices)
  _attr_num_sparse_features = len(sparse_example_indices)
  if not isinstance(sparse_feature_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_indices' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_feature_indices)
  if len(sparse_feature_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_feature_indices' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_feature_indices), _attr_num_sparse_features))
  if not isinstance(sparse_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_indices' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_indices)
  if len(sparse_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_indices' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_indices), _attr_num_sparse_features))
  if not isinstance(sparse_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_weights' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_weights)
  if len(sparse_weights) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_weights' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_weights), _attr_num_sparse_features))
  if not isinstance(sparse_feature_values, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_values' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_feature_values)
  _attr_num_sparse_features_with_values = len(sparse_feature_values)
  if not isinstance(dense_features, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_features' argument to "
        "'sdca_optimizer' Op, not %r." % dense_features)
  _attr_num_dense_features = len(dense_features)
  if not isinstance(dense_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_weights' argument to "
        "'sdca_optimizer' Op, not %r." % dense_weights)
  if len(dense_weights) != _attr_num_dense_features:
    raise ValueError(
        "List argument 'dense_weights' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'dense_features'." %
        (len(dense_weights), _attr_num_dense_features))
  loss_type = _execute.make_str(loss_type, "loss_type")
  l1 = _execute.make_float(l1, "l1")
  l2 = _execute.make_float(l2, "l2")
  num_loss_partitions = _execute.make_int(num_loss_partitions, "num_loss_partitions")
  num_inner_iterations = _execute.make_int(num_inner_iterations, "num_inner_iterations")
  if adaptative is None:
    adaptative = True
  adaptative = _execute.make_bool(adaptative, "adaptative")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "SdcaOptimizer", sparse_example_indices=sparse_example_indices,
                         sparse_feature_indices=sparse_feature_indices,
                         sparse_feature_values=sparse_feature_values,
                         dense_features=dense_features,
                         example_weights=example_weights,
                         example_labels=example_labels,
                         sparse_indices=sparse_indices,
                         sparse_weights=sparse_weights,
                         dense_weights=dense_weights,
                         example_state_data=example_state_data,
                         loss_type=loss_type, l1=l1, l2=l2,
                         num_loss_partitions=num_loss_partitions,
                         num_inner_iterations=num_inner_iterations,
                         adaptative=adaptative, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          sdca_optimizer, sparse_example_indices=sparse_example_indices,
                          sparse_feature_indices=sparse_feature_indices,
                          sparse_feature_values=sparse_feature_values,
                          dense_features=dense_features,
                          example_weights=example_weights,
                          example_labels=example_labels,
                          sparse_indices=sparse_indices,
                          sparse_weights=sparse_weights,
                          dense_weights=dense_weights,
                          example_state_data=example_state_data,
                          loss_type=loss_type, l1=l1, l2=l2,
                          num_loss_partitions=num_loss_partitions,
                          num_inner_iterations=num_inner_iterations,
                          adaptative=adaptative, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("loss_type", _op.get_attr("loss_type"), "adaptative",
              _op._get_attr_bool("adaptative"), "num_sparse_features",
              _op._get_attr_int("num_sparse_features"),
              "num_sparse_features_with_values",
              _op._get_attr_int("num_sparse_features_with_values"),
              "num_dense_features", _op._get_attr_int("num_dense_features"),
              "l1", _op.get_attr("l1"), "l2", _op.get_attr("l2"),
              "num_loss_partitions", _op._get_attr_int("num_loss_partitions"),
              "num_inner_iterations",
              _op._get_attr_int("num_inner_iterations"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "SdcaOptimizer", _inputs_flat, _attrs, _result)
  _result = _result[:1] + [_result[1:1 + _attr_num_sparse_features]] + _result[1 + _attr_num_sparse_features:]
  _result = _result[:2] + [_result[2:]]
  _result = _SdcaOptimizerOutput._make(_result)
  return _result

SdcaOptimizer = tf_export("raw_ops.SdcaOptimizer")(_ops.to_raw_op(sdca_optimizer))


def sdca_optimizer_eager_fallback(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptative, name, ctx):
  if not isinstance(sparse_example_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_example_indices' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_example_indices)
  _attr_num_sparse_features = len(sparse_example_indices)
  if not isinstance(sparse_feature_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_indices' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_feature_indices)
  if len(sparse_feature_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_feature_indices' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_feature_indices), _attr_num_sparse_features))
  if not isinstance(sparse_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_indices' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_indices)
  if len(sparse_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_indices' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_indices), _attr_num_sparse_features))
  if not isinstance(sparse_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_weights' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_weights)
  if len(sparse_weights) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_weights' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_weights), _attr_num_sparse_features))
  if not isinstance(sparse_feature_values, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_values' argument to "
        "'sdca_optimizer' Op, not %r." % sparse_feature_values)
  _attr_num_sparse_features_with_values = len(sparse_feature_values)
  if not isinstance(dense_features, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_features' argument to "
        "'sdca_optimizer' Op, not %r." % dense_features)
  _attr_num_dense_features = len(dense_features)
  if not isinstance(dense_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_weights' argument to "
        "'sdca_optimizer' Op, not %r." % dense_weights)
  if len(dense_weights) != _attr_num_dense_features:
    raise ValueError(
        "List argument 'dense_weights' to 'sdca_optimizer' Op with length %d "
        "must match length %d of argument 'dense_features'." %
        (len(dense_weights), _attr_num_dense_features))
  loss_type = _execute.make_str(loss_type, "loss_type")
  l1 = _execute.make_float(l1, "l1")
  l2 = _execute.make_float(l2, "l2")
  num_loss_partitions = _execute.make_int(num_loss_partitions, "num_loss_partitions")
  num_inner_iterations = _execute.make_int(num_inner_iterations, "num_inner_iterations")
  if adaptative is None:
    adaptative = True
  adaptative = _execute.make_bool(adaptative, "adaptative")
  sparse_example_indices = _ops.convert_n_to_tensor(sparse_example_indices, _dtypes.int64)
  sparse_feature_indices = _ops.convert_n_to_tensor(sparse_feature_indices, _dtypes.int64)
  sparse_feature_values = _ops.convert_n_to_tensor(sparse_feature_values, _dtypes.float32)
  dense_features = _ops.convert_n_to_tensor(dense_features, _dtypes.float32)
  example_weights = _ops.convert_to_tensor(example_weights, _dtypes.float32)
  example_labels = _ops.convert_to_tensor(example_labels, _dtypes.float32)
  sparse_indices = _ops.convert_n_to_tensor(sparse_indices, _dtypes.int64)
  sparse_weights = _ops.convert_n_to_tensor(sparse_weights, _dtypes.float32)
  dense_weights = _ops.convert_n_to_tensor(dense_weights, _dtypes.float32)
  example_state_data = _ops.convert_to_tensor(example_state_data, _dtypes.float32)
  _inputs_flat = list(sparse_example_indices) + list(sparse_feature_indices) + list(sparse_feature_values) + list(dense_features) + [example_weights, example_labels] + list(sparse_indices) + list(sparse_weights) + list(dense_weights) + [example_state_data]
  _attrs = ("loss_type", loss_type, "adaptative", adaptative,
  "num_sparse_features", _attr_num_sparse_features,
  "num_sparse_features_with_values", _attr_num_sparse_features_with_values,
  "num_dense_features", _attr_num_dense_features, "l1", l1, "l2", l2,
  "num_loss_partitions", num_loss_partitions, "num_inner_iterations",
  num_inner_iterations)
  _result = _execute.execute(b"SdcaOptimizer", _attr_num_sparse_features +
                             _attr_num_dense_features + 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=ctx,
                             name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "SdcaOptimizer", _inputs_flat, _attrs, _result)
  _result = _result[:1] + [_result[1:1 + _attr_num_sparse_features]] + _result[1 + _attr_num_sparse_features:]
  _result = _result[:2] + [_result[2:]]
  _result = _SdcaOptimizerOutput._make(_result)
  return _result

_SdcaOptimizerV2Output = collections.namedtuple(
    "SdcaOptimizerV2",
    ["out_example_state_data", "out_delta_sparse_weights", "out_delta_dense_weights"])


def sdca_optimizer_v2(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptive=True, name=None):
  r"""Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

  linear models with L1 + L2 regularization. As global optimization objective is
  strongly-convex, the optimizer optimizes the dual objective at each step. The
  optimizer applies each update one example at a time. Examples are sampled
  uniformly, and the optimizer is learning rate free and enjoys linear convergence
  rate.

  [Proximal Stochastic Dual Coordinate Ascent](http://arxiv.org/pdf/1211.2717v1.pdf).<br>
  Shai Shalev-Shwartz, Tong Zhang. 2012

  $$Loss Objective = \sum f_{i} (wx_{i}) + (l2 / 2) * |w|^2 + l1 * |w|$$

  [Adding vs. Averaging in Distributed Primal-Dual Optimization](http://arxiv.org/abs/1502.03508).<br>
  Chenxin Ma, Virginia Smith, Martin Jaggi, Michael I. Jordan,
  Peter Richtarik, Martin Takac. 2015

  [Stochastic Dual Coordinate Ascent with Adaptive Probabilities](https://arxiv.org/abs/1502.08053).<br>
  Dominik Csiba, Zheng Qu, Peter Richtarik. 2015

  Args:
    sparse_example_indices: A list of `Tensor` objects with type `int64`.
      a list of vectors which contain example indices.
    sparse_feature_indices: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
      a list of vectors which contain feature indices.
    sparse_feature_values: A list of `Tensor` objects with type `float32`.
      a list of vectors which contains feature value
      associated with each feature group.
    dense_features: A list of `Tensor` objects with type `float32`.
      a list of matrices which contains the dense feature values.
    example_weights: A `Tensor` of type `float32`.
      a vector which contains the weight associated with each
      example.
    example_labels: A `Tensor` of type `float32`.
      a vector which contains the label/target associated with each
      example.
    sparse_indices: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
      a list of vectors where each value is the indices which has
      corresponding weights in sparse_weights. This field maybe omitted for the
      dense approach.
    sparse_weights: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
      a list of vectors where each value is the weight associated with
      a sparse feature group.
    dense_weights: A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
      a list of vectors where the values are the weights associated
      with a dense feature group.
    example_state_data: A `Tensor` of type `float32`.
      a list of vectors containing the example state data.
    loss_type: A `string` from: `"logistic_loss", "squared_loss", "hinge_loss", "smooth_hinge_loss", "poisson_loss"`.
      Type of the primal loss. Currently SdcaSolver supports logistic,
      squared and hinge losses.
    l1: A `float`. Symmetric l1 regularization strength.
    l2: A `float`. Symmetric l2 regularization strength.
    num_loss_partitions: An `int` that is `>= 1`.
      Number of partitions of the global loss function.
    num_inner_iterations: An `int` that is `>= 1`.
      Number of iterations per mini-batch.
    adaptive: An optional `bool`. Defaults to `True`.
      Whether to use Adaptive SDCA for the inner loop.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (out_example_state_data, out_delta_sparse_weights, out_delta_dense_weights).

    out_example_state_data: A `Tensor` of type `float32`.
    out_delta_sparse_weights: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
    out_delta_dense_weights: A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "SdcaOptimizerV2", name,
        tld.op_callbacks, sparse_example_indices, sparse_feature_indices,
        sparse_feature_values, dense_features, example_weights,
        example_labels, sparse_indices, sparse_weights, dense_weights,
        example_state_data, "loss_type", loss_type, "adaptive", adaptive,
        "l1", l1, "l2", l2, "num_loss_partitions", num_loss_partitions,
        "num_inner_iterations", num_inner_iterations)
      _result = _SdcaOptimizerV2Output._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return sdca_optimizer_v2_eager_fallback(
            sparse_example_indices, sparse_feature_indices,
            sparse_feature_values, dense_features, example_weights,
            example_labels, sparse_indices, sparse_weights, dense_weights,
            example_state_data, loss_type=loss_type, adaptive=adaptive, l1=l1,
            l2=l2, num_loss_partitions=num_loss_partitions,
            num_inner_iterations=num_inner_iterations, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if not isinstance(sparse_example_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_example_indices' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_example_indices)
  _attr_num_sparse_features = len(sparse_example_indices)
  if not isinstance(sparse_feature_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_indices' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_feature_indices)
  if len(sparse_feature_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_feature_indices' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_feature_indices), _attr_num_sparse_features))
  if not isinstance(sparse_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_indices' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_indices)
  if len(sparse_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_indices' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_indices), _attr_num_sparse_features))
  if not isinstance(sparse_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_weights' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_weights)
  if len(sparse_weights) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_weights' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_weights), _attr_num_sparse_features))
  if not isinstance(sparse_feature_values, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_values' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_feature_values)
  _attr_num_sparse_features_with_values = len(sparse_feature_values)
  if not isinstance(dense_features, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_features' argument to "
        "'sdca_optimizer_v2' Op, not %r." % dense_features)
  _attr_num_dense_features = len(dense_features)
  if not isinstance(dense_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_weights' argument to "
        "'sdca_optimizer_v2' Op, not %r." % dense_weights)
  if len(dense_weights) != _attr_num_dense_features:
    raise ValueError(
        "List argument 'dense_weights' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'dense_features'." %
        (len(dense_weights), _attr_num_dense_features))
  loss_type = _execute.make_str(loss_type, "loss_type")
  l1 = _execute.make_float(l1, "l1")
  l2 = _execute.make_float(l2, "l2")
  num_loss_partitions = _execute.make_int(num_loss_partitions, "num_loss_partitions")
  num_inner_iterations = _execute.make_int(num_inner_iterations, "num_inner_iterations")
  if adaptive is None:
    adaptive = True
  adaptive = _execute.make_bool(adaptive, "adaptive")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "SdcaOptimizerV2", sparse_example_indices=sparse_example_indices,
                           sparse_feature_indices=sparse_feature_indices,
                           sparse_feature_values=sparse_feature_values,
                           dense_features=dense_features,
                           example_weights=example_weights,
                           example_labels=example_labels,
                           sparse_indices=sparse_indices,
                           sparse_weights=sparse_weights,
                           dense_weights=dense_weights,
                           example_state_data=example_state_data,
                           loss_type=loss_type, l1=l1, l2=l2,
                           num_loss_partitions=num_loss_partitions,
                           num_inner_iterations=num_inner_iterations,
                           adaptive=adaptive, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("loss_type", _op.get_attr("loss_type"), "adaptive",
              _op._get_attr_bool("adaptive"), "num_sparse_features",
              _op._get_attr_int("num_sparse_features"),
              "num_sparse_features_with_values",
              _op._get_attr_int("num_sparse_features_with_values"),
              "num_dense_features", _op._get_attr_int("num_dense_features"),
              "l1", _op.get_attr("l1"), "l2", _op.get_attr("l2"),
              "num_loss_partitions", _op._get_attr_int("num_loss_partitions"),
              "num_inner_iterations",
              _op._get_attr_int("num_inner_iterations"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "SdcaOptimizerV2", _inputs_flat, _attrs, _result)
  _result = _result[:1] + [_result[1:1 + _attr_num_sparse_features]] + _result[1 + _attr_num_sparse_features:]
  _result = _result[:2] + [_result[2:]]
  _result = _SdcaOptimizerV2Output._make(_result)
  return _result

SdcaOptimizerV2 = tf_export("raw_ops.SdcaOptimizerV2")(_ops.to_raw_op(sdca_optimizer_v2))


def sdca_optimizer_v2_eager_fallback(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptive, name, ctx):
  if not isinstance(sparse_example_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_example_indices' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_example_indices)
  _attr_num_sparse_features = len(sparse_example_indices)
  if not isinstance(sparse_feature_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_indices' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_feature_indices)
  if len(sparse_feature_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_feature_indices' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_feature_indices), _attr_num_sparse_features))
  if not isinstance(sparse_indices, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_indices' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_indices)
  if len(sparse_indices) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_indices' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_indices), _attr_num_sparse_features))
  if not isinstance(sparse_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_weights' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_weights)
  if len(sparse_weights) != _attr_num_sparse_features:
    raise ValueError(
        "List argument 'sparse_weights' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'sparse_example_indices'." %
        (len(sparse_weights), _attr_num_sparse_features))
  if not isinstance(sparse_feature_values, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_feature_values' argument to "
        "'sdca_optimizer_v2' Op, not %r." % sparse_feature_values)
  _attr_num_sparse_features_with_values = len(sparse_feature_values)
  if not isinstance(dense_features, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_features' argument to "
        "'sdca_optimizer_v2' Op, not %r." % dense_features)
  _attr_num_dense_features = len(dense_features)
  if not isinstance(dense_weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_weights' argument to "
        "'sdca_optimizer_v2' Op, not %r." % dense_weights)
  if len(dense_weights) != _attr_num_dense_features:
    raise ValueError(
        "List argument 'dense_weights' to 'sdca_optimizer_v2' Op with length %d "
        "must match length %d of argument 'dense_features'." %
        (len(dense_weights), _attr_num_dense_features))
  loss_type = _execute.make_str(loss_type, "loss_type")
  l1 = _execute.make_float(l1, "l1")
  l2 = _execute.make_float(l2, "l2")
  num_loss_partitions = _execute.make_int(num_loss_partitions, "num_loss_partitions")
  num_inner_iterations = _execute.make_int(num_inner_iterations, "num_inner_iterations")
  if adaptive is None:
    adaptive = True
  adaptive = _execute.make_bool(adaptive, "adaptive")
  sparse_example_indices = _ops.convert_n_to_tensor(sparse_example_indices, _dtypes.int64)
  sparse_feature_indices = _ops.convert_n_to_tensor(sparse_feature_indices, _dtypes.int64)
  sparse_feature_values = _ops.convert_n_to_tensor(sparse_feature_values, _dtypes.float32)
  dense_features = _ops.convert_n_to_tensor(dense_features, _dtypes.float32)
  example_weights = _ops.convert_to_tensor(example_weights, _dtypes.float32)
  example_labels = _ops.convert_to_tensor(example_labels, _dtypes.float32)
  sparse_indices = _ops.convert_n_to_tensor(sparse_indices, _dtypes.int64)
  sparse_weights = _ops.convert_n_to_tensor(sparse_weights, _dtypes.float32)
  dense_weights = _ops.convert_n_to_tensor(dense_weights, _dtypes.float32)
  example_state_data = _ops.convert_to_tensor(example_state_data, _dtypes.float32)
  _inputs_flat = list(sparse_example_indices) + list(sparse_feature_indices) + list(sparse_feature_values) + list(dense_features) + [example_weights, example_labels] + list(sparse_indices) + list(sparse_weights) + list(dense_weights) + [example_state_data]
  _attrs = ("loss_type", loss_type, "adaptive", adaptive,
  "num_sparse_features", _attr_num_sparse_features,
  "num_sparse_features_with_values", _attr_num_sparse_features_with_values,
  "num_dense_features", _attr_num_dense_features, "l1", l1, "l2", l2,
  "num_loss_partitions", num_loss_partitions, "num_inner_iterations",
  num_inner_iterations)
  _result = _execute.execute(b"SdcaOptimizerV2", _attr_num_sparse_features +
                             _attr_num_dense_features + 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=ctx,
                             name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "SdcaOptimizerV2", _inputs_flat, _attrs, _result)
  _result = _result[:1] + [_result[1:1 + _attr_num_sparse_features]] + _result[1 + _attr_num_sparse_features:]
  _result = _result[:2] + [_result[2:]]
  _result = _SdcaOptimizerV2Output._make(_result)
  return _result


@_dispatch.add_dispatch_list
@tf_export(v1=['train.sdca_shrink_l1'])
@deprecated_endpoints('train.sdca_shrink_l1')
def sdca_shrink_l1(weights, l1, l2, name=None):
  r"""Applies L1 regularization shrink step on the parameters.

  Args:
    weights: A list of `Tensor` objects with type mutable `float32`.
      a list of vectors where each value is the weight associated with a
      feature group.
    l1: A `float`. Symmetric l1 regularization strength.
    l2: A `float`.
      Symmetric l2 regularization strength. Should be a positive float.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("sdca_shrink_l1 op does not support eager execution. Arg 'weights' is a ref.")
  # Add nodes to the TensorFlow graph.
  if not isinstance(weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'weights' argument to "
        "'sdca_shrink_l1' Op, not %r." % weights)
  _attr_num_features = len(weights)
  l1 = _execute.make_float(l1, "l1")
  l2 = _execute.make_float(l2, "l2")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "SdcaShrinkL1", weights=weights, l1=l1, l2=l2, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          sdca_shrink_l1, weights=weights, l1=l1, l2=l2, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  return _op
SdcaShrinkL1 = tf_export("raw_ops.SdcaShrinkL1")(_ops.to_raw_op(sdca_shrink_l1))


def sdca_shrink_l1_eager_fallback(weights, l1, l2, name, ctx):
  raise RuntimeError("sdca_shrink_l1 op does not support eager execution. Arg 'weights' is a ref.")
