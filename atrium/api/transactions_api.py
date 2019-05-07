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


class TransactionsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cleanse_and_categorize_transactions(self, body, **kwargs):  # noqa: E501
        """Categorize transactions  # noqa: E501

        Use this endpoint to categorize, cleanse, and classify transactions. These transactions are not persisted or stored on the MX platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cleanse_and_categorize_transactions(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransactionsCleanseAndCategorizeRequestBody body: User object to be created with optional parameters (amount, type) amd required parameters (description, identifier) (required)
        :return: TransactionsCleanseAndCategorizeResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cleanse_and_categorize_transactions_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.cleanse_and_categorize_transactions_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def cleanse_and_categorize_transactions_with_http_info(self, body, **kwargs):  # noqa: E501
        """Categorize transactions  # noqa: E501

        Use this endpoint to categorize, cleanse, and classify transactions. These transactions are not persisted or stored on the MX platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cleanse_and_categorize_transactions_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransactionsCleanseAndCategorizeRequestBody body: User object to be created with optional parameters (amount, type) amd required parameters (description, identifier) (required)
        :return: TransactionsCleanseAndCategorizeResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cleanse_and_categorize_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `cleanse_and_categorize_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/transactions/cleanse_and_categorize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionsCleanseAndCategorizeResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_transactions(self, user_guid, **kwargs):  # noqa: E501
        """List transactions for a user  # noqa: E501

        Use this endpoint to get all transactions that belong to a specific user, across all the user's members and accounts.<br> This endpoint accepts optional query parameters, from_date and to_date, which filter transactions according to the date they were posted. If no values are given, from_date will default to 90 days prior to the request, and to_date will default to 5 days from the time of the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_transactions(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param str from_date: Filter transactions from this date.
        :param int records_per_page: Specify records per page.
        :param str to_date: Filter transactions to this date.
        :return: TransactionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_transactions_with_http_info(user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_transactions_with_http_info(user_guid, **kwargs)  # noqa: E501
            return data

    def list_user_transactions_with_http_info(self, user_guid, **kwargs):  # noqa: E501
        """List transactions for a user  # noqa: E501

        Use this endpoint to get all transactions that belong to a specific user, across all the user's members and accounts.<br> This endpoint accepts optional query parameters, from_date and to_date, which filter transactions according to the date they were posted. If no values are given, from_date will default to 90 days prior to the request, and to_date will default to 5 days from the time of the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_transactions_with_http_info(user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param str from_date: Filter transactions from this date.
        :param int records_per_page: Specify records per page.
        :param str to_date: Filter transactions to this date.
        :return: TransactionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_guid', 'page', 'from_date', 'records_per_page', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_user_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('from_date', params['from_date']))  # noqa: E501
        if 'records_per_page' in params:
            query_params.append(('records_per_page', params['records_per_page']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('to_date', params['to_date']))  # noqa: E501

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
            '/users/{user_guid}/transactions', 'GET',
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

    def read_transaction(self, transaction_guid, user_guid, **kwargs):  # noqa: E501
        """Read a transaction  # noqa: E501

        This endpoint allows you to view information about a specific transaction that belongs to a user.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_transaction(transaction_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_guid: The unique identifier for a `transaction`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: TransactionResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_transaction_with_http_info(transaction_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_transaction_with_http_info(transaction_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def read_transaction_with_http_info(self, transaction_guid, user_guid, **kwargs):  # noqa: E501
        """Read a transaction  # noqa: E501

        This endpoint allows you to view information about a specific transaction that belongs to a user.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_transaction_with_http_info(transaction_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_guid: The unique identifier for a `transaction`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :return: TransactionResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_guid', 'user_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transaction_guid' is set
        if ('transaction_guid' not in params or
                params['transaction_guid'] is None):
            raise ValueError("Missing the required parameter `transaction_guid` when calling `read_transaction`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_guid' in params:
            path_params['transaction_guid'] = params['transaction_guid']  # noqa: E501
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
            '/users/{user_guid}/transactions/{transaction_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
