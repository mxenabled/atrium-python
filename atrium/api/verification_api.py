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


class VerificationApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_account_numbers(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read account numbers  # noqa: E501

        Use this endpoint to check whether account and routing numbers are available for accounts associated with a particular member. It returns the account_numbers object, which contains account and routing number data for each account associated with the member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_numbers(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountNumbersResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_account_numbers_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_account_numbers_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_account_numbers_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read account numbers  # noqa: E501

        Use this endpoint to check whether account and routing numbers are available for accounts associated with a particular member. It returns the account_numbers object, which contains account and routing number data for each account associated with the member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_numbers_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountNumbersResponseBody
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
                    " to method list_account_numbers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_account_numbers`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_account_numbers`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/account_numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountNumbersResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_account_numbers_by_account(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """Read account numbers by account GUID  # noqa: E501

        Use this endpoint to check whether account and routing numbers are available for a specific account. It returns the account_numbers object, which contains account and routing number data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_numbers_by_account(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountNumbersResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_account_numbers_by_account_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_account_numbers_by_account_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_account_numbers_by_account_with_http_info(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """Read account numbers by account GUID  # noqa: E501

        Use this endpoint to check whether account and routing numbers are available for a specific account. It returns the account_numbers object, which contains account and routing number data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_numbers_by_account_with_http_info(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountNumbersResponseBody
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
                    " to method list_account_numbers_by_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_guid' is set
        if ('account_guid' not in params or
                params['account_guid'] is None):
            raise ValueError("Missing the required parameter `account_guid` when calling `list_account_numbers_by_account`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_account_numbers_by_account`")  # noqa: E501

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
            '/users/{user_guid}/accounts/{account_guid}/account_numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountNumbersResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_member(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Verify  # noqa: E501

        The verify endpoint begins a verification process for a member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_member(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def verify_member_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Verify  # noqa: E501

        The verify endpoint begins a verification process for a member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_member_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: MemberResponseBody
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
                    " to method verify_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `verify_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `verify_member`")  # noqa: E501

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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/members/{member_guid}/verify', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MemberResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
