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


class StatementsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_statement_pdf(self, member_guid, user_guid, statement_guid, **kwargs):  # noqa: E501
        """Download statement PDF  # noqa: E501

        Use this endpoint to download a specified statement. The endpoint URL is the same as the URI given in each `statement` object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_statement_pdf(member_guid, user_guid, statement_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str statement_guid: The unique identifier for an `statement`. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_statement_pdf_with_http_info(member_guid, user_guid, statement_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.download_statement_pdf_with_http_info(member_guid, user_guid, statement_guid, **kwargs)  # noqa: E501
            return data

    def download_statement_pdf_with_http_info(self, member_guid, user_guid, statement_guid, **kwargs):  # noqa: E501
        """Download statement PDF  # noqa: E501

        Use this endpoint to download a specified statement. The endpoint URL is the same as the URI given in each `statement` object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_statement_pdf_with_http_info(member_guid, user_guid, statement_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str statement_guid: The unique identifier for an `statement`. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'statement_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_statement_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `download_statement_pdf`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `download_statement_pdf`")  # noqa: E501
        # verify the required parameter 'statement_guid' is set
        if ('statement_guid' not in params or
                params['statement_guid'] is None):
            raise ValueError("Missing the required parameter `statement_guid` when calling `download_statement_pdf`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_guid' in params:
            path_params['member_guid'] = params['member_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501
        if 'statement_guid' in params:
            path_params['statement_guid'] = params['statement_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.mx.atrium.v1+pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'clientID']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_guid}/members/{member_guid}/statements/{statement_guid}.pdf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_statements(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Fetch statements  # noqa: E501

        The fetch statements endpoint begins fetching statements for a member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_statements(member_guid, user_guid, async_req=True)
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
            return self.fetch_statements_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_statements_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def fetch_statements_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """Fetch statements  # noqa: E501

        The fetch statements endpoint begins fetching statements for a member.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_statements_with_http_info(member_guid, user_guid, async_req=True)
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
                    " to method fetch_statements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `fetch_statements`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `fetch_statements`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/fetch_statements', 'POST',
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

    def list_member_statements(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member statements  # noqa: E501

        Certain institutions in Atrium allow developers to access account statements associated with a particular `member`. Use this endpoint to get an array of available statements.  Before this endpoint can be used, `fetch_statements` should be performed on the relevant `member`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_statements(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: StatementsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_member_statements_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_member_statements_with_http_info(member_guid, user_guid, **kwargs)  # noqa: E501
            return data

    def list_member_statements_with_http_info(self, member_guid, user_guid, **kwargs):  # noqa: E501
        """List member statements  # noqa: E501

        Certain institutions in Atrium allow developers to access account statements associated with a particular `member`. Use this endpoint to get an array of available statements.  Before this endpoint can be used, `fetch_statements` should be performed on the relevant `member`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_member_statements_with_http_info(member_guid, user_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :return: StatementsResponseBody
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
                    " to method list_member_statements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `list_member_statements`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `list_member_statements`")  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/statements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatementsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_member_statement(self, member_guid, user_guid, statement_guid, **kwargs):  # noqa: E501
        """Read statement JSON  # noqa: E501

        Use this endpoint to download a specified statement. The endpoint URL is the same as the URI given in each `statement` object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_member_statement(member_guid, user_guid, statement_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str statement_guid: The unique identifier for an `statement`. (required)
        :return: StatementResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_member_statement_with_http_info(member_guid, user_guid, statement_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_member_statement_with_http_info(member_guid, user_guid, statement_guid, **kwargs)  # noqa: E501
            return data

    def read_member_statement_with_http_info(self, member_guid, user_guid, statement_guid, **kwargs):  # noqa: E501
        """Read statement JSON  # noqa: E501

        Use this endpoint to download a specified statement. The endpoint URL is the same as the URI given in each `statement` object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_member_statement_with_http_info(member_guid, user_guid, statement_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_guid: The unique identifier for a `member`. (required)
        :param str user_guid: The unique identifier for a `user`. (required)
        :param str statement_guid: The unique identifier for an `statement`. (required)
        :return: StatementResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_guid', 'user_guid', 'statement_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_member_statement" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_guid' is set
        if ('member_guid' not in params or
                params['member_guid'] is None):
            raise ValueError("Missing the required parameter `member_guid` when calling `read_member_statement`")  # noqa: E501
        # verify the required parameter 'user_guid' is set
        if ('user_guid' not in params or
                params['user_guid'] is None):
            raise ValueError("Missing the required parameter `user_guid` when calling `read_member_statement`")  # noqa: E501
        # verify the required parameter 'statement_guid' is set
        if ('statement_guid' not in params or
                params['statement_guid'] is None):
            raise ValueError("Missing the required parameter `statement_guid` when calling `read_member_statement`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_guid' in params:
            path_params['member_guid'] = params['member_guid']  # noqa: E501
        if 'user_guid' in params:
            path_params['user_guid'] = params['user_guid']  # noqa: E501
        if 'statement_guid' in params:
            path_params['statement_guid'] = params['statement_guid']  # noqa: E501

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
            '/users/{user_guid}/members/{member_guid}/statements/{statement_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatementResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
