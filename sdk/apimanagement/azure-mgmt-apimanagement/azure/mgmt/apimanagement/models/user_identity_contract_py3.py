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

from msrest.serialization import Model


class UserIdentityContract(Model):
    """User identity details.

    :param provider: Identity provider name.
    :type provider: str
    :param id: Identifier value within provider.
    :type id: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, id: str=None, **kwargs) -> None:
        super(UserIdentityContract, self).__init__(**kwargs)
        self.provider = provider
        self.id = id
