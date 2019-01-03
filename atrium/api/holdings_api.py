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


class HoldingsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_holdings(self, user_guid, **kwargs):  # noqa: E501
        """List holdings  # noqa: E501

        Use this endpoint to read all holdings associated with a specific user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_holdings_with_http_info(user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_holdings_with_http_info(user_guid, **kwargs)  # noqa: E501
            return data

    def list_holdings_with_http_info(self, user_guid, **kwargs):  # noqa: E501
        """List holdings  # noqa: E501

        Use this endpoint to read all holdings associated with a specific user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_with_http_info(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_holdings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_holdings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.mx.atrium.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/holdings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_holdings_by_account(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """List holdings by account  # noqa: E501

        Use this endpoint to read all holdings associated with a specific account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_by_account(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_holdings_by_account_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_holdings_by_account_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_holdings_by_account_with_http_info(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """List holdings by account  # noqa: E501

        Use this endpoint to read all holdings associated with a specific account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_by_account_with_http_info(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_guid', 'user_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_holdings_by_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_guid' is set
        if ('account_guid' not in params or
                params['account_guid'] is None):
            raise ValueError("Missing the required parameter `account_guid` when calling `list_holdings_by_account`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_holdings_by_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_guid' in params:
            path_params['account_guid'] = params['account_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.mx.atrium.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/accounts/{account_guid}/holdings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_holdings_by_member(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List holdings by member  # noqa: E501

        Use this endpoint to read all holdings associated with a specific member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_by_member(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_holdings_by_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_holdings_by_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_holdings_by_member_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List holdings by member  # noqa: E501

        Use this endpoint to read all holdings associated with a specific member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_holdings_by_member_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_holdings_by_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_holdings_by_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_holdings_by_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_guid' in params:
            path_params['member_guid'] = params['member_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.mx.atrium.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/members/{member_guid}/holdings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_holding(self, holding_guid, user_guid, **kwargs):  # noqa: E501
        """Read holding  # noqa: E501

        Use this endpoint to read the attributes of a specific holding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_holding(holding_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str holding_guid: The unique identifier for a `holding`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_holding_with_http_info(holding_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_holding_with_http_info(holding_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_holding_with_http_info(self, holding_guid, user_guid, **kwargs):  # noqa: E501
        """Read holding  # noqa: E501

        Use this endpoint to read the attributes of a specific holding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_holding_with_http_info(holding_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str holding_guid: The unique identifier for a `holding`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: HoldingResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['holding_guid', 'user_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_holding" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'holding_guid' is set
        if ('holding_guid' not in params or
                params['holding_guid'] is None):
            raise ValueError("Missing the required parameter `holding_guid` when calling `read_holding`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_holding`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'holding_guid' in params:
            path_params['holding_guid'] = params['holding_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.mx.atrium.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/holdings/{holding_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
