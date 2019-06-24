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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import ContainerRegistryManagementClientConfiguration
from .operations import RegistriesOperations
from .operations import Operations
from .operations import ReplicationsOperations
from .operations import WebhooksOperations
from .operations import RunsOperations
from .operations import TasksOperations
from . import models


class ContainerRegistryManagementClient(SDKClient):
    """ContainerRegistryManagementClient

    :ivar config: Configuration for client.
    :vartype config: ContainerRegistryManagementClientConfiguration

    :ivar registries: Registries operations
    :vartype registries: azure.mgmt.containerregistry.v2019_05_01.operations.RegistriesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2019_05_01.operations.Operations
    :ivar replications: Replications operations
    :vartype replications: azure.mgmt.containerregistry.v2019_05_01.operations.ReplicationsOperations
    :ivar webhooks: Webhooks operations
    :vartype webhooks: azure.mgmt.containerregistry.v2019_05_01.operations.WebhooksOperations
    :ivar runs: Runs operations
    :vartype runs: azure.mgmt.containerregistry.v2019_05_01.operations.RunsOperations
    :ivar tasks: Tasks operations
    :vartype tasks: azure.mgmt.containerregistry.v2019_05_01.operations.TasksOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ContainerRegistryManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ContainerRegistryManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.registries = RegistriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.replications = ReplicationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.webhooks = WebhooksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.runs = RunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(
            self._client, self.config, self._serialize, self._deserialize)
