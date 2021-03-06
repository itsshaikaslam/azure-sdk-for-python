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

from .proxy_resource_py3 import ProxyResource


class RedisFirewallRule(ProxyResource):
    """A firewall rule on a redis cache has a name, and describes a contiguous
    range of IP addresses permitted to connect.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param start_ip: Required. lowest IP address included in the range
    :type start_ip: str
    :param end_ip: Required. highest IP address included in the range
    :type end_ip: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'start_ip': {'required': True},
        'end_ip': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'start_ip': {'key': 'properties.startIP', 'type': 'str'},
        'end_ip': {'key': 'properties.endIP', 'type': 'str'},
    }

    def __init__(self, *, start_ip: str, end_ip: str, **kwargs) -> None:
        super(RedisFirewallRule, self).__init__(**kwargs)
        self.start_ip = start_ip
        self.end_ip = end_ip
