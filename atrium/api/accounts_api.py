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


class AccountsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_account_transactions(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """List account transactions  # noqa: E501

        This endpoint allows you to see every transaction that belongs to a specific account. The default from_date is 90 days prior to the request, and the default to_date is 5 days from the time of the request.<br> The from_date and to_date parameters can optionally be appended to the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_transactions(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
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
            return self.list_account_transactions_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_account_transactions_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_account_transactions_with_http_info(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """List account transactions  # noqa: E501

        This endpoint allows you to see every transaction that belongs to a specific account. The default from_date is 90 days prior to the request, and the default to_date is 5 days from the time of the request.<br> The from_date and to_date parameters can optionally be appended to the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_transactions_with_http_info(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str from_date: Filter transactions from this date.
        :param str to_date: Filter transactions to this date.
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: TransactionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_guid', 'user_guid', 'from_date', 'to_date', 'page', 'records_per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_account_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_guid' is set
        if ('account_guid' not in params or
                params['account_guid'] is None):
            raise ValueError("Missing the required parameter `account_guid` when calling `list_account_transactions`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_account_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_guid' in params:
            path_params['account_guid'] = params['account_guid']  # noqa: E501
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
            '/users/{user_guid}/accounts/{account_guid}/transactions', 'GET',
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

    def list_user_accounts(self, user_guid, **kwargs):  # noqa: E501
        """List accounts for a user  # noqa: E501

        Use this endpoint to view information about every account that belongs to a user. You'll need the user's GUID to access this list. The information will include the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the account balance, the date the account was started, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_accounts(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: AccountsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_accounts_with_http_info(user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_accounts_with_http_info(user_guid, **kwargs)  # noqa: E501
            return data

    def list_user_accounts_with_http_info(self, user_guid, **kwargs):  # noqa: E501
        """List accounts for a user  # noqa: E501

        Use this endpoint to view information about every account that belongs to a user. You'll need the user's GUID to access this list. The information will include the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the account balance, the date the account was started, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_accounts_with_http_info(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: AccountsResponseBody
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
                    " to method list_user_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_user_accounts`")  # noqa: E501

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
            '/users/{user_guid}/accounts', 'GET',
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

    def read_account(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """Read an account  # noqa: E501

        Reading an account allows you to get information about a specific account that belongs to a user. That includes the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the balance, the date the account was started, and much more.<br> There are two endpoints for reading an account. Both will return the same information.<br> It's important to remember that balance and available_balance will normally be positive numbers — for all account types. But this should be interpreted differently for debt accounts and asset accounts.<br> An asset account, e.g., CHECKING, SAVINGS, or INVESTMENT, will have a positive balance unless it is in an overdraft condition, in which case the balance will be negative.<br> On the other hand, a debt account, e.g., CREDIT CARD, LOAN, MORTGAGE, would have a positivebalance when the user owes money on the account. It would have a negative balance if the account has been overpaid.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_account(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_account_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_account_with_http_info(account_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_account_with_http_info(self, account_guid, user_guid, **kwargs):  # noqa: E501
        """Read an account  # noqa: E501

        Reading an account allows you to get information about a specific account that belongs to a user. That includes the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the balance, the date the account was started, and much more.<br> There are two endpoints for reading an account. Both will return the same information.<br> It's important to remember that balance and available_balance will normally be positive numbers — for all account types. But this should be interpreted differently for debt accounts and asset accounts.<br> An asset account, e.g., CHECKING, SAVINGS, or INVESTMENT, will have a positive balance unless it is in an overdraft condition, in which case the balance will be negative.<br> On the other hand, a debt account, e.g., CREDIT CARD, LOAN, MORTGAGE, would have a positivebalance when the user owes money on the account. It would have a negative balance if the account has been overpaid.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_account_with_http_info(account_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountResponseBody
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
                    " to method read_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_guid' is set
        if ('account_guid' not in params or
                params['account_guid'] is None):
            raise ValueError("Missing the required parameter `account_guid` when calling `read_account`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_account`")  # noqa: E501

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
            '/users/{user_guid}/accounts/{account_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_account_by_member_guid(self, account_guid, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read an account  # noqa: E501

        Reading an account allows you to get information about a specific account that belongs to a user. That includes the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the balance, the date the account was started, and much more.<br> There are two endpoints for reading an account. Both will return the same information.<br> It's important to remember that balance and available_balance will normally be positive numbers — for all account types. But this should be interpreted differently for debt accounts and asset accounts.<br> An asset account, e.g., CHECKING, SAVINGS, or INVESTMENT, will have a positive balance unless it is in an overdraft condition, in which case the balance will be negative.<br> On the other hand, a debt account, e.g., CREDIT CARD, LOAN, MORTGAGE, would have a positivebalance when the user owes money on the account. It would have a negative balance if the account has been overpaid.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_account_by_member_guid(account_guid, member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_account_by_member_guid_with_http_info(account_guid, member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_account_by_member_guid_with_http_info(account_guid, member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_account_by_member_guid_with_http_info(self, account_guid, member_guid, user_guid, **kwargs):  # noqa: E501
        """Read an account  # noqa: E501

        Reading an account allows you to get information about a specific account that belongs to a user. That includes the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the balance, the date the account was started, and much more.<br> There are two endpoints for reading an account. Both will return the same information.<br> It's important to remember that balance and available_balance will normally be positive numbers — for all account types. But this should be interpreted differently for debt accounts and asset accounts.<br> An asset account, e.g., CHECKING, SAVINGS, or INVESTMENT, will have a positive balance unless it is in an overdraft condition, in which case the balance will be negative.<br> On the other hand, a debt account, e.g., CREDIT CARD, LOAN, MORTGAGE, would have a positivebalance when the user owes money on the account. It would have a negative balance if the account has been overpaid.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_account_by_member_guid_with_http_info(account_guid, member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_guid: The unique identifier for an `account`. (required)
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: AccountResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_guid', 'member_guid', 'user_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_account_by_member_guid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_guid' is set
        if ('account_guid' not in params or
                params['account_guid'] is None):
            raise ValueError("Missing the required parameter `account_guid` when calling `read_account_by_member_guid`")  # noqa: E501
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `read_account_by_member_guid`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_account_by_member_guid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_guid' in params:
            path_params['account_guid'] = params['account_guid']  # noqa: E501
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
            '/users/{user_guid}/members/{member_guid}/accounts/{account_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
