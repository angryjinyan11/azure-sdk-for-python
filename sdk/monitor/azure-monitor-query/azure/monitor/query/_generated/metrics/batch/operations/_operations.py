# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_metrics_batch_batch_request(
    subscription_id: str,
    *,
    metricnamespace: str,
    metricnames: List[str],
    starttime: Optional[str] = None,
    endtime: Optional[str] = None,
    interval: Optional[datetime.timedelta] = None,
    aggregation: Optional[str] = None,
    top: Optional[int] = None,
    orderby: Optional[str] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-05-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/metrics:getBatch"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if starttime is not None:
        _params["starttime"] = _SERIALIZER.query("starttime", starttime, "str")
    if endtime is not None:
        _params["endtime"] = _SERIALIZER.query("endtime", endtime, "str")
    if interval is not None:
        _params["interval"] = _SERIALIZER.query("interval", interval, "duration")
    _params["metricnamespace"] = _SERIALIZER.query("metricnamespace", metricnamespace, "str")
    _params["metricnames"] = _SERIALIZER.query("metricnames", metricnames, "[str]", div=",")
    if aggregation is not None:
        _params["aggregation"] = _SERIALIZER.query("aggregation", aggregation, "str")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if orderby is not None:
        _params["orderby"] = _SERIALIZER.query("orderby", orderby, "str")
    if filter is not None:
        _params["filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class MetricsBatchOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~monitor_batch_metrics_client.MonitorBatchMetricsClient`'s
        :attr:`metrics_batch` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def batch(
        self,
        subscription_id: str,
        resource_ids: JSON,
        *,
        metricnamespace: str,
        metricnames: List[str],
        starttime: Optional[str] = None,
        endtime: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        filter: Optional[str] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> JSON:
        """Lists the metric values for multiple resources.

        :param subscription_id: The subscription identifier for the resources in this batch. Required.
        :type subscription_id: str
        :param resource_ids: The comma separated list of resource IDs to query metrics for. Required.
        :type resource_ids: JSON
        :keyword metricnamespace: Metric namespace that contains the requested metric names. Required.
        :paramtype metricnamespace: str
        :keyword metricnames: The names of the metrics (comma separated) to retrieve. Required.
        :paramtype metricnames: list[str]
        :keyword starttime: The start time of the query. It is a string in the format
         'yyyy-MM-ddTHH:mm:ss.fffZ'. If you have specified the endtime parameter, then this parameter is
         required.
         If only starttime is specified, then endtime defaults to the current time.
         If no time interval is specified, the default is 1 hour. Default value is None.
        :paramtype starttime: str
        :keyword endtime: The end time of the query. It is a string in the format
         'yyyy-MM-ddTHH:mm:ss.fffZ'. Default value is None.
        :paramtype endtime: str
        :keyword interval: The interval (i.e. timegrain) of the query.
         *Examples: PT15M, PT1H, P1D*. Default value is None.
        :paramtype interval: ~datetime.timedelta
        :keyword aggregation: The list of aggregation types (comma separated) to retrieve.
         *Examples: average, minimum, maximum*. Default value is None.
        :paramtype aggregation: str
        :keyword top: The maximum number of records to retrieve per resource ID in the request.
         Valid only if filter is specified.
         Defaults to 10. Default value is None.
        :paramtype top: int
        :keyword orderby: The aggregation to use for sorting results and the direction of the sort.
         Only one order can be specified.
         *Examples: sum asc*. Default value is None.
        :paramtype orderby: str
        :keyword filter: The filter is used to reduce the set of metric data
         returned.:code:`<br>`Example::code:`<br>`Metric contains metadata A, B and C.:code:`<br>`-
         Return all time series of C where A = a1 and B = b1 or b2:code:`<br>`\ **filter=A eq ‘a1’ and B
         eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**\ :code:`<br>`- Invalid variant::code:`<br>`\ **filter=A eq
         ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**\ :code:`<br>`This is invalid because the logical
         or operator cannot separate two different metadata names.:code:`<br>`- Return all time series
         where A = a1, B = b1 and C = c1::code:`<br>`\ **filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**\
         :code:`<br>`- Return all time series where A = a1:code:`<br>`\ **filter=A eq ‘a1’ and B eq ‘\
         *’ and C eq ‘*\ ’**. Default value is None.
        :paramtype filter: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_ids = {
                    "resourceids": [
                        "str"  # Optional. The list of resource IDs to query metrics for.
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "values": [
                        {
                            "endtime": "str",  # The end time, in datetime format, for
                              which the data was retrieved. Required.
                            "starttime": "str",  # The start time, in datetime format,
                              for which the data was retrieved. Required.
                            "value": [
                                {
                                    "id": "str",  # the metric Id. Required.
                                    "name": {
                                        "value": "str",  # The invariant
                                          value. Required.
                                        "localizedValue": "str"  # Optional.
                                          The display name.
                                    },
                                    "timeseries": [
                                        {
                                            "data": [
                                                {
                                                    "timeStamp":
                                                      "2020-02-20 00:00:00",  # The timestamp for the
                                                      metric value in ISO 8601 format. Required.
                                                    "average":
                                                      0.0,  # Optional. The average value in the time
                                                      range.
                                                    "count": 0.0,
                                                      # Optional. The number of samples in the time
                                                      range. Can be used to determine the number of
                                                      values that contributed to the average value.
                                                    "maximum":
                                                      0.0,  # Optional. The greatest value in the time
                                                      range.
                                                    "minimum":
                                                      0.0,  # Optional. The least value in the time
                                                      range.
                                                    "total": 0.0
                                                      # Optional. The sum of all of the values in the
                                                      time range.
                                                }
                                            ],
                                            "metadatavalues": [
                                                {
                                                    "name": {
                "value": "str",  # The invariant value.
                                                          Required.
                "localizedValue": "str"  # Optional. The
                                                          display name.
                                                    },
                                                    "value":
                                                      "str"  # Optional. The value of the metadata.
                                                }
                                            ]
                                        }
                                    ],
                                    "type": "str",  # the resource type of the
                                      metric resource. Required.
                                    "unit": "str",  # The unit of the metric.
                                      Required. Known values are: "Count", "Bytes", "Seconds",
                                      "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds",
                                      "ByteSeconds", "Unspecified", "Cores", "MilliCores", "NanoCores",
                                      and "BitsPerSecond".
                                    "displayDescription": "str",  # Optional.
                                      Detailed description of this metric.
                                    "errorCode": "str",  # Optional. 'Success' or
                                      the error details on query failures for this metric.
                                    "errorMessage": "str"  # Optional. Error
                                      message encountered querying this specific metric.
                                }
                            ],
                            "interval": "1 day, 0:00:00",  # Optional. The interval
                              (window size) for which the metric data was returned in. Follows the
                              IS8601/RFC3339 duration format (e.g. 'P1D' for 1 day). This may be
                              adjusted in the future and returned back from what was originally
                              requested.  This is not present if a metadata request was made.
                            "namespace": "str",  # Optional. The namespace of the metrics
                              been queried.
                            "resourceid": "str",  # Optional. The resource that has been
                              queried for metrics.
                            "resourceregion": "str"  # Optional. The region of the
                              resource been queried for metrics.
                        }
                    ]
                }
        """

    @overload
    def batch(
        self,
        subscription_id: str,
        resource_ids: IO,
        *,
        metricnamespace: str,
        metricnames: List[str],
        starttime: Optional[str] = None,
        endtime: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        filter: Optional[str] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> JSON:
        """Lists the metric values for multiple resources.

        :param subscription_id: The subscription identifier for the resources in this batch. Required.
        :type subscription_id: str
        :param resource_ids: The comma separated list of resource IDs to query metrics for. Required.
        :type resource_ids: IO
        :keyword metricnamespace: Metric namespace that contains the requested metric names. Required.
        :paramtype metricnamespace: str
        :keyword metricnames: The names of the metrics (comma separated) to retrieve. Required.
        :paramtype metricnames: list[str]
        :keyword starttime: The start time of the query. It is a string in the format
         'yyyy-MM-ddTHH:mm:ss.fffZ'. If you have specified the endtime parameter, then this parameter is
         required.
         If only starttime is specified, then endtime defaults to the current time.
         If no time interval is specified, the default is 1 hour. Default value is None.
        :paramtype starttime: str
        :keyword endtime: The end time of the query. It is a string in the format
         'yyyy-MM-ddTHH:mm:ss.fffZ'. Default value is None.
        :paramtype endtime: str
        :keyword interval: The interval (i.e. timegrain) of the query.
         *Examples: PT15M, PT1H, P1D*. Default value is None.
        :paramtype interval: ~datetime.timedelta
        :keyword aggregation: The list of aggregation types (comma separated) to retrieve.
         *Examples: average, minimum, maximum*. Default value is None.
        :paramtype aggregation: str
        :keyword top: The maximum number of records to retrieve per resource ID in the request.
         Valid only if filter is specified.
         Defaults to 10. Default value is None.
        :paramtype top: int
        :keyword orderby: The aggregation to use for sorting results and the direction of the sort.
         Only one order can be specified.
         *Examples: sum asc*. Default value is None.
        :paramtype orderby: str
        :keyword filter: The filter is used to reduce the set of metric data
         returned.:code:`<br>`Example::code:`<br>`Metric contains metadata A, B and C.:code:`<br>`-
         Return all time series of C where A = a1 and B = b1 or b2:code:`<br>`\ **filter=A eq ‘a1’ and B
         eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**\ :code:`<br>`- Invalid variant::code:`<br>`\ **filter=A eq
         ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**\ :code:`<br>`This is invalid because the logical
         or operator cannot separate two different metadata names.:code:`<br>`- Return all time series
         where A = a1, B = b1 and C = c1::code:`<br>`\ **filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**\
         :code:`<br>`- Return all time series where A = a1:code:`<br>`\ **filter=A eq ‘a1’ and B eq ‘\
         *’ and C eq ‘*\ ’**. Default value is None.
        :paramtype filter: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "values": [
                        {
                            "endtime": "str",  # The end time, in datetime format, for
                              which the data was retrieved. Required.
                            "starttime": "str",  # The start time, in datetime format,
                              for which the data was retrieved. Required.
                            "value": [
                                {
                                    "id": "str",  # the metric Id. Required.
                                    "name": {
                                        "value": "str",  # The invariant
                                          value. Required.
                                        "localizedValue": "str"  # Optional.
                                          The display name.
                                    },
                                    "timeseries": [
                                        {
                                            "data": [
                                                {
                                                    "timeStamp":
                                                      "2020-02-20 00:00:00",  # The timestamp for the
                                                      metric value in ISO 8601 format. Required.
                                                    "average":
                                                      0.0,  # Optional. The average value in the time
                                                      range.
                                                    "count": 0.0,
                                                      # Optional. The number of samples in the time
                                                      range. Can be used to determine the number of
                                                      values that contributed to the average value.
                                                    "maximum":
                                                      0.0,  # Optional. The greatest value in the time
                                                      range.
                                                    "minimum":
                                                      0.0,  # Optional. The least value in the time
                                                      range.
                                                    "total": 0.0
                                                      # Optional. The sum of all of the values in the
                                                      time range.
                                                }
                                            ],
                                            "metadatavalues": [
                                                {
                                                    "name": {
                "value": "str",  # The invariant value.
                                                          Required.
                "localizedValue": "str"  # Optional. The
                                                          display name.
                                                    },
                                                    "value":
                                                      "str"  # Optional. The value of the metadata.
                                                }
                                            ]
                                        }
                                    ],
                                    "type": "str",  # the resource type of the
                                      metric resource. Required.
                                    "unit": "str",  # The unit of the metric.
                                      Required. Known values are: "Count", "Bytes", "Seconds",
                                      "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds",
                                      "ByteSeconds", "Unspecified", "Cores", "MilliCores", "NanoCores",
                                      and "BitsPerSecond".
                                    "displayDescription": "str",  # Optional.
                                      Detailed description of this metric.
                                    "errorCode": "str",  # Optional. 'Success' or
                                      the error details on query failures for this metric.
                                    "errorMessage": "str"  # Optional. Error
                                      message encountered querying this specific metric.
                                }
                            ],
                            "interval": "1 day, 0:00:00",  # Optional. The interval
                              (window size) for which the metric data was returned in. Follows the
                              IS8601/RFC3339 duration format (e.g. 'P1D' for 1 day). This may be
                              adjusted in the future and returned back from what was originally
                              requested.  This is not present if a metadata request was made.
                            "namespace": "str",  # Optional. The namespace of the metrics
                              been queried.
                            "resourceid": "str",  # Optional. The resource that has been
                              queried for metrics.
                            "resourceregion": "str"  # Optional. The region of the
                              resource been queried for metrics.
                        }
                    ]
                }
        """

    @distributed_trace
    def batch(
        self,
        subscription_id: str,
        resource_ids: Union[JSON, IO],
        *,
        metricnamespace: str,
        metricnames: List[str],
        starttime: Optional[str] = None,
        endtime: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> JSON:
        """Lists the metric values for multiple resources.

        :param subscription_id: The subscription identifier for the resources in this batch. Required.
        :type subscription_id: str
        :param resource_ids: The comma separated list of resource IDs to query metrics for. Is either a
         JSON type or a IO type. Required.
        :type resource_ids: JSON or IO
        :keyword metricnamespace: Metric namespace that contains the requested metric names. Required.
        :paramtype metricnamespace: str
        :keyword metricnames: The names of the metrics (comma separated) to retrieve. Required.
        :paramtype metricnames: list[str]
        :keyword starttime: The start time of the query. It is a string in the format
         'yyyy-MM-ddTHH:mm:ss.fffZ'. If you have specified the endtime parameter, then this parameter is
         required.
         If only starttime is specified, then endtime defaults to the current time.
         If no time interval is specified, the default is 1 hour. Default value is None.
        :paramtype starttime: str
        :keyword endtime: The end time of the query. It is a string in the format
         'yyyy-MM-ddTHH:mm:ss.fffZ'. Default value is None.
        :paramtype endtime: str
        :keyword interval: The interval (i.e. timegrain) of the query.
         *Examples: PT15M, PT1H, P1D*. Default value is None.
        :paramtype interval: ~datetime.timedelta
        :keyword aggregation: The list of aggregation types (comma separated) to retrieve.
         *Examples: average, minimum, maximum*. Default value is None.
        :paramtype aggregation: str
        :keyword top: The maximum number of records to retrieve per resource ID in the request.
         Valid only if filter is specified.
         Defaults to 10. Default value is None.
        :paramtype top: int
        :keyword orderby: The aggregation to use for sorting results and the direction of the sort.
         Only one order can be specified.
         *Examples: sum asc*. Default value is None.
        :paramtype orderby: str
        :keyword filter: The filter is used to reduce the set of metric data
         returned.:code:`<br>`Example::code:`<br>`Metric contains metadata A, B and C.:code:`<br>`-
         Return all time series of C where A = a1 and B = b1 or b2:code:`<br>`\ **filter=A eq ‘a1’ and B
         eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**\ :code:`<br>`- Invalid variant::code:`<br>`\ **filter=A eq
         ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**\ :code:`<br>`This is invalid because the logical
         or operator cannot separate two different metadata names.:code:`<br>`- Return all time series
         where A = a1, B = b1 and C = c1::code:`<br>`\ **filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**\
         :code:`<br>`- Return all time series where A = a1:code:`<br>`\ **filter=A eq ‘a1’ and B eq ‘\
         *’ and C eq ‘*\ ’**. Default value is None.
        :paramtype filter: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_ids = {
                    "resourceids": [
                        "str"  # Optional. The list of resource IDs to query metrics for.
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "values": [
                        {
                            "endtime": "str",  # The end time, in datetime format, for
                              which the data was retrieved. Required.
                            "starttime": "str",  # The start time, in datetime format,
                              for which the data was retrieved. Required.
                            "value": [
                                {
                                    "id": "str",  # the metric Id. Required.
                                    "name": {
                                        "value": "str",  # The invariant
                                          value. Required.
                                        "localizedValue": "str"  # Optional.
                                          The display name.
                                    },
                                    "timeseries": [
                                        {
                                            "data": [
                                                {
                                                    "timeStamp":
                                                      "2020-02-20 00:00:00",  # The timestamp for the
                                                      metric value in ISO 8601 format. Required.
                                                    "average":
                                                      0.0,  # Optional. The average value in the time
                                                      range.
                                                    "count": 0.0,
                                                      # Optional. The number of samples in the time
                                                      range. Can be used to determine the number of
                                                      values that contributed to the average value.
                                                    "maximum":
                                                      0.0,  # Optional. The greatest value in the time
                                                      range.
                                                    "minimum":
                                                      0.0,  # Optional. The least value in the time
                                                      range.
                                                    "total": 0.0
                                                      # Optional. The sum of all of the values in the
                                                      time range.
                                                }
                                            ],
                                            "metadatavalues": [
                                                {
                                                    "name": {
                "value": "str",  # The invariant value.
                                                          Required.
                "localizedValue": "str"  # Optional. The
                                                          display name.
                                                    },
                                                    "value":
                                                      "str"  # Optional. The value of the metadata.
                                                }
                                            ]
                                        }
                                    ],
                                    "type": "str",  # the resource type of the
                                      metric resource. Required.
                                    "unit": "str",  # The unit of the metric.
                                      Required. Known values are: "Count", "Bytes", "Seconds",
                                      "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds",
                                      "ByteSeconds", "Unspecified", "Cores", "MilliCores", "NanoCores",
                                      and "BitsPerSecond".
                                    "displayDescription": "str",  # Optional.
                                      Detailed description of this metric.
                                    "errorCode": "str",  # Optional. 'Success' or
                                      the error details on query failures for this metric.
                                    "errorMessage": "str"  # Optional. Error
                                      message encountered querying this specific metric.
                                }
                            ],
                            "interval": "1 day, 0:00:00",  # Optional. The interval
                              (window size) for which the metric data was returned in. Follows the
                              IS8601/RFC3339 duration format (e.g. 'P1D' for 1 day). This may be
                              adjusted in the future and returned back from what was originally
                              requested.  This is not present if a metadata request was made.
                            "namespace": "str",  # Optional. The namespace of the metrics
                              been queried.
                            "resourceid": "str",  # Optional. The resource that has been
                              queried for metrics.
                            "resourceregion": "str"  # Optional. The region of the
                              resource been queried for metrics.
                        }
                    ]
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(resource_ids, (IOBase, bytes)):
            _content = resource_ids
        else:
            _json = resource_ids

        _request = build_metrics_batch_batch_request(
            subscription_id=subscription_id,
            metricnamespace=metricnamespace,
            metricnames=metricnames,
            starttime=starttime,
            endtime=endtime,
            interval=interval,
            aggregation=aggregation,
            top=top,
            orderby=orderby,
            filter=filter,
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore
