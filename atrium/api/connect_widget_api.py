# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from atrium.api_client import ApiClient


class ConnectWidgetApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_connect_widget(self, user_guid, body, **kwargs):  # noqa: E501
        """Embedding in a website  # noqa: E501

        This endpoint will return a URL for an embeddable version of MX Connect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connect_widget(user_guid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param ConnectWidgetRequestBody body: Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) (required)
        :return: ConnectWidgetResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connect_widget_with_http_info(user_guid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connect_widget_with_http_info(user_guid, body, **kwargs)  # noqa: E501
            return data

    def get_connect_widget_with_http_info(self, user_guid, body, **kwargs):  # noqa: E501
        """Embedding in a website  # noqa: E501

        This endpoint will return a URL for an embeddable version of MX Connect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connect_widget_with_http_info(user_guid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param ConnectWidgetRequestBody body: Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) (required)
        :return: ConnectWidgetResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_guid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connect_widget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `get_connect_widget`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_connect_widget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.mx.atrium.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/connect_widget_url', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWidgetResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
