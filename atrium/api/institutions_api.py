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


class InstitutionsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_institutions(self, **kwargs):  # noqa: E501
        """List institutions  # noqa: E501

        This endpoint allows you to see what institutions are available for connection. Information returned will include the institution_code assigned to a particular institution, URLs for the financial institution's logo, and the URL for its website.<br> This endpoint takes an optional query string, name={string}. This will list only institutions in which the appended string appears.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_institutions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: This will list only institutions in which the appended string appears.
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :param bool supports_account_identification: Filter only institutions which support account identification.
        :param bool supports_account_statement: Filter only institutions which support account statements.
        :param bool supports_account_verification: Filter only institutions which support account verification.
        :param bool supports_transaction_history: Filter only institutions which support extended transaction history.
        :return: InstitutionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_institutions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_institutions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_institutions_with_http_info(self, **kwargs):  # noqa: E501
        """List institutions  # noqa: E501

        This endpoint allows you to see what institutions are available for connection. Information returned will include the institution_code assigned to a particular institution, URLs for the financial institution's logo, and the URL for its website.<br> This endpoint takes an optional query string, name={string}. This will list only institutions in which the appended string appears.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_institutions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: This will list only institutions in which the appended string appears.
        :param int page: Specify current page.
        :param int records_per_page: Specify records per page.
        :param bool supports_account_identification: Filter only institutions which support account identification.
        :param bool supports_account_statement: Filter only institutions which support account statements.
        :param bool supports_account_verification: Filter only institutions which support account verification.
        :param bool supports_transaction_history: Filter only institutions which support extended transaction history.
        :return: InstitutionsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'page', 'records_per_page', 'supports_account_identification', 'supports_account_statement', 'supports_account_verification', 'supports_transaction_history']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_institutions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'records_per_page' in params:
            query_params.append(('records_per_page', params['records_per_page']))  # noqa: E501
        if 'supports_account_identification' in params:
            query_params.append(('supports_account_identification', params['supports_account_identification']))  # noqa: E501
        if 'supports_account_statement' in params:
            query_params.append(('supports_account_statement', params['supports_account_statement']))  # noqa: E501
        if 'supports_account_verification' in params:
            query_params.append(('supports_account_verification', params['supports_account_verification']))  # noqa: E501
        if 'supports_transaction_history' in params:
            query_params.append(('supports_transaction_history', params['supports_transaction_history']))  # noqa: E501

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
            '/institutions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstitutionsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_institution(self, institution_code, **kwargs):  # noqa: E501
        """Read institution  # noqa: E501

        This endpoint allows you to see information for a specific institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_institution(institution_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str institution_code: The institution_code of the institution. (required)
        :return: InstitutionResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_institution_with_http_info(institution_code, **kwargs)  # noqa: E501
        else:
            (data) = self.read_institution_with_http_info(institution_code, **kwargs)  # noqa: E501
            return data

    def read_institution_with_http_info(self, institution_code, **kwargs):  # noqa: E501
        """Read institution  # noqa: E501

        This endpoint allows you to see information for a specific institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_institution_with_http_info(institution_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str institution_code: The institution_code of the institution. (required)
        :return: InstitutionResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['institution_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_institution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'institution_code' is set
        if ('institution_code' not in params or
                params['institution_code'] is None):
            raise ValueError("Missing the required parameter `institution_code` when calling `read_institution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'institution_code' in params:
            path_params['institution_code'] = params['institution_code']  # noqa: E501

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
            '/institutions/{institution_code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstitutionResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_institution_credentials(self, institution_code, **kwargs):  # noqa: E501
        """Read institution credentials  # noqa: E501

        Use this endpoint to see which credentials will be needed to create a member for a specific institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_institution_credentials(institution_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str institution_code: The institution_code of the institution. (required)
        :return: CredentialsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_institution_credentials_with_http_info(institution_code, **kwargs)  # noqa: E501
        else:
            (data) = self.read_institution_credentials_with_http_info(institution_code, **kwargs)  # noqa: E501
            return data

    def read_institution_credentials_with_http_info(self, institution_code, **kwargs):  # noqa: E501
        """Read institution credentials  # noqa: E501

        Use this endpoint to see which credentials will be needed to create a member for a specific institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_institution_credentials_with_http_info(institution_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str institution_code: The institution_code of the institution. (required)
        :return: CredentialsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['institution_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_institution_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'institution_code' is set
        if ('institution_code' not in params or
                params['institution_code'] is None):
            raise ValueError("Missing the required parameter `institution_code` when calling `read_institution_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'institution_code' in params:
            path_params['institution_code'] = params['institution_code']  # noqa: E501

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
            '/institutions/{institution_code}/credentials', 'GET',
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
