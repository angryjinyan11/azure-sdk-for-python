# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AcquireStorageAccountLock(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether storage account lock is to be acquired for this container or not."""

    ACQUIRE = "Acquire"
    NOT_ACQUIRE = "NotAcquire"


class AzureFileShareType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """File Share type XSync or XSMB."""

    INVALID = "Invalid"
    XSMB = "XSMB"
    X_SYNC = "XSync"


class BackupEngineType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the backup engine."""

    INVALID = "Invalid"
    DPM_BACKUP_ENGINE = "DpmBackupEngine"
    AZURE_BACKUP_SERVER_ENGINE = "AzureBackupServerEngine"


class BackupItemType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of backup items associated with this container."""

    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"


class BackupManagementType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup management type to execute the current job."""

    INVALID = "Invalid"
    AZURE_IAAS_VM = "AzureIaasVM"
    MAB = "MAB"
    DPM = "DPM"
    AZURE_BACKUP_SERVER = "AzureBackupServer"
    AZURE_SQL = "AzureSql"
    AZURE_STORAGE = "AzureStorage"
    AZURE_WORKLOAD = "AzureWorkload"
    DEFAULT_BACKUP = "DefaultBackup"


class BackupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of backup, viz. Full, Differential, Log or CopyOnlyFull."""

    INVALID = "Invalid"
    FULL = "Full"
    DIFFERENTIAL = "Differential"
    LOG = "Log"
    COPY_ONLY_FULL = "CopyOnlyFull"
    INCREMENTAL = "Incremental"
    SNAPSHOT_FULL = "SnapshotFull"
    SNAPSHOT_COPY_ONLY_FULL = "SnapshotCopyOnlyFull"


class ContainerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of container for filter."""

    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"
    HANA_HSR_CONTAINER = "HanaHSRContainer"


class CopyOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Options to resolve copy conflicts."""

    INVALID = "Invalid"
    CREATE_COPY = "CreateCopy"
    SKIP = "Skip"
    OVERWRITE = "Overwrite"
    FAIL_ON_CONFLICT = "FailOnConflict"


class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Create mode to indicate recovery of existing soft deleted data source or creation of new data
    source.
    """

    INVALID = "Invalid"
    DEFAULT = "Default"
    RECOVER = "Recover"


class DataMoveLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DataMove Level."""

    INVALID = "Invalid"
    VAULT = "Vault"
    CONTAINER = "Container"


class DataSourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of workload this item represents."""

    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"


class DayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DayOfWeek."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class DedupState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Vault Dedup state."""

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EncryptionAtRestType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Encryption At Rest Type."""

    INVALID = "Invalid"
    MICROSOFT_MANAGED = "MicrosoftManaged"
    CUSTOMER_MANAGED = "CustomerManaged"


class EnhancedSecurityState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enabled or Disabled."""

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FabricName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the fabric name - Azure or AD."""

    INVALID = "Invalid"
    AZURE = "Azure"


class HealthState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health State for the backed up item."""

    PASSED = "Passed"
    ACTION_REQUIRED = "ActionRequired"
    ACTION_SUGGESTED = "ActionSuggested"
    INVALID = "Invalid"


class HealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health status of protected item."""

    PASSED = "Passed"
    ACTION_REQUIRED = "ActionRequired"
    ACTION_SUGGESTED = "ActionSuggested"
    INVALID = "Invalid"


class HttpStatusCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """HTTP Status Code of the operation."""

    CONTINUE_ENUM = "Continue"
    SWITCHING_PROTOCOLS = "SwitchingProtocols"
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NON_AUTHORITATIVE_INFORMATION = "NonAuthoritativeInformation"
    NO_CONTENT = "NoContent"
    RESET_CONTENT = "ResetContent"
    PARTIAL_CONTENT = "PartialContent"
    MULTIPLE_CHOICES = "MultipleChoices"
    AMBIGUOUS = "Ambiguous"
    MOVED_PERMANENTLY = "MovedPermanently"
    MOVED = "Moved"
    FOUND = "Found"
    REDIRECT = "Redirect"
    SEE_OTHER = "SeeOther"
    REDIRECT_METHOD = "RedirectMethod"
    NOT_MODIFIED = "NotModified"
    USE_PROXY = "UseProxy"
    UNUSED = "Unused"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    REDIRECT_KEEP_VERB = "RedirectKeepVerb"
    BAD_REQUEST = "BadRequest"
    UNAUTHORIZED = "Unauthorized"
    PAYMENT_REQUIRED = "PaymentRequired"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    METHOD_NOT_ALLOWED = "MethodNotAllowed"
    NOT_ACCEPTABLE = "NotAcceptable"
    PROXY_AUTHENTICATION_REQUIRED = "ProxyAuthenticationRequired"
    REQUEST_TIMEOUT = "RequestTimeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTH_REQUIRED = "LengthRequired"
    PRECONDITION_FAILED = "PreconditionFailed"
    REQUEST_ENTITY_TOO_LARGE = "RequestEntityTooLarge"
    REQUEST_URI_TOO_LONG = "RequestUriTooLong"
    UNSUPPORTED_MEDIA_TYPE = "UnsupportedMediaType"
    REQUESTED_RANGE_NOT_SATISFIABLE = "RequestedRangeNotSatisfiable"
    EXPECTATION_FAILED = "ExpectationFailed"
    UPGRADE_REQUIRED = "UpgradeRequired"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    NOT_IMPLEMENTED = "NotImplemented"
    BAD_GATEWAY = "BadGateway"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"
    GATEWAY_TIMEOUT = "GatewayTimeout"
    HTTP_VERSION_NOT_SUPPORTED = "HttpVersionNotSupported"


class IAASVMPolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IAASVMPolicyType."""

    INVALID = "Invalid"
    V1 = "V1"
    V2 = "V2"


class IaasVMSnapshotConsistencyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IaasVMSnapshotConsistencyType."""

    ONLY_CRASH_CONSISTENT = "OnlyCrashConsistent"


class InfrastructureEncryptionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """InfrastructureEncryptionState."""

    INVALID = "Invalid"
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class InquiryStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of protectable item, i.e. InProgress,Succeeded,Failed."""

    INVALID = "Invalid"
    SUCCESS = "Success"
    FAILED = "Failed"


class IntentItemType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of workload this item represents."""

    INVALID = "Invalid"
    SQL_INSTANCE = "SQLInstance"
    SQL_AVAILABILITY_GROUP_CONTAINER = "SQLAvailabilityGroupContainer"


class JobOperationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of operation."""

    INVALID = "Invalid"
    REGISTER = "Register"
    UN_REGISTER = "UnRegister"
    CONFIGURE_BACKUP = "ConfigureBackup"
    BACKUP = "Backup"
    RESTORE = "Restore"
    DISABLE_BACKUP = "DisableBackup"
    DELETE_BACKUP_DATA = "DeleteBackupData"
    CROSS_REGION_RESTORE = "CrossRegionRestore"
    UNDELETE = "Undelete"
    UPDATE_CUSTOMER_MANAGED_KEY = "UpdateCustomerManagedKey"


class JobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the job."""

    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"


class JobSupportedAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """JobSupportedAction."""

    INVALID = "Invalid"
    CANCELLABLE = "Cancellable"
    RETRIABLE = "Retriable"


class LastBackupStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Last backup operation status. Possible values: Healthy, Unhealthy."""

    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    IR_PENDING = "IRPending"


class LastUpdateStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LastUpdateStatus."""

    INVALID = "Invalid"
    NOT_ENABLED = "NotEnabled"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    PARTIALLY_FAILED = "PartiallyFailed"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    INITIALIZED = "Initialized"
    FIRST_INITIALIZATION = "FirstInitialization"


class MabServerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Server type of MAB container."""

    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"


