# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class Resource(_serialization.Model):
    """Describes an Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Alert(Resource):  # pylint: disable=too-many-instance-attributes
    """Security alert.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar version: Schema version.
    :vartype version: str
    :ivar alert_type: Unique identifier for the detection logic (all alert instances from the same
     detection logic will have the same alertType).
    :vartype alert_type: str
    :ivar system_alert_id: Unique identifier for the alert.
    :vartype system_alert_id: str
    :ivar product_component_name: The name of Azure Security Center pricing tier which powering
     this alert. Learn more:
     https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing.
    :vartype product_component_name: str
    :ivar alert_display_name: The display name of the alert.
    :vartype alert_display_name: str
    :ivar description: Description of the suspicious activity that was detected.
    :vartype description: str
    :ivar severity: The risk level of the threat that was detected. Learn more:
     https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified.
     Known values are: "Informational", "Low", "Medium", and "High".
    :vartype severity: str or ~azure.mgmt.security.v2022_01_01.models.AlertSeverity
    :ivar intent: The kill chain related intent behind the alert. For list of supported values, and
     explanations of Azure Security Center's supported kill chain intents. Known values are:
     "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation",
     "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution",
     "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation".
    :vartype intent: str or ~azure.mgmt.security.v2022_01_01.models.Intent
    :ivar start_time_utc: The UTC time of the first event or activity included in the alert in
     ISO8601 format.
    :vartype start_time_utc: ~datetime.datetime
    :ivar end_time_utc: The UTC time of the last event or activity included in the alert in ISO8601
     format.
    :vartype end_time_utc: ~datetime.datetime
    :ivar resource_identifiers: The resource identifiers that can be used to direct the alert to
     the right product exposure group (tenant, workspace, subscription etc.). There can be multiple
     identifiers of different type per alert.
    :vartype resource_identifiers: list[~azure.mgmt.security.v2022_01_01.models.ResourceIdentifier]
    :ivar remediation_steps: Manual action items to take to remediate the alert.
    :vartype remediation_steps: list[str]
    :ivar vendor_name: The name of the vendor that raises the alert.
    :vartype vendor_name: str
    :ivar status: The life cycle status of the alert. Known values are: "Active", "InProgress",
     "Resolved", and "Dismissed".
    :vartype status: str or ~azure.mgmt.security.v2022_01_01.models.AlertStatus
    :ivar extended_links: Links related to the alert.
    :vartype extended_links: list[dict[str, str]]
    :ivar alert_uri: A direct link to the alert page in Azure Portal.
    :vartype alert_uri: str
    :ivar time_generated_utc: The UTC time the alert was generated in ISO8601 format.
    :vartype time_generated_utc: ~datetime.datetime
    :ivar product_name: The name of the product which published this alert (Azure Security Center,
     Azure ATP, Microsoft Defender ATP, O365 ATP, MCAS, and so on).
    :vartype product_name: str
    :ivar processing_end_time_utc: The UTC processing end time of the alert in ISO8601 format.
    :vartype processing_end_time_utc: ~datetime.datetime
    :ivar entities: A list of entities related to the alert.
    :vartype entities: list[~azure.mgmt.security.v2022_01_01.models.AlertEntity]
    :ivar is_incident: This field determines whether the alert is an incident (a compound grouping
     of several alerts) or a single alert.
    :vartype is_incident: bool
    :ivar correlation_key: Key for corelating related alerts. Alerts with the same correlation key
     considered to be related.
    :vartype correlation_key: str
    :ivar extended_properties: Custom properties for the alert.
    :vartype extended_properties: dict[str, str]
    :ivar compromised_entity: The display name of the resource most related to this alert.
    :vartype compromised_entity: str
    :ivar techniques: kill chain related techniques behind the alert.
    :vartype techniques: list[str]
    :ivar sub_techniques: Kill chain related sub-techniques behind the alert.
    :vartype sub_techniques: list[str]
    :ivar supporting_evidence: Changing set of properties depending on the supportingEvidence type.
    :vartype supporting_evidence:
     ~azure.mgmt.security.v2022_01_01.models.AlertPropertiesSupportingEvidence
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "version": {"readonly": True},
        "alert_type": {"readonly": True},
        "system_alert_id": {"readonly": True},
        "product_component_name": {"readonly": True},
        "alert_display_name": {"readonly": True},
        "description": {"readonly": True},
        "severity": {"readonly": True},
        "intent": {"readonly": True},
        "start_time_utc": {"readonly": True},
        "end_time_utc": {"readonly": True},
        "resource_identifiers": {"readonly": True},
        "remediation_steps": {"readonly": True},
        "vendor_name": {"readonly": True},
        "status": {"readonly": True},
        "extended_links": {"readonly": True},
        "alert_uri": {"readonly": True},
        "time_generated_utc": {"readonly": True},
        "product_name": {"readonly": True},
        "processing_end_time_utc": {"readonly": True},
        "entities": {"readonly": True},
        "is_incident": {"readonly": True},
        "correlation_key": {"readonly": True},
        "compromised_entity": {"readonly": True},
        "techniques": {"readonly": True},
        "sub_techniques": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "version": {"key": "properties.version", "type": "str"},
        "alert_type": {"key": "properties.alertType", "type": "str"},
        "system_alert_id": {"key": "properties.systemAlertId", "type": "str"},
        "product_component_name": {"key": "properties.productComponentName", "type": "str"},
        "alert_display_name": {"key": "properties.alertDisplayName", "type": "str"},
        "description": {"key": "properties.description", "type": "str"},
        "severity": {"key": "properties.severity", "type": "str"},
        "intent": {"key": "properties.intent", "type": "str"},
        "start_time_utc": {"key": "properties.startTimeUtc", "type": "iso-8601"},
        "end_time_utc": {"key": "properties.endTimeUtc", "type": "iso-8601"},
        "resource_identifiers": {"key": "properties.resourceIdentifiers", "type": "[ResourceIdentifier]"},
        "remediation_steps": {"key": "properties.remediationSteps", "type": "[str]"},
        "vendor_name": {"key": "properties.vendorName", "type": "str"},
        "status": {"key": "properties.status", "type": "str"},
        "extended_links": {"key": "properties.extendedLinks", "type": "[{str}]"},
        "alert_uri": {"key": "properties.alertUri", "type": "str"},
        "time_generated_utc": {"key": "properties.timeGeneratedUtc", "type": "iso-8601"},
        "product_name": {"key": "properties.productName", "type": "str"},
        "processing_end_time_utc": {"key": "properties.processingEndTimeUtc", "type": "iso-8601"},
        "entities": {"key": "properties.entities", "type": "[AlertEntity]"},
        "is_incident": {"key": "properties.isIncident", "type": "bool"},
        "correlation_key": {"key": "properties.correlationKey", "type": "str"},
        "extended_properties": {"key": "properties.extendedProperties", "type": "{str}"},
        "compromised_entity": {"key": "properties.compromisedEntity", "type": "str"},
        "techniques": {"key": "properties.techniques", "type": "[str]"},
        "sub_techniques": {"key": "properties.subTechniques", "type": "[str]"},
        "supporting_evidence": {"key": "properties.supportingEvidence", "type": "AlertPropertiesSupportingEvidence"},
    }

    def __init__(  # pylint: disable=too-many-locals
        self,
        *,
        extended_properties: Optional[Dict[str, str]] = None,
        supporting_evidence: Optional["_models.AlertPropertiesSupportingEvidence"] = None,
        **kwargs
    ):
        """
        :keyword extended_properties: Custom properties for the alert.
        :paramtype extended_properties: dict[str, str]
        :keyword supporting_evidence: Changing set of properties depending on the supportingEvidence
         type.
        :paramtype supporting_evidence:
         ~azure.mgmt.security.v2022_01_01.models.AlertPropertiesSupportingEvidence
        """
        super().__init__(**kwargs)
        self.version = None
        self.alert_type = None
        self.system_alert_id = None
        self.product_component_name = None
        self.alert_display_name = None
        self.description = None
        self.severity = None
        self.intent = None
        self.start_time_utc = None
        self.end_time_utc = None
        self.resource_identifiers = None
        self.remediation_steps = None
        self.vendor_name = None
        self.status = None
        self.extended_links = None
        self.alert_uri = None
        self.time_generated_utc = None
        self.product_name = None
        self.processing_end_time_utc = None
        self.entities = None
        self.is_incident = None
        self.correlation_key = None
        self.extended_properties = extended_properties
        self.compromised_entity = None
        self.techniques = None
        self.sub_techniques = None
        self.supporting_evidence = supporting_evidence


