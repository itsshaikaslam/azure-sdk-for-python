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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class PolicyAssignmentsOperations(object):
    """PolicyAssignmentsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for the operation. Constant value: "2018-03-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-03-01"

        self.config = config

    def delete(
            self, scope, policy_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a policy assignment.

        This operation deletes a policy assignment, given its name and the
        scope it was created in. The scope of a policy assignment is the part
        of its ID preceding
        '/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.

        :param scope: The scope of the policy assignment. Valid scopes are:
         management group (format:
         '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
         subscription (format: '/subscriptions/{subscriptionId}'), resource
         group (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}',
         or resource (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment to
         delete.
        :type policy_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'policyAssignmentName': self._serialize.url("policy_assignment_name", policy_assignment_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PolicyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'}

    def create(
            self, scope, policy_assignment_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a policy assignment.

        This operation creates or updates a policy assignment with the given
        scope and name. Policy assignments apply to all resources contained
        within their scope. For example, when you assign a policy at resource
        group scope, that policy applies to all resources in the group.

        :param scope: The scope of the policy assignment. Valid scopes are:
         management group (format:
         '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
         subscription (format: '/subscriptions/{subscriptionId}'), resource
         group (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}',
         or resource (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment.
        :type policy_assignment_name: str
        :param parameters: Parameters for the policy assignment.
        :type parameters:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'policyAssignmentName': self._serialize.url("policy_assignment_name", policy_assignment_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'PolicyAssignment')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 201:
            deserialized = self._deserialize('PolicyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'}

    def get(
            self, scope, policy_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Retrieves a policy assignment.

        This operation retrieves a single policy assignment, given its name and
        the scope it was created at.

        :param scope: The scope of the policy assignment. Valid scopes are:
         management group (format:
         '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
         subscription (format: '/subscriptions/{subscriptionId}'), resource
         group (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}',
         or resource (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment to
         get.
        :type policy_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'policyAssignmentName': self._serialize.url("policy_assignment_name", policy_assignment_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PolicyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'}

    def list_for_resource_group(
            self, resource_group_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves all policy assignments that apply to a resource group.

        This operation retrieves the list of all policy assignments associated
        with the given resource group in the given subscription that match the
        optional given $filter. Valid values for $filter are: 'atScope()' or
        'policyDefinitionId eq '{value}''. If $filter is not provided, the
        unfiltered list includes all policy assignments associated with the
        resource group, including those that apply directly or apply from
        containing scopes, as well as any applied to resources contained within
        the resource group. If $filter=atScope() is provided, the returned list
        includes all policy assignments that apply to the resource group, which
        is everything in the unfiltered list except those applied to resources
        contained within the resource group. If $filter=policyDefinitionId eq
        '{value}' is provided, the returned list includes only policy
        assignments that apply to the resource group and assign the policy
        definition whose id is {value}.

        :param resource_group_name: The name of the resource group that
         contains policy assignments.
        :type resource_group_name: str
        :param filter: The filter to apply on the operation. Valid values for
         $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If
         $filter is not provided, no filtering is performed.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PolicyAssignment
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignmentPaged[~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_resource_group.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str', skip_quote=True)
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PolicyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_for_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments'}

    def list_for_resource(
            self, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves all policy assignments that apply to a resource.

        This operation retrieves the list of all policy assignments associated
        with the specified resource in the given resource group and
        subscription that match the optional given $filter. Valid values for
        $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If
        $filter is not provided, the unfiltered list includes all policy
        assignments associated with the resource, including those that apply
        directly or from all containing scopes, as well as any applied to
        resources contained within the resource. If $filter=atScope() is
        provided, the returned list includes all policy assignments that apply
        to the resource, which is everything in the unfiltered list except
        those applied to resources contained within the resource. If
        $filter=policyDefinitionId eq '{value}' is provided, the returned list
        includes only policy assignments that apply to the resource and assign
        the policy definition whose id is {value}. Three parameters plus the
        resource name are used to identify a specific resource. If the resource
        is not part of a parent resource (the more common case), the parent
        resource path should not be provided (or provided as ''). For example a
        web app could be specified as ({resourceProviderNamespace} ==
        'Microsoft.Web', {parentResourcePath} == '', {resourceType} == 'sites',
        {resourceName} == 'MyWebApp'). If the resource is part of a parent
        resource, then all parameters should be provided. For example a virtual
        machine DNS name could be specified as ({resourceProviderNamespace} ==
        'Microsoft.Compute', {parentResourcePath} ==
        'virtualMachines/MyVirtualMachine', {resourceType} == 'domainNames',
        {resourceName} == 'MyComputerName'). A convenient alternative to
        providing the namespace and type name separately is to provide both in
        the {resourceType} parameter, format: ({resourceProviderNamespace} ==
        '', {parentResourcePath} == '', {resourceType} ==
        'Microsoft.Web/sites', {resourceName} == 'MyWebApp').

        :param resource_group_name: The name of the resource group containing
         the resource.
        :type resource_group_name: str
        :param resource_provider_namespace: The namespace of the resource
         provider. For example, the namespace of a virtual machine is
         Microsoft.Compute (from Microsoft.Compute/virtualMachines)
        :type resource_provider_namespace: str
        :param parent_resource_path: The parent resource path. Use empty
         string if there is none.
        :type parent_resource_path: str
        :param resource_type: The resource type name. For example the type
         name of a web app is 'sites' (from Microsoft.Web/sites).
        :type resource_type: str
        :param resource_name: The name of the resource.
        :type resource_name: str
        :param filter: The filter to apply on the operation. Valid values for
         $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If
         $filter is not provided, no filtering is performed.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PolicyAssignment
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignmentPaged[~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_resource.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
                    'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PolicyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_for_resource.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyAssignments'}

    def list(
            self, filter=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves all policy assignments that apply to a subscription.

        This operation retrieves the list of all policy assignments associated
        with the given subscription that match the optional given $filter.
        Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq
        '{value}''. If $filter is not provided, the unfiltered list includes
        all policy assignments associated with the subscription, including
        those that apply directly or from management groups that contain the
        given subscription, as well as any applied to objects contained within
        the subscription. If $filter=atScope() is provided, the returned list
        includes all policy assignments that apply to the subscription, which
        is everything in the unfiltered list except those applied to objects
        contained within the subscription. If $filter=policyDefinitionId eq
        '{value}' is provided, the returned list includes only policy
        assignments that apply to the subscription and assign the policy
        definition whose id is {value}.

        :param filter: The filter to apply on the operation. Valid values for
         $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If
         $filter is not provided, no filtering is performed.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PolicyAssignment
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignmentPaged[~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PolicyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments'}

    def delete_by_id(
            self, policy_assignment_id, custom_headers=None, raw=False, **operation_config):
        """Deletes a policy assignment.

        This operation deletes the policy with the given ID. Policy assignment
        IDs have this format:
        '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
        Valid formats for {scope} are:
        '/providers/Microsoft.Management/managementGroups/{managementGroup}'
        (management group), '/subscriptions/{subscriptionId}' (subscription),
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}'
        (resource group), or
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        (resource).

        :param policy_assignment_id: The ID of the policy assignment to
         delete. Use the format
         '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
        :type policy_assignment_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_by_id.metadata['url']
        path_format_arguments = {
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PolicyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_by_id.metadata = {'url': '/{policyAssignmentId}'}

    def create_by_id(
            self, policy_assignment_id, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a policy assignment.

        This operation creates or updates the policy assignment with the given
        ID. Policy assignments made on a scope apply to all resources contained
        in that scope. For example, when you assign a policy to a resource
        group that policy applies to all resources in the group. Policy
        assignment IDs have this format:
        '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
        Valid scopes are: management group (format:
        '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
        subscription (format: '/subscriptions/{subscriptionId}'), resource
        group (format:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}',
        or resource (format:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'.

        :param policy_assignment_id: The ID of the policy assignment to
         create. Use the format
         '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
        :type policy_assignment_id: str
        :param parameters: Parameters for policy assignment.
        :type parameters:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_by_id.metadata['url']
        path_format_arguments = {
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'PolicyAssignment')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 201:
            deserialized = self._deserialize('PolicyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_by_id.metadata = {'url': '/{policyAssignmentId}'}

    def get_by_id(
            self, policy_assignment_id, custom_headers=None, raw=False, **operation_config):
        """Retrieves the policy assignment with the given ID.

        The operation retrieves the policy assignment with the given ID. Policy
        assignment IDs have this format:
        '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
        Valid scopes are: management group (format:
        '/providers/Microsoft.Management/managementGroups/{managementGroup}'),
        subscription (format: '/subscriptions/{subscriptionId}'), resource
        group (format:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}',
        or resource (format:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'.

        :param policy_assignment_id: The ID of the policy assignment to get.
         Use the format
         '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
        :type policy_assignment_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.resource.policy.v2018_03_01.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PolicyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_id.metadata = {'url': '/{policyAssignmentId}'}