class MonthOfYear(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """MonthOfYear."""

    INVALID = "Invalid"
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"


class OperationStatusValues(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operation status."""

    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class OperationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Re-Do Operation."""

    INVALID = "Invalid"
    REGISTER = "Register"
    REREGISTER = "Reregister"


class OverwriteOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Can Overwrite if Target DataBase already exists."""

    INVALID = "Invalid"
    FAIL_ON_CONFLICT = "FailOnConflict"
    OVERWRITE = "Overwrite"


class PolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of backup policy type."""

    INVALID = "Invalid"
    FULL = "Full"
    DIFFERENTIAL = "Differential"
    LOG = "Log"
    COPY_ONLY_FULL = "CopyOnlyFull"
    INCREMENTAL = "Incremental"
    SNAPSHOT_FULL = "SnapshotFull"
    SNAPSHOT_COPY_ONLY_FULL = "SnapshotCopyOnlyFull"


class PrivateEndpointConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ProtectableContainerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the container. The value of this property for


    #. Compute Azure VM is Microsoft.Compute/virtualMachines
    #. Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines.
    """

    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"
    MICROSOFT_CLASSIC_COMPUTE_VIRTUAL_MACHINES = "Microsoft.ClassicCompute/virtualMachines"
    MICROSOFT_COMPUTE_VIRTUAL_MACHINES = "Microsoft.Compute/virtualMachines"
    AZURE_WORKLOAD_CONTAINER = "AzureWorkloadContainer"


class ProtectedItemHealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health status of the backup item, evaluated based on last heartbeat received."""

    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NOT_REACHABLE = "NotReachable"
    IR_PENDING = "IRPending"


class ProtectedItemState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup state of the backed up item."""

    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"
    BACKUPS_SUSPENDED = "BackupsSuspended"


class ProtectionIntentItemType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """backup protectionIntent type."""

    INVALID = "Invalid"
    AZURE_RESOURCE_ITEM = "AzureResourceItem"
    RECOVERY_SERVICE_VAULT_ITEM = "RecoveryServiceVaultItem"
    AZURE_WORKLOAD_CONTAINER_AUTO_PROTECTION_INTENT = "AzureWorkloadContainerAutoProtectionIntent"
    AZURE_WORKLOAD_AUTO_PROTECTION_INTENT = "AzureWorkloadAutoProtectionIntent"
    AZURE_WORKLOAD_SQL_AUTO_PROTECTION_INTENT = "AzureWorkloadSQLAutoProtectionIntent"


class ProtectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup state of this backup item."""

    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"
    BACKUPS_SUSPENDED = "BackupsSuspended"


class ProtectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether the container is registered or not."""

    INVALID = "Invalid"
    NOT_PROTECTED = "NotProtected"
    PROTECTING = "Protecting"
    PROTECTED = "Protected"
    PROTECTION_FAILED = "ProtectionFailed"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets provisioning state of the private endpoint connection."""

    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    PENDING = "Pending"


class RecoveryMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines whether the current recovery mode is file restore or database restore."""

    INVALID = "Invalid"
    FILE_RECOVERY = "FileRecovery"
    WORKLOAD_RECOVERY = "WorkloadRecovery"
    SNAPSHOT_ATTACH = "SnapshotAttach"
    RECOVERY_USING_SNAPSHOT = "RecoveryUsingSnapshot"
    SNAPSHOT_ATTACH_AND_RECOVER = "SnapshotAttachAndRecover"


class RecoveryPointTierStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Recovery point tier status."""

    INVALID = "Invalid"
    VALID = "Valid"
    DISABLED = "Disabled"
    DELETED = "Deleted"
    REHYDRATED = "Rehydrated"


class RecoveryPointTierType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Recovery point tier type."""

    INVALID = "Invalid"
    INSTANT_RP = "InstantRP"
    HARDENED_RP = "HardenedRP"
    ARCHIVED_RP = "ArchivedRP"


class RecoveryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of this recovery."""

    INVALID = "Invalid"
    ORIGINAL_LOCATION = "OriginalLocation"
    ALTERNATE_LOCATION = "AlternateLocation"
    RESTORE_DISKS = "RestoreDisks"
    OFFLINE = "Offline"


class RehydrationPriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Rehydration Priority."""

    STANDARD = "Standard"
    HIGH = "High"


class ResourceHealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource Health Status."""

    HEALTHY = "Healthy"
    TRANSIENT_DEGRADED = "TransientDegraded"
    PERSISTENT_DEGRADED = "PersistentDegraded"
    TRANSIENT_UNHEALTHY = "TransientUnhealthy"
    PERSISTENT_UNHEALTHY = "PersistentUnhealthy"
    INVALID = "Invalid"


class RestorePointQueryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RestorePoint type."""

    INVALID = "Invalid"
    FULL = "Full"
    LOG = "Log"
    DIFFERENTIAL = "Differential"
    FULL_AND_DIFFERENTIAL = "FullAndDifferential"
    ALL = "All"
    INCREMENTAL = "Incremental"
    SNAPSHOT_FULL = "SnapshotFull"
    SNAPSHOT_COPY_ONLY_FULL = "SnapshotCopyOnlyFull"


class RestorePointType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of restore point."""

    INVALID = "Invalid"
    FULL = "Full"
    LOG = "Log"
    DIFFERENTIAL = "Differential"
    INCREMENTAL = "Incremental"
    SNAPSHOT_FULL = "SnapshotFull"
    SNAPSHOT_COPY_ONLY_FULL = "SnapshotCopyOnlyFull"


class RestoreRequestType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Restore Type (FullShareRestore or ItemLevelRestore)."""

    INVALID = "Invalid"
    FULL_SHARE_RESTORE = "FullShareRestore"
    ITEM_LEVEL_RESTORE = "ItemLevelRestore"


class RetentionDurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Retention duration type of retention policy."""

    INVALID = "Invalid"
    DAYS = "Days"
    WEEKS = "Weeks"
    MONTHS = "Months"
    YEARS = "Years"


class RetentionScheduleFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Retention schedule format type for monthly retention policy."""

    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"


class ScheduleRunType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Frequency of the schedule operation of this policy."""

    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    HOURLY = "Hourly"


class SoftDeleteFeatureState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Soft Delete feature state."""

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    ALWAYS_ON = "AlwaysON"


class SQLDataDirectoryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of data directory mapping."""

    INVALID = "Invalid"
    DATA = "Data"
    LOG = "Log"


class StorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage type."""

    INVALID = "Invalid"
    GEO_REDUNDANT = "GeoRedundant"
    LOCALLY_REDUNDANT = "LocallyRedundant"
    ZONE_REDUNDANT = "ZoneRedundant"
    READ_ACCESS_GEO_ZONE_REDUNDANT = "ReadAccessGeoZoneRedundant"


class StorageTypeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Locked or Unlocked. Once a machine is registered against a resource, the storageTypeState is
    always Locked.
    """

    INVALID = "Invalid"
    LOCKED = "Locked"
    UNLOCKED = "Unlocked"


class SupportStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Support status of feature."""

    INVALID = "Invalid"
    SUPPORTED = "Supported"
    DEFAULT_OFF = "DefaultOFF"
    DEFAULT_ON = "DefaultON"
    NOT_SUPPORTED = "NotSupported"


class TargetDiskNetworkAccessOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network access settings to be used for restored disks."""

    SAME_AS_ON_SOURCE_DISKS = "SameAsOnSourceDisks"
    ENABLE_PRIVATE_ACCESS_FOR_ALL_DISKS = "EnablePrivateAccessForAllDisks"
    ENABLE_PUBLIC_ACCESS_FOR_ALL_DISKS = "EnablePublicAccessForAllDisks"


class TieringMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tiering Mode to control automatic tiering of recovery points. Supported values are:


    #. TierRecommended: Tier all recovery points recommended to be tiered
    #. TierAfter: Tier all recovery points after a fixed period, as specified in duration +
    durationType below.
    #. DoNotTier: Do not tier any recovery points.
    """

    INVALID = "Invalid"
    TIER_RECOMMENDED = "TierRecommended"
    TIER_AFTER = "TierAfter"
    DO_NOT_TIER = "DoNotTier"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup management type for this container."""

    INVALID = "Invalid"
    BACKUP_PROTECTED_ITEM_COUNT_SUMMARY = "BackupProtectedItemCountSummary"
    BACKUP_PROTECTION_CONTAINER_COUNT_SUMMARY = "BackupProtectionContainerCountSummary"


class UsagesUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Unit of the usage."""

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"


class ValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Validation Status."""

    INVALID = "Invalid"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class VaultSubResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """GroupId for the PrivateEndpointConnection - AzureBackup, AzureBackup_secondary or
    AzureSiteRecovery.
    """

    AZURE_BACKUP = "AzureBackup"
    AZURE_BACKUP_SECONDARY = "AzureBackup_secondary"
    AZURE_SITE_RECOVERY = "AzureSiteRecovery"


class WeekOfMonth(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """WeekOfMonth."""

    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
    LAST = "Last"
    INVALID = "Invalid"


class WorkloadItemType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Workload item type of the item for which intent is to be set."""

    INVALID = "Invalid"
    SQL_INSTANCE = "SQLInstance"
    SQL_DATA_BASE = "SQLDataBase"
    SAP_HANA_SYSTEM = "SAPHanaSystem"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_SYSTEM = "SAPAseSystem"
    SAP_ASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"


class WorkloadType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of workload for the backup management."""

    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAP_ASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"


class XcoolState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Vault x-cool state."""

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
