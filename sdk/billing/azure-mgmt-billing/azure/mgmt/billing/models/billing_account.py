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

from .resource import Resource


class BillingAccount(Resource):
    """A billing account resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar display_name: The billing account name.
    :vartype display_name: str
    :param address: The address associated with billing account.
    :type address: ~azure.mgmt.billing.models.Address
    :ivar agreement_type: The type of agreement. Possible values include:
     'MicrosoftCustomerAgreement', 'EnterpriseAgreement', 'Legacy'
    :vartype agreement_type: str or ~azure.mgmt.billing.models.enum
    :ivar customer_type: The type of customer. Possible values include:
     'Enterprise', 'Individual', 'Partner'
    :vartype customer_type: str or ~azure.mgmt.billing.models.enum
    :param billing_profiles: The billing profiles associated to the billing
     account. By default this is not populated, unless it's specified in
     $expand.
    :type billing_profiles: list[~azure.mgmt.billing.models.BillingProfile]
    :ivar enrollment_details: The details about the associated legacy
     enrollment. By default this is not populated, unless it's specified in
     $expand.
    :vartype enrollment_details: ~azure.mgmt.billing.models.Enrollment
    :param departments: The departments associated to the enrollment.
    :type departments: list[~azure.mgmt.billing.models.Department]
    :param enrollment_accounts: The accounts associated to the enrollment.
    :type enrollment_accounts:
     list[~azure.mgmt.billing.models.EnrollmentAccount]
    :ivar organization_id: Organization id.
    :vartype organization_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'readonly': True},
        'agreement_type': {'readonly': True},
        'customer_type': {'readonly': True},
        'enrollment_details': {'readonly': True},
        'organization_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'address': {'key': 'properties.address', 'type': 'Address'},
        'agreement_type': {'key': 'properties.agreementType', 'type': 'str'},
        'customer_type': {'key': 'properties.customerType', 'type': 'str'},
        'billing_profiles': {'key': 'properties.billingProfiles', 'type': '[BillingProfile]'},
        'enrollment_details': {'key': 'properties.enrollmentDetails', 'type': 'Enrollment'},
        'departments': {'key': 'properties.departments', 'type': '[Department]'},
        'enrollment_accounts': {'key': 'properties.enrollmentAccounts', 'type': '[EnrollmentAccount]'},
        'organization_id': {'key': 'properties.organizationId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BillingAccount, self).__init__(**kwargs)
        self.display_name = None
        self.address = kwargs.get('address', None)
        self.agreement_type = None
        self.customer_type = None
        self.billing_profiles = kwargs.get('billing_profiles', None)
        self.enrollment_details = None
        self.departments = kwargs.get('departments', None)
        self.enrollment_accounts = kwargs.get('enrollment_accounts', None)
        self.organization_id = None