class AlertEntity(_serialization.Model):
    """Changing set of properties depending on the entity type.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, JSON]
    :ivar type: Type of entity.
    :vartype type: str
    """

    _validation = {
        "type": {"readonly": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, *, additional_properties: Optional[Dict[str, JSON]] = None, **kwargs):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, JSON]
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.type = None


class AlertList(_serialization.Model):
    """List of security alerts.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: describes security alert properties.
    :vartype value: list[~azure.mgmt.security.v2022_01_01.models.Alert]
    :ivar next_link: The URI to fetch the next page.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Alert]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.Alert"]] = None, **kwargs):
        """
        :keyword value: describes security alert properties.
        :paramtype value: list[~azure.mgmt.security.v2022_01_01.models.Alert]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class AlertPropertiesSupportingEvidence(_serialization.Model):
    """Changing set of properties depending on the supportingEvidence type.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, JSON]
    :ivar type: Type of the supportingEvidence.
    :vartype type: str
    """

    _validation = {
        "type": {"readonly": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, *, additional_properties: Optional[Dict[str, JSON]] = None, **kwargs):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, JSON]
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.type = None


class AlertSimulatorRequestProperties(_serialization.Model):
    """Describes properties of an alert simulation request.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    AlertSimulatorBundlesRequestProperties

    All required parameters must be populated in order to send to Azure.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar kind: The kind of alert simulation. Required. "Bundles"
    :vartype kind: str or ~azure.mgmt.security.v2022_01_01.models.KindEnum
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "kind": {"key": "kind", "type": "str"},
    }

    _subtype_map = {"kind": {"Bundles": "AlertSimulatorBundlesRequestProperties"}}

    def __init__(self, *, additional_properties: Optional[Dict[str, Any]] = None, **kwargs):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.kind = None  # type: Optional[str]


class AlertSimulatorBundlesRequestProperties(AlertSimulatorRequestProperties):
    """Simulate alerts according to this bundles.

    All required parameters must be populated in order to send to Azure.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar kind: The kind of alert simulation. Required. "Bundles"
    :vartype kind: str or ~azure.mgmt.security.v2022_01_01.models.KindEnum
    :ivar bundles: Bundles list.
    :vartype bundles: list[str or ~azure.mgmt.security.v2022_01_01.models.BundleType]
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "kind": {"key": "kind", "type": "str"},
        "bundles": {"key": "bundles", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, Any]] = None,
        bundles: Optional[List[Union[str, "_models.BundleType"]]] = None,
        **kwargs
    ):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword bundles: Bundles list.
        :paramtype bundles: list[str or ~azure.mgmt.security.v2022_01_01.models.BundleType]
        """
        super().__init__(additional_properties=additional_properties, **kwargs)
        self.kind = "Bundles"  # type: str
        self.bundles = bundles


class AlertSimulatorRequestBody(_serialization.Model):
    """Alert Simulator request body.

    :ivar properties: Alert Simulator request body data.
    :vartype properties: ~azure.mgmt.security.v2022_01_01.models.AlertSimulatorRequestProperties
    """

    _attribute_map = {
        "properties": {"key": "properties", "type": "AlertSimulatorRequestProperties"},
    }

    def __init__(self, *, properties: Optional["_models.AlertSimulatorRequestProperties"] = None, **kwargs):
        """
        :keyword properties: Alert Simulator request body data.
        :paramtype properties: ~azure.mgmt.security.v2022_01_01.models.AlertSimulatorRequestProperties
        """
        super().__init__(**kwargs)
        self.properties = properties


class ResourceIdentifier(_serialization.Model):
    """A resource identifier for an alert which can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.).

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    AzureResourceIdentifier, LogAnalyticsIdentifier

    All required parameters must be populated in order to send to Azure.

    :ivar type: There can be multiple identifiers of different type per alert, this field specify
     the identifier type. Required. Known values are: "AzureResource" and "LogAnalytics".
    :vartype type: str or ~azure.mgmt.security.v2022_01_01.models.ResourceIdentifierType
    """

    _validation = {
        "type": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
    }

    _subtype_map = {"type": {"AzureResource": "AzureResourceIdentifier", "LogAnalytics": "LogAnalyticsIdentifier"}}

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.type = None  # type: Optional[str]


class AzureResourceIdentifier(ResourceIdentifier):
    """Azure resource identifier.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: There can be multiple identifiers of different type per alert, this field specify
     the identifier type. Required. Known values are: "AzureResource" and "LogAnalytics".
    :vartype type: str or ~azure.mgmt.security.v2022_01_01.models.ResourceIdentifierType
    :ivar azure_resource_id: ARM resource identifier for the cloud resource being alerted on.
    :vartype azure_resource_id: str
    """

    _validation = {
        "type": {"required": True},
        "azure_resource_id": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "azure_resource_id": {"key": "azureResourceId", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.type = "AzureResource"  # type: str
        self.azure_resource_id = None


class CloudErrorBody(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.security.v2022_01_01.models.CloudErrorBody]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.security.v2022_01_01.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class LogAnalyticsIdentifier(ResourceIdentifier):
    """Represents a Log Analytics workspace scope identifier.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: There can be multiple identifiers of different type per alert, this field specify
     the identifier type. Required. Known values are: "AzureResource" and "LogAnalytics".
    :vartype type: str or ~azure.mgmt.security.v2022_01_01.models.ResourceIdentifierType
    :ivar workspace_id: The LogAnalytics workspace id that stores this alert.
    :vartype workspace_id: str
    :ivar workspace_subscription_id: The azure subscription id for the LogAnalytics workspace
     storing this alert.
    :vartype workspace_subscription_id: str
    :ivar workspace_resource_group: The azure resource group for the LogAnalytics workspace storing
     this alert.
    :vartype workspace_resource_group: str
    :ivar agent_id: (optional) The LogAnalytics agent id reporting the event that this alert is
     based on.
    :vartype agent_id: str
    """

    _validation = {
        "type": {"required": True},
        "workspace_id": {"readonly": True},
        "workspace_subscription_id": {
            "readonly": True,
            "pattern": r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$",
        },
        "workspace_resource_group": {"readonly": True},
        "agent_id": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "workspace_id": {"key": "workspaceId", "type": "str"},
        "workspace_subscription_id": {"key": "workspaceSubscriptionId", "type": "str"},
        "workspace_resource_group": {"key": "workspaceResourceGroup", "type": "str"},
        "agent_id": {"key": "agentId", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.type = "LogAnalytics"  # type: str
        self.workspace_id = None
        self.workspace_subscription_id = None
        self.workspace_resource_group = None
        self.agent_id = None
