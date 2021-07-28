# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AccessPolicy(msrest.serialization.Model):
    """An Access policy.

    :param start: The date-time the policy is active.
    :type start: str
    :param expiry: The date-time the policy expires.
    :type expiry: str
    :param permission: The permissions for the ACL policy.
    :type permission: str
    """

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'str'},
        'expiry': {'key': 'Expiry', 'type': 'str'},
        'permission': {'key': 'Permission', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccessPolicy, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        self.expiry = kwargs.get('expiry', None)
        self.permission = kwargs.get('permission', None)


class ClearRange(msrest.serialization.Model):
    """ClearRange.

    All required parameters must be populated in order to send to Azure.

    :param start: Required.
    :type start: long
    :param end: Required.
    :type end: long
    """

    _validation = {
        'start': {'required': True},
        'end': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'long', 'xml': {'name': 'Start'}},
        'end': {'key': 'End', 'type': 'long', 'xml': {'name': 'End'}},
    }
    _xml_map = {
        'name': 'ClearRange'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ClearRange, self).__init__(**kwargs)
        self.start = kwargs['start']
        self.end = kwargs['end']


class CopyFileSmbInfo(msrest.serialization.Model):
    """Parameter group.

    :param file_permission_copy_mode: Specifies the option to copy file security descriptor from
     source file or to set it using the value which is defined by the header value of
     x-ms-file-permission or x-ms-file-permission-key. Possible values include: "source",
     "override".
    :type file_permission_copy_mode: str or ~azure.storage.fileshare.models.PermissionCopyModeType
    :param ignore_read_only: Specifies the option to overwrite the target file if it already exists
     and has read-only attribute set.
    :type ignore_read_only: bool
    :param file_attributes: Specifies either the option to copy file attributes from a source
     file(source) to a target file or a list of attributes to set on a target file.
    :type file_attributes: str
    :param file_creation_time: Specifies either the option to copy file creation time from a source
     file(source) to a target file or a time value in ISO 8601 format to set as creation time on a
     target file.
    :type file_creation_time: str
    :param file_last_write_time: Specifies either the option to copy file last write time from a
     source file(source) to a target file or a time value in ISO 8601 format to set as last write
     time on a target file.
    :type file_last_write_time: str
    :param set_archive_attribute: Specifies the option to set archive attribute on a target file.
     True means archive attribute will be set on a target file despite attribute overrides or a
     source file state.
    :type set_archive_attribute: bool
    """

    _attribute_map = {
        'file_permission_copy_mode': {'key': 'filePermissionCopyMode', 'type': 'str'},
        'ignore_read_only': {'key': 'ignoreReadOnly', 'type': 'bool'},
        'file_attributes': {'key': 'fileAttributes', 'type': 'str'},
        'file_creation_time': {'key': 'fileCreationTime', 'type': 'str'},
        'file_last_write_time': {'key': 'fileLastWriteTime', 'type': 'str'},
        'set_archive_attribute': {'key': 'setArchiveAttribute', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CopyFileSmbInfo, self).__init__(**kwargs)
        self.file_permission_copy_mode = kwargs.get('file_permission_copy_mode', None)
        self.ignore_read_only = kwargs.get('ignore_read_only', None)
        self.file_attributes = kwargs.get('file_attributes', None)
        self.file_creation_time = kwargs.get('file_creation_time', None)
        self.file_last_write_time = kwargs.get('file_last_write_time', None)
        self.set_archive_attribute = kwargs.get('set_archive_attribute', None)


class CorsRule(msrest.serialization.Model):
    """CORS is an HTTP feature that enables a web application running under one domain to access resources in another domain. Web browsers implement a security restriction known as same-origin policy that prevents a web page from calling APIs in a different domain; CORS provides a secure way to allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :param allowed_origins: Required. The origin domains that are permitted to make a request
     against the storage service via CORS. The origin domain is the domain from which the request
     originates. Note that the origin must be an exact case-sensitive match with the origin that the
     user age sends to the service. You can also use the wildcard character '*' to allow all origin
     domains to make requests via CORS.
    :type allowed_origins: str
    :param allowed_methods: Required. The methods (HTTP request verbs) that the origin domain may
     use for a CORS request. (comma separated).
    :type allowed_methods: str
    :param allowed_headers: Required. The request headers that the origin domain may specify on the
     CORS request.
    :type allowed_headers: str
    :param exposed_headers: Required. The response headers that may be sent in the response to the
     CORS request and exposed by the browser to the request issuer.
    :type exposed_headers: str
    :param max_age_in_seconds: Required. The maximum amount time that a browser should cache the
     preflight OPTIONS request.
    :type max_age_in_seconds: int
    """

    _validation = {
        'allowed_origins': {'required': True},
        'allowed_methods': {'required': True},
        'allowed_headers': {'required': True},
        'exposed_headers': {'required': True},
        'max_age_in_seconds': {'required': True, 'minimum': 0},
    }

    _attribute_map = {
        'allowed_origins': {'key': 'AllowedOrigins', 'type': 'str'},
        'allowed_methods': {'key': 'AllowedMethods', 'type': 'str'},
        'allowed_headers': {'key': 'AllowedHeaders', 'type': 'str'},
        'exposed_headers': {'key': 'ExposedHeaders', 'type': 'str'},
        'max_age_in_seconds': {'key': 'MaxAgeInSeconds', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CorsRule, self).__init__(**kwargs)
        self.allowed_origins = kwargs['allowed_origins']
        self.allowed_methods = kwargs['allowed_methods']
        self.allowed_headers = kwargs['allowed_headers']
        self.exposed_headers = kwargs['exposed_headers']
        self.max_age_in_seconds = kwargs['max_age_in_seconds']


class DirectoryItem(msrest.serialization.Model):
    """A listed directory item.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param file_id:
    :type file_id: str
    :param properties: File properties.
    :type properties: ~azure.storage.fileshare.models.FileProperty
    :param attributes:
    :type attributes: str
    :param permission_key:
    :type permission_key: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'file_id': {'key': 'FileId', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'FileProperty'},
        'attributes': {'key': 'Attributes', 'type': 'str'},
        'permission_key': {'key': 'PermissionKey', 'type': 'str'},
    }
    _xml_map = {
        'name': 'Directory'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DirectoryItem, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.file_id = kwargs.get('file_id', None)
        self.properties = kwargs.get('properties', None)
        self.attributes = kwargs.get('attributes', None)
        self.permission_key = kwargs.get('permission_key', None)


class FileHTTPHeaders(msrest.serialization.Model):
    """Parameter group.

    :param file_content_type: Sets the MIME content type of the file. The default type is
     'application/octet-stream'.
    :type file_content_type: str
    :param file_content_encoding: Specifies which content encodings have been applied to the file.
    :type file_content_encoding: str
    :param file_content_language: Specifies the natural languages used by this resource.
    :type file_content_language: str
    :param file_cache_control: Sets the file's cache control. The File service stores this value
     but does not use or modify it.
    :type file_cache_control: str
    :param file_content_md5: Sets the file's MD5 hash.
    :type file_content_md5: bytearray
    :param file_content_disposition: Sets the file's Content-Disposition header.
    :type file_content_disposition: str
    """

    _attribute_map = {
        'file_content_type': {'key': 'fileContentType', 'type': 'str'},
        'file_content_encoding': {'key': 'fileContentEncoding', 'type': 'str'},
        'file_content_language': {'key': 'fileContentLanguage', 'type': 'str'},
        'file_cache_control': {'key': 'fileCacheControl', 'type': 'str'},
        'file_content_md5': {'key': 'fileContentMD5', 'type': 'bytearray'},
        'file_content_disposition': {'key': 'fileContentDisposition', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FileHTTPHeaders, self).__init__(**kwargs)
        self.file_content_type = kwargs.get('file_content_type', None)
        self.file_content_encoding = kwargs.get('file_content_encoding', None)
        self.file_content_language = kwargs.get('file_content_language', None)
        self.file_cache_control = kwargs.get('file_cache_control', None)
        self.file_content_md5 = kwargs.get('file_content_md5', None)
        self.file_content_disposition = kwargs.get('file_content_disposition', None)


class FileItem(msrest.serialization.Model):
    """A listed file item.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param file_id:
    :type file_id: str
    :param properties: Required. File properties.
    :type properties: ~azure.storage.fileshare.models.FileProperty
    :param attributes:
    :type attributes: str
    :param permission_key:
    :type permission_key: str
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'file_id': {'key': 'FileId', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'FileProperty'},
        'attributes': {'key': 'Attributes', 'type': 'str'},
        'permission_key': {'key': 'PermissionKey', 'type': 'str'},
    }
    _xml_map = {
        'name': 'File'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FileItem, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.file_id = kwargs.get('file_id', None)
        self.properties = kwargs['properties']
        self.attributes = kwargs.get('attributes', None)
        self.permission_key = kwargs.get('permission_key', None)


class FileProperty(msrest.serialization.Model):
    """File properties.

    All required parameters must be populated in order to send to Azure.

    :param content_length: Required. Content length of the file. This value may not be up-to-date
     since an SMB client may have modified the file locally. The value of Content-Length may not
     reflect that fact until the handle is closed or the op-lock is broken. To retrieve current
     property values, call Get File Properties.
    :type content_length: long
    :param creation_time:
    :type creation_time: ~datetime.datetime
    :param last_access_time:
    :type last_access_time: ~datetime.datetime
    :param last_write_time:
    :type last_write_time: ~datetime.datetime
    :param change_time:
    :type change_time: ~datetime.datetime
    :param last_modified:
    :type last_modified: ~datetime.datetime
    :param etag:
    :type etag: str
    """

    _validation = {
        'content_length': {'required': True},
    }

    _attribute_map = {
        'content_length': {'key': 'Content-Length', 'type': 'long'},
        'creation_time': {'key': 'CreationTime', 'type': 'iso-8601'},
        'last_access_time': {'key': 'LastAccessTime', 'type': 'iso-8601'},
        'last_write_time': {'key': 'LastWriteTime', 'type': 'iso-8601'},
        'change_time': {'key': 'ChangeTime', 'type': 'iso-8601'},
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FileProperty, self).__init__(**kwargs)
        self.content_length = kwargs['content_length']
        self.creation_time = kwargs.get('creation_time', None)
        self.last_access_time = kwargs.get('last_access_time', None)
        self.last_write_time = kwargs.get('last_write_time', None)
        self.change_time = kwargs.get('change_time', None)
        self.last_modified = kwargs.get('last_modified', None)
        self.etag = kwargs.get('etag', None)


class FileRange(msrest.serialization.Model):
    """An Azure Storage file range.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. Start of the range.
    :type start: long
    :param end: Required. End of the range.
    :type end: long
    """

    _validation = {
        'start': {'required': True},
        'end': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'long'},
        'end': {'key': 'End', 'type': 'long'},
    }
    _xml_map = {
        'name': 'Range'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FileRange, self).__init__(**kwargs)
        self.start = kwargs['start']
        self.end = kwargs['end']


class FilesAndDirectoriesListSegment(msrest.serialization.Model):
    """Abstract for entries that can be listed from Directory.

    All required parameters must be populated in order to send to Azure.

    :param directory_items: Required.
    :type directory_items: list[~azure.storage.fileshare.models.DirectoryItem]
    :param file_items: Required.
    :type file_items: list[~azure.storage.fileshare.models.FileItem]
    """

    _validation = {
        'directory_items': {'required': True},
        'file_items': {'required': True},
    }

    _attribute_map = {
        'directory_items': {'key': 'DirectoryItems', 'type': '[DirectoryItem]'},
        'file_items': {'key': 'FileItems', 'type': '[FileItem]'},
    }
    _xml_map = {
        'name': 'Entries'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FilesAndDirectoriesListSegment, self).__init__(**kwargs)
        self.directory_items = kwargs['directory_items']
        self.file_items = kwargs['file_items']


class HandleItem(msrest.serialization.Model):
    """A listed Azure Storage handle item.

    All required parameters must be populated in order to send to Azure.

    :param handle_id: Required. XSMB service handle ID.
    :type handle_id: str
    :param path: Required. File or directory name including full path starting from share root.
    :type path: str
    :param file_id: Required. FileId uniquely identifies the file or directory.
    :type file_id: str
    :param parent_id: ParentId uniquely identifies the parent directory of the object.
    :type parent_id: str
    :param session_id: Required. SMB session ID in context of which the file handle was opened.
    :type session_id: str
    :param client_ip: Required. Client IP that opened the handle.
    :type client_ip: str
    :param open_time: Required. Time when the session that previously opened the handle has last
     been reconnected. (UTC).
    :type open_time: ~datetime.datetime
    :param last_reconnect_time: Time handle was last connected to (UTC).
    :type last_reconnect_time: ~datetime.datetime
    """

    _validation = {
        'handle_id': {'required': True},
        'path': {'required': True},
        'file_id': {'required': True},
        'session_id': {'required': True},
        'client_ip': {'required': True},
        'open_time': {'required': True},
    }

    _attribute_map = {
        'handle_id': {'key': 'HandleId', 'type': 'str'},
        'path': {'key': 'Path', 'type': 'str'},
        'file_id': {'key': 'FileId', 'type': 'str'},
        'parent_id': {'key': 'ParentId', 'type': 'str'},
        'session_id': {'key': 'SessionId', 'type': 'str'},
        'client_ip': {'key': 'ClientIp', 'type': 'str'},
        'open_time': {'key': 'OpenTime', 'type': 'rfc-1123'},
        'last_reconnect_time': {'key': 'LastReconnectTime', 'type': 'rfc-1123'},
    }
    _xml_map = {
        'name': 'Handle'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(HandleItem, self).__init__(**kwargs)
        self.handle_id = kwargs['handle_id']
        self.path = kwargs['path']
        self.file_id = kwargs['file_id']
        self.parent_id = kwargs.get('parent_id', None)
        self.session_id = kwargs['session_id']
        self.client_ip = kwargs['client_ip']
        self.open_time = kwargs['open_time']
        self.last_reconnect_time = kwargs.get('last_reconnect_time', None)


class LeaseAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :param lease_id: If specified, the operation only succeeds if the resource's lease is active
     and matches this ID.
    :type lease_id: str
    """

    _attribute_map = {
        'lease_id': {'key': 'leaseId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LeaseAccessConditions, self).__init__(**kwargs)
        self.lease_id = kwargs.get('lease_id', None)


class ListFilesAndDirectoriesSegmentResponse(msrest.serialization.Model):
    """An enumeration of directories and files.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param share_name: Required.
    :type share_name: str
    :param share_snapshot:
    :type share_snapshot: str
    :param directory_path: Required.
    :type directory_path: str
    :param prefix: Required.
    :type prefix: str
    :param marker:
    :type marker: str
    :param max_results:
    :type max_results: int
    :param segment: Required. Abstract for entries that can be listed from Directory.
    :type segment: ~azure.storage.fileshare.models.FilesAndDirectoriesListSegment
    :param next_marker: Required.
    :type next_marker: str
    :param directory_id:
    :type directory_id: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'share_name': {'required': True},
        'directory_path': {'required': True},
        'prefix': {'required': True},
        'segment': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'attr': True}},
        'share_name': {'key': 'ShareName', 'type': 'str', 'xml': {'attr': True}},
        'share_snapshot': {'key': 'ShareSnapshot', 'type': 'str', 'xml': {'attr': True}},
        'directory_path': {'key': 'DirectoryPath', 'type': 'str', 'xml': {'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'segment': {'key': 'Segment', 'type': 'FilesAndDirectoriesListSegment'},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
        'directory_id': {'key': 'DirectoryId', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListFilesAndDirectoriesSegmentResponse, self).__init__(**kwargs)
        self.service_endpoint = kwargs['service_endpoint']
        self.share_name = kwargs['share_name']
        self.share_snapshot = kwargs.get('share_snapshot', None)
        self.directory_path = kwargs['directory_path']
        self.prefix = kwargs['prefix']
        self.marker = kwargs.get('marker', None)
        self.max_results = kwargs.get('max_results', None)
        self.segment = kwargs['segment']
        self.next_marker = kwargs['next_marker']
        self.directory_id = kwargs.get('directory_id', None)


class ListHandlesResponse(msrest.serialization.Model):
    """An enumeration of handles.

    All required parameters must be populated in order to send to Azure.

    :param handle_list:
    :type handle_list: list[~azure.storage.fileshare.models.HandleItem]
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'handle_list': {'key': 'HandleList', 'type': '[HandleItem]', 'xml': {'name': 'Entries', 'wrapped': True, 'itemsName': 'Handle'}},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListHandlesResponse, self).__init__(**kwargs)
        self.handle_list = kwargs.get('handle_list', None)
        self.next_marker = kwargs['next_marker']


class ListSharesResponse(msrest.serialization.Model):
    """An enumeration of shares.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param prefix:
    :type prefix: str
    :param marker:
    :type marker: str
    :param max_results:
    :type max_results: int
    :param share_items:
    :type share_items: list[~azure.storage.fileshare.models.ShareItemInternal]
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'share_items': {'key': 'ShareItems', 'type': '[ShareItemInternal]', 'xml': {'name': 'Shares', 'wrapped': True, 'itemsName': 'Share'}},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListSharesResponse, self).__init__(**kwargs)
        self.service_endpoint = kwargs['service_endpoint']
        self.prefix = kwargs.get('prefix', None)
        self.marker = kwargs.get('marker', None)
        self.max_results = kwargs.get('max_results', None)
        self.share_items = kwargs.get('share_items', None)
        self.next_marker = kwargs['next_marker']


class Metrics(msrest.serialization.Model):
    """Storage Analytics metrics for file service.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of Storage Analytics to configure.
    :type version: str
    :param enabled: Required. Indicates whether metrics are enabled for the File service.
    :type enabled: bool
    :param include_apis: Indicates whether metrics should generate summary statistics for called
     API operations.
    :type include_apis: bool
    :param retention_policy: The retention policy.
    :type retention_policy: ~azure.storage.fileshare.models.RetentionPolicy
    """

    _validation = {
        'version': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'include_apis': {'key': 'IncludeAPIs', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Metrics, self).__init__(**kwargs)
        self.version = kwargs['version']
        self.enabled = kwargs['enabled']
        self.include_apis = kwargs.get('include_apis', None)
        self.retention_policy = kwargs.get('retention_policy', None)


class RetentionPolicy(msrest.serialization.Model):
    """The retention policy.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Indicates whether a retention policy is enabled for the File service.
     If false, metrics data is retained, and the user is responsible for deleting it.
    :type enabled: bool
    :param days: Indicates the number of days that metrics data should be retained. All data older
     than this value will be deleted. Metrics data is deleted on a best-effort basis after the
     retention period expires.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'maximum': 365, 'minimum': 1},
    }

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'days': {'key': 'Days', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = kwargs['enabled']
        self.days = kwargs.get('days', None)


class ShareFileRangeList(msrest.serialization.Model):
    """The list of file ranges.

    :param ranges:
    :type ranges: list[~azure.storage.fileshare.models.FileRange]
    :param clear_ranges:
    :type clear_ranges: list[~azure.storage.fileshare.models.ClearRange]
    """

    _attribute_map = {
        'ranges': {'key': 'Ranges', 'type': '[FileRange]'},
        'clear_ranges': {'key': 'ClearRanges', 'type': '[ClearRange]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ShareFileRangeList, self).__init__(**kwargs)
        self.ranges = kwargs.get('ranges', None)
        self.clear_ranges = kwargs.get('clear_ranges', None)


class ShareItemInternal(msrest.serialization.Model):
    """A listed Azure Storage share item.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param snapshot:
    :type snapshot: str
    :param deleted:
    :type deleted: bool
    :param version:
    :type version: str
    :param properties: Required. Properties of a share.
    :type properties: ~azure.storage.fileshare.models.SharePropertiesInternal
    :param metadata: Dictionary of :code:`<string>`.
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'snapshot': {'key': 'Snapshot', 'type': 'str'},
        'deleted': {'key': 'Deleted', 'type': 'bool'},
        'version': {'key': 'Version', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'SharePropertiesInternal'},
        'metadata': {'key': 'Metadata', 'type': '{str}'},
    }
    _xml_map = {
        'name': 'Share'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ShareItemInternal, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.snapshot = kwargs.get('snapshot', None)
        self.deleted = kwargs.get('deleted', None)
        self.version = kwargs.get('version', None)
        self.properties = kwargs['properties']
        self.metadata = kwargs.get('metadata', None)


class SharePermission(msrest.serialization.Model):
    """A permission (a security descriptor) at the share level.

    All required parameters must be populated in order to send to Azure.

    :param permission: Required. The permission in the Security Descriptor Definition Language
     (SDDL).
    :type permission: str
    """

    _validation = {
        'permission': {'required': True},
    }

    _attribute_map = {
        'permission': {'key': 'permission', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SharePermission, self).__init__(**kwargs)
        self.permission = kwargs['permission']


class SharePropertiesInternal(msrest.serialization.Model):
    """Properties of a share.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: ~datetime.datetime
    :param etag: Required.
    :type etag: str
    :param quota: Required.
    :type quota: int
    :param provisioned_iops:
    :type provisioned_iops: int
    :param provisioned_ingress_m_bps:
    :type provisioned_ingress_m_bps: int
    :param provisioned_egress_m_bps:
    :type provisioned_egress_m_bps: int
    :param next_allowed_quota_downgrade_time:
    :type next_allowed_quota_downgrade_time: ~datetime.datetime
    :param deleted_time:
    :type deleted_time: ~datetime.datetime
    :param remaining_retention_days:
    :type remaining_retention_days: int
    :param access_tier:
    :type access_tier: str
    :param access_tier_change_time:
    :type access_tier_change_time: ~datetime.datetime
    :param access_tier_transition_state:
    :type access_tier_transition_state: str
    :param lease_status: The current lease status of the share. Possible values include: "locked",
     "unlocked".
    :type lease_status: str or ~azure.storage.fileshare.models.LeaseStatusType
    :param lease_state: Lease state of the share. Possible values include: "available", "leased",
     "expired", "breaking", "broken".
    :type lease_state: str or ~azure.storage.fileshare.models.LeaseStateType
    :param lease_duration: When a share is leased, specifies whether the lease is of infinite or
     fixed duration. Possible values include: "infinite", "fixed".
    :type lease_duration: str or ~azure.storage.fileshare.models.LeaseDurationType
    :param enabled_protocols:
    :type enabled_protocols: str
    :param root_squash:  Possible values include: "NoRootSquash", "RootSquash", "AllSquash".
    :type root_squash: str or ~azure.storage.fileshare.models.ShareRootSquash
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
        'quota': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'quota': {'key': 'Quota', 'type': 'int'},
        'provisioned_iops': {'key': 'ProvisionedIops', 'type': 'int'},
        'provisioned_ingress_m_bps': {'key': 'ProvisionedIngressMBps', 'type': 'int'},
        'provisioned_egress_m_bps': {'key': 'ProvisionedEgressMBps', 'type': 'int'},
        'next_allowed_quota_downgrade_time': {'key': 'NextAllowedQuotaDowngradeTime', 'type': 'rfc-1123'},
        'deleted_time': {'key': 'DeletedTime', 'type': 'rfc-1123'},
        'remaining_retention_days': {'key': 'RemainingRetentionDays', 'type': 'int'},
        'access_tier': {'key': 'AccessTier', 'type': 'str'},
        'access_tier_change_time': {'key': 'AccessTierChangeTime', 'type': 'rfc-1123'},
        'access_tier_transition_state': {'key': 'AccessTierTransitionState', 'type': 'str'},
        'lease_status': {'key': 'LeaseStatus', 'type': 'str'},
        'lease_state': {'key': 'LeaseState', 'type': 'str'},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'str'},
        'enabled_protocols': {'key': 'EnabledProtocols', 'type': 'str'},
        'root_squash': {'key': 'RootSquash', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SharePropertiesInternal, self).__init__(**kwargs)
        self.last_modified = kwargs['last_modified']
        self.etag = kwargs['etag']
        self.quota = kwargs['quota']
        self.provisioned_iops = kwargs.get('provisioned_iops', None)
        self.provisioned_ingress_m_bps = kwargs.get('provisioned_ingress_m_bps', None)
        self.provisioned_egress_m_bps = kwargs.get('provisioned_egress_m_bps', None)
        self.next_allowed_quota_downgrade_time = kwargs.get('next_allowed_quota_downgrade_time', None)
        self.deleted_time = kwargs.get('deleted_time', None)
        self.remaining_retention_days = kwargs.get('remaining_retention_days', None)
        self.access_tier = kwargs.get('access_tier', None)
        self.access_tier_change_time = kwargs.get('access_tier_change_time', None)
        self.access_tier_transition_state = kwargs.get('access_tier_transition_state', None)
        self.lease_status = kwargs.get('lease_status', None)
        self.lease_state = kwargs.get('lease_state', None)
        self.lease_duration = kwargs.get('lease_duration', None)
        self.enabled_protocols = kwargs.get('enabled_protocols', None)
        self.root_squash = kwargs.get('root_squash', None)


class ShareProtocolSettings(msrest.serialization.Model):
    """Protocol settings.

    :param smb: Settings for SMB protocol.
    :type smb: ~azure.storage.fileshare.models.ShareSmbSettings
    """

    _attribute_map = {
        'smb': {'key': 'Smb', 'type': 'ShareSmbSettings'},
    }
    _xml_map = {
        'name': 'ProtocolSettings'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ShareProtocolSettings, self).__init__(**kwargs)
        self.smb = kwargs.get('smb', None)


class ShareSmbSettings(msrest.serialization.Model):
    """Settings for SMB protocol.

    :param multichannel: Settings for SMB Multichannel.
    :type multichannel: ~azure.storage.fileshare.models.SmbMultichannel
    """

    _attribute_map = {
        'multichannel': {'key': 'Multichannel', 'type': 'SmbMultichannel'},
    }
    _xml_map = {
        'name': 'SMB'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ShareSmbSettings, self).__init__(**kwargs)
        self.multichannel = kwargs.get('multichannel', None)


class ShareStats(msrest.serialization.Model):
    """Stats for the share.

    All required parameters must be populated in order to send to Azure.

    :param share_usage_bytes: Required. The approximate size of the data stored in bytes. Note that
     this value may not include all recently created or recently resized files.
    :type share_usage_bytes: int
    """

    _validation = {
        'share_usage_bytes': {'required': True},
    }

    _attribute_map = {
        'share_usage_bytes': {'key': 'ShareUsageBytes', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ShareStats, self).__init__(**kwargs)
        self.share_usage_bytes = kwargs['share_usage_bytes']


class SignedIdentifier(msrest.serialization.Model):
    """Signed identifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A unique id.
    :type id: str
    :param access_policy: The access policy.
    :type access_policy: ~azure.storage.fileshare.models.AccessPolicy
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'access_policy': {'key': 'AccessPolicy', 'type': 'AccessPolicy'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SignedIdentifier, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.access_policy = kwargs.get('access_policy', None)


class SmbMultichannel(msrest.serialization.Model):
    """Settings for SMB multichannel.

    :param enabled: If SMB multichannel is enabled.
    :type enabled: bool
    """

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool'},
    }
    _xml_map = {
        'name': 'Multichannel'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SmbMultichannel, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)


class SourceModifiedAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :param source_if_match_crc64: Specify the crc64 value to operate only on range with a matching
     crc64 checksum.
    :type source_if_match_crc64: bytearray
    :param source_if_none_match_crc64: Specify the crc64 value to operate only on range without a
     matching crc64 checksum.
    :type source_if_none_match_crc64: bytearray
    """

    _attribute_map = {
        'source_if_match_crc64': {'key': 'sourceIfMatchCrc64', 'type': 'bytearray'},
        'source_if_none_match_crc64': {'key': 'sourceIfNoneMatchCrc64', 'type': 'bytearray'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourceModifiedAccessConditions, self).__init__(**kwargs)
        self.source_if_match_crc64 = kwargs.get('source_if_match_crc64', None)
        self.source_if_none_match_crc64 = kwargs.get('source_if_none_match_crc64', None)


class StorageError(msrest.serialization.Model):
    """StorageError.

    :param message:
    :type message: str
    """

    _attribute_map = {
        'message': {'key': 'Message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageError, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)


class StorageServiceProperties(msrest.serialization.Model):
    """Storage service properties.

    :param hour_metrics: A summary of request statistics grouped by API in hourly aggregates for
     files.
    :type hour_metrics: ~azure.storage.fileshare.models.Metrics
    :param minute_metrics: A summary of request statistics grouped by API in minute aggregates for
     files.
    :type minute_metrics: ~azure.storage.fileshare.models.Metrics
    :param cors: The set of CORS rules.
    :type cors: list[~azure.storage.fileshare.models.CorsRule]
    :param protocol: Protocol settings.
    :type protocol: ~azure.storage.fileshare.models.ShareProtocolSettings
    """

    _attribute_map = {
        'hour_metrics': {'key': 'HourMetrics', 'type': 'Metrics'},
        'minute_metrics': {'key': 'MinuteMetrics', 'type': 'Metrics'},
        'cors': {'key': 'Cors', 'type': '[CorsRule]', 'xml': {'wrapped': True}},
        'protocol': {'key': 'Protocol', 'type': 'ShareProtocolSettings'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageServiceProperties, self).__init__(**kwargs)
        self.hour_metrics = kwargs.get('hour_metrics', None)
        self.minute_metrics = kwargs.get('minute_metrics', None)
        self.cors = kwargs.get('cors', None)
        self.protocol = kwargs.get('protocol', None)
