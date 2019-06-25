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

from enum import Enum


class DirectoryType(str, Enum):

    active_directory = "ActiveDirectory"


class DaysOfWeek(str, Enum):

    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class OSType(str, Enum):

    windows = "Windows"
    linux = "Linux"


class Tier(str, Enum):

    standard = "Standard"
    premium = "Premium"


class JsonWebKeyEncryptionAlgorithm(str, Enum):

    rsa_oaep = "RSA-OAEP"
    rsa_oaep_256 = "RSA-OAEP-256"
    rsa1_5 = "RSA1_5"


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"


class HDInsightClusterProvisioningState(str, Enum):

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    canceled = "Canceled"
    deleting = "Deleting"


class AsyncOperationState(str, Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
