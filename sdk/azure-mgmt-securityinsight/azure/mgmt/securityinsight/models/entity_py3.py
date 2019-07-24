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


class Entity(Model):
    """Specific entity.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AccountEntity, HostEntity, FileEntity, SecurityAlert,
    FileHashEntity, MalwareEntity, SecurityGroupEntity, AzureResourceEntity,
    CloudApplicationEntity, ProcessEntity, DnsEntity, IpEntity,
    RegistryKeyEntity, RegistryValueEntity, UrlEntity

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'Account': 'AccountEntity', 'Host': 'HostEntity', 'File': 'FileEntity', 'SecurityAlert': 'SecurityAlert', 'FileHash': 'FileHashEntity', 'Malware': 'MalwareEntity', 'SecurityGroup': 'SecurityGroupEntity', 'AzureResource': 'AzureResourceEntity', 'CloudApplication': 'CloudApplicationEntity', 'Process': 'ProcessEntity', 'DnsResolution': 'DnsEntity', 'Ip': 'IpEntity', 'RegistryKey': 'RegistryKeyEntity', 'RegistryValue': 'RegistryValueEntity', 'Url': 'UrlEntity'}
    }

    def __init__(self, **kwargs) -> None:
        super(Entity, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.kind = None
