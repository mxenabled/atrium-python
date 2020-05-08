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


class MembersApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aggregate_member(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Aggregate member  # noqa: E501

        Calling this endpoint initiates an aggregation event for the member. This brings in the latest account and transaction data from the connected institution. If this data has recently been updated, MX may not initiate an aggregation event.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_member(member_guid, user_guid, async_req=True)
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
            return self.aggregate_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def aggregate_member_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Aggregate member  # noqa: E501

        Calling this endpoint initiates an aggregation event for the member. This brings in the latest account and transaction data from the connected institution. If this data has recently been updated, MX may not initiate an aggregation event.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_member_with_http_info(member_guid, user_guid, async_req=True)
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
                    " to method aggregate_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `aggregate_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `aggregate_member`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/aggregate', 'POST',
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

    def aggregate_member_balances(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Aggregate member account balances  # noqa: E501

        This endpoint operates much like the _aggregate member_ endpoint except that it gathers only account balance information; it does not gather any transaction data at all.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_member_balances(member_guid, user_guid, async_req=True)
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
            return self.aggregate_member_balances_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_member_balances_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def aggregate_member_balances_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Aggregate member account balances  # noqa: E501

        This endpoint operates much like the _aggregate member_ endpoint except that it gathers only account balance information; it does not gather any transaction data at all.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_member_balances_with_http_info(member_guid, user_guid, async_req=True)
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
                    " to method aggregate_member_balances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `aggregate_member_balances`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `aggregate_member_balances`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/balance', 'POST',
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

    def create_member(self, user_guid, body, **kwargs):  # noqa: E501
        """Create member  # noqa: E501

        This endpoint allows you to create a new member. Members are created with the required parameters credentials and institution_code, and the optional parameters identifier and metadata.<br> When creating a member, you'll need to include the correct type of credential required by the financial institution and provided by the user. You can find out which credential type is required with the /institutions/{institution_code}/credentials endpoint.<br> If successful, Atrium will respond with the newly-created member object.<br> Once you successfully create a member, MX will immediately validate the provided credentials and attempt to aggregate data for accounts and transactions.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_member(user_guid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param MemberCreateRequestBody body: Member object to be created with optional parameters (identifier and metadata) and required parameters (credentials and institution_code) (required)
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_member_with_http_info(user_guid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_member_with_http_info(user_guid, body, **kwargs)  # noqa: E501
            return data

    def create_member_with_http_info(self, user_guid, body, **kwargs):  # noqa: E501
        """Create member  # noqa: E501

        This endpoint allows you to create a new member. Members are created with the required parameters credentials and institution_code, and the optional parameters identifier and metadata.<br> When creating a member, you'll need to include the correct type of credential required by the financial institution and provided by the user. You can find out which credential type is required with the /institutions/{institution_code}/credentials endpoint.<br> If successful, Atrium will respond with the newly-created member object.<br> Once you successfully create a member, MX will immediately validate the provided credentials and attempt to aggregate data for accounts and transactions.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_member_with_http_info(user_guid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param MemberCreateRequestBody body: Member object to be created with optional parameters (identifier and metadata) and required parameters (credentials and institution_code) (required)
        :return: MemberResponseBody
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
                    " to method create_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `create_member`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_member`")  # noqa: E501

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
            '/users/{user_guid}/members', 'POST',
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

    def delete_member(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Delete member  # noqa: E501

        Accessing this endpoint will permanently delete a member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_member(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def delete_member_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Delete member  # noqa: E501

        Accessing this endpoint will permanently delete a member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_member_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: None
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
                    " to method delete_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `delete_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `delete_member`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def extend_history(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Extend history  # noqa: E501

        The extend_history endpoint begins the process of fetching up to 24 months of data associated with a particular `member`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.extend_history(member_guid, user_guid, async_req=True)
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
            return self.extend_history_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.extend_history_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def extend_history_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Extend history  # noqa: E501

        The extend_history endpoint begins the process of fetching up to 24 months of data associated with a particular `member`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.extend_history_with_http_info(member_guid, user_guid, async_req=True)
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
                    " to method extend_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `extend_history`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `extend_history`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/extend_history', 'POST',
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

    def list_member_accounts(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member accounts  # noqa: E501

        This endpoint returns an array with information about every account associated with a particular member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_accounts(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: AccountsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_member_accounts_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_member_accounts_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_member_accounts_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member accounts  # noqa: E501

        This endpoint returns an array with information about every account associated with a particular member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_accounts_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: AccountsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'page', 'records_per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_member_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_member_accounts`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_member_accounts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_guid' in params:
            path_params['member_guid'] = params['member_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'records_per_page' in params:
            query_params.append(('records_per_page', params['records_per_page']))  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_member_credentials(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member credentials  # noqa: E501

        This endpoint returns an array which contains information on every non-MFA credential associated with a specific member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_credentials(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: CredentialsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_member_credentials_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_member_credentials_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_member_credentials_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member credentials  # noqa: E501

        This endpoint returns an array which contains information on every non-MFA credential associated with a specific member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_credentials_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: CredentialsResponseBody
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
                    " to method list_member_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_member_credentials`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_member_credentials`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredentialsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_member_mfa_challenges(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member MFA challenges  # noqa: E501

        Use this endpoint for information on what multi-factor authentication challenges need to be answered in order to aggregate a member.<br> If the aggregation is not challenged, i.e., the member does not have a connection status of CHALLENGED, then code 204 No Content will be returned.<br> If the aggregation has been challenged, i.e., the member does have a connection status of CHALLENGED, then code 200 OK will be returned — along with the corresponding credentials.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_mfa_challenges(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: ChallengesResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_member_mfa_challenges_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_member_mfa_challenges_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_member_mfa_challenges_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member MFA challenges  # noqa: E501

        Use this endpoint for information on what multi-factor authentication challenges need to be answered in order to aggregate a member.<br> If the aggregation is not challenged, i.e., the member does not have a connection status of CHALLENGED, then code 204 No Content will be returned.<br> If the aggregation has been challenged, i.e., the member does have a connection status of CHALLENGED, then code 200 OK will be returned — along with the corresponding credentials.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_mfa_challenges_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: ChallengesResponseBody
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
                    " to method list_member_mfa_challenges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_member_mfa_challenges`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_member_mfa_challenges`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/challenges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChallengesResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_member_transactions(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member transactions  # noqa: E501

        Use this endpoint to get all transactions from all accounts associated with a specific member.<br> This endpoint accepts optional URL query parameters — from_date and to_date — which are used to filter transactions according to the date they were posted. If no values are given for the query parameters, from_date will default to 90 days prior to the request and to_date will default to 5 days from the time of the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_transactions(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str from_date: Filter transactions from this date.
        :param str to_date: Filter transactions to this date.
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: TransactionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_member_transactions_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_member_transactions_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_member_transactions_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member transactions  # noqa: E501

        Use this endpoint to get all transactions from all accounts associated with a specific member.<br> This endpoint accepts optional URL query parameters — from_date and to_date — which are used to filter transactions according to the date they were posted. If no values are given for the query parameters, from_date will default to 90 days prior to the request and to_date will default to 5 days from the time of the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_transactions_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str from_date: Filter transactions from this date.
        :param str to_date: Filter transactions to this date.
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: TransactionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'from_date', 'to_date', 'page', 'records_per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_member_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_member_transactions`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_member_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_guid' in params:
            path_params['member_guid'] = params['member_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []
        if 'from_date' in params:
            query_params.append(('from_date', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('to_date', params['to_date']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'records_per_page' in params:
            query_params.append(('records_per_page', params['records_per_page']))  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_members(self, user_guid, **kwargs):  # noqa: E501
        """List members  # noqa: E501

        This endpoint returns an array which contains information on every member associated with a specific user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_members(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: MembersResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_members_with_http_info(user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_members_with_http_info(user_guid, **kwargs)  # noqa: E501
            return data

    def list_members_with_http_info(self, user_guid, **kwargs):  # noqa: E501
        """List members  # noqa: E501

        This endpoint returns an array which contains information on every member associated with a specific user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_members_with_http_info(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: MembersResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_guid', 'page', 'records_per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'records_per_page' in params:
            query_params.append(('records_per_page', params['records_per_page']))  # noqa: E501

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
            '/users/{user_guid}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MembersResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_member(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read member  # noqa: E501

        Use this endpoint to read the attributes of a specific member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_member(member_guid, user_guid, async_req=True)
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
            return self.read_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_member_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read member  # noqa: E501

        Use this endpoint to read the attributes of a specific member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_member_with_http_info(member_guid, user_guid, async_req=True)
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
                    " to method read_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `read_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_member`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}', 'GET',
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

    def read_member_status(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read member connection status  # noqa: E501

        This endpoint provides the status of the member's most recent aggregation event. This is an important step in the aggregation process, and the results returned by this endpoint should determine what you do next in order to successfully aggregate a member.<br> MX has introduced new, more detailed information on the current status of a member's connection to a financial institution and the state of its aggregation: the connection_status field. These are intended to replace and expand upon the information provided in the status field, which will soon be deprecated; support for the status field remains for the time being.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_member_status(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: MemberConnectionStatusResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_member_status_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_member_status_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_member_status_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read member connection status  # noqa: E501

        This endpoint provides the status of the member's most recent aggregation event. This is an important step in the aggregation process, and the results returned by this endpoint should determine what you do next in order to successfully aggregate a member.<br> MX has introduced new, more detailed information on the current status of a member's connection to a financial institution and the state of its aggregation: the connection_status field. These are intended to replace and expand upon the information provided in the status field, which will soon be deprecated; support for the status field remains for the time being.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_member_status_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: MemberConnectionStatusResponseBody
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
                    " to method read_member_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `read_member_status`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_member_status`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MemberConnectionStatusResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_o_auth_window_uri(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read OAuth Window URI  # noqa: E501

        This endpoint will generate an `oauth_window_uri` for the specified `member`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_o_auth_window_uri(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str referral_source: Should be either BROWSER or APP depending on the implementation.
        :param str ui_message_webview_url_scheme: A scheme for routing the user back to the application state they were previously in.
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_o_auth_window_uri_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_o_auth_window_uri_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_o_auth_window_uri_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read OAuth Window URI  # noqa: E501

        This endpoint will generate an `oauth_window_uri` for the specified `member`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_o_auth_window_uri_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str referral_source: Should be either BROWSER or APP depending on the implementation.
        :param str ui_message_webview_url_scheme: A scheme for routing the user back to the application state they were previously in.
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'referral_source', 'ui_message_webview_url_scheme']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_o_auth_window_uri" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `read_o_auth_window_uri`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_o_auth_window_uri`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_guid' in params:
            path_params['member_guid'] = params['member_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []
        if 'referral_source' in params:
            query_params.append(('referral_source', params['referral_source']))  # noqa: E501
        if 'ui_message_webview_url_scheme' in params:
            query_params.append(('ui_message_webview_url_scheme', params['ui_message_webview_url_scheme']))  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/oauth_window_uri', 'GET',
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

    def resume_member(self, member_guid, user_guid, body, **kwargs):  # noqa: E501
        """Resume aggregation from MFA  # noqa: E501

        This endpoint answers the challenges needed when a member has been challenged by multi-factor authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resume_member(member_guid, user_guid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param MemberResumeRequestBody body: Member object with MFA challenge answers (required)
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resume_member_with_http_info(member_guid, user_guid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.resume_member_with_http_info(member_guid, user_guid, body, **kwargs)  # noqa: E501
            return data

    def resume_member_with_http_info(self, member_guid, user_guid, body, **kwargs):  # noqa: E501
        """Resume aggregation from MFA  # noqa: E501

        This endpoint answers the challenges needed when a member has been challenged by multi-factor authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resume_member_with_http_info(member_guid, user_guid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param MemberResumeRequestBody body: Member object with MFA challenge answers (required)
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resume_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `resume_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `resume_member`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `resume_member`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/resume', 'PUT',
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

    def update_member(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Update member  # noqa: E501

        Use this endpoint to update a member's attributes. Only the credentials, identifier, and metadata parameters can be updated. To get a list of the required credentials for the member, use the list member credentials endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_member(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param MemberUpdateRequestBody body: Member object to be updated with optional parameters (credentials, identifier, metadata)
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_member_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def update_member_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Update member  # noqa: E501

        Use this endpoint to update a member's attributes. Only the credentials, identifier, and metadata parameters can be updated. To get a list of the required credentials for the member, use the list member credentials endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_member_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param MemberUpdateRequestBody body: Member object to be updated with optional parameters (credentials, identifier, metadata)
        :return: MemberResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `update_member`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `update_member`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}', 'PUT',
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
