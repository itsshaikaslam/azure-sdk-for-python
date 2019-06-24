# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import MetricNamespace
    from ._models_py3 import MetricNamespaceName
except (SyntaxError, ImportError):
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import MetricNamespace
    from ._models import MetricNamespaceName
from ._paged_models import MetricNamespacePaged

__all__ = [
    'ErrorResponse', 'ErrorResponseException',
    'MetricNamespace',
    'MetricNamespaceName',
    'MetricNamespacePaged',
]
