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


class StorageAccount(Resource):
    """The storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param provisioning_state: Gets the status of the storage account at the
     time the operation was called. Possible values include: 'Creating',
     'ResolvingDNS', 'Succeeded'
    :type provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.storage.v2015_06_15.models.ProvisioningState>`
    :param account_type: Gets the type of the storage account. Possible values
     include: 'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS',
     'Premium_LRS'
    :type account_type: str or :class:`AccountType
     <azure.mgmt.storage.v2015_06_15.models.AccountType>`
    :param primary_endpoints: Gets the URLs that are used to perform a
     retrieval of a public blob, queue, or table object. Note that Standard_ZRS
     and Premium_LRS accounts only return the blob endpoint.
    :type primary_endpoints: :class:`Endpoints
     <azure.mgmt.storage.v2015_06_15.models.Endpoints>`
    :param primary_location: Gets the location of the primary data center for
     the storage account.
    :type primary_location: str
    :param status_of_primary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible
     values include: 'Available', 'Unavailable'
    :type status_of_primary: str or :class:`AccountStatus
     <azure.mgmt.storage.v2015_06_15.models.AccountStatus>`
    :param last_geo_failover_time: Gets the timestamp of the most recent
     instance of a failover to the secondary location. Only the most recent
     timestamp is retained. This element is not returned if there has never
     been a failover instance. Only available if the accountType is
     Standard_GRS or Standard_RAGRS.
    :type last_geo_failover_time: datetime
    :param secondary_location: Gets the location of the geo-replicated
     secondary for the storage account. Only available if the accountType is
     Standard_GRS or Standard_RAGRS.
    :type secondary_location: str
    :param status_of_secondary: Gets the status indicating whether the
     secondary location of the storage account is available or unavailable.
     Only available if the SKU name is Standard_GRS or Standard_RAGRS. Possible
     values include: 'Available', 'Unavailable'
    :type status_of_secondary: str or :class:`AccountStatus
     <azure.mgmt.storage.v2015_06_15.models.AccountStatus>`
    :param creation_time: Gets the creation date and time of the storage
     account in UTC.
    :type creation_time: datetime
    :param custom_domain: Gets the custom domain the user assigned to this
     storage account.
    :type custom_domain: :class:`CustomDomain
     <azure.mgmt.storage.v2015_06_15.models.CustomDomain>`
    :param secondary_endpoints: Gets the URLs that are used to perform a
     retrieval of a public blob, queue, or table object from the secondary
     location of the storage account. Only available if the SKU name is
     Standard_RAGRS.
    :type secondary_endpoints: :class:`Endpoints
     <azure.mgmt.storage.v2015_06_15.models.Endpoints>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'account_type': {'key': 'properties.accountType', 'type': 'AccountType'},
        'primary_endpoints': {'key': 'properties.primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'properties.primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'properties.statusOfPrimary', 'type': 'AccountStatus'},
        'last_geo_failover_time': {'key': 'properties.lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'properties.secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'properties.statusOfSecondary', 'type': 'AccountStatus'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'properties.secondaryEndpoints', 'type': 'Endpoints'},
    }

    def __init__(self, location=None, tags=None, provisioning_state=None, account_type=None, primary_endpoints=None, primary_location=None, status_of_primary=None, last_geo_failover_time=None, secondary_location=None, status_of_secondary=None, creation_time=None, custom_domain=None, secondary_endpoints=None):
        super(StorageAccount, self).__init__(location=location, tags=tags)
        self.provisioning_state = provisioning_state
        self.account_type = account_type
        self.primary_endpoints = primary_endpoints
        self.primary_location = primary_location
        self.status_of_primary = status_of_primary
        self.last_geo_failover_time = last_geo_failover_time
        self.secondary_location = secondary_location
        self.status_of_secondary = status_of_secondary
        self.creation_time = creation_time
        self.custom_domain = custom_domain
        self.secondary_endpoints = secondary_endpoints
