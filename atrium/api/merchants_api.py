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


class MerchantsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_merchant_locations(self, merchant_guid, **kwargs):  # noqa: E501
        """List merchant locations  # noqa: E501

        Returns a list of all the merchant locations associated with a merchant, including physical location, latitude, longitude, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_merchant_locations(merchant_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_guid: The unique identifier for a `merchant`. (required)
        :return: MerchantLocationsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_merchant_locations_with_http_info(merchant_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_merchant_locations_with_http_info(merchant_guid, **kwargs)  # noqa: E501
            return data

    def list_merchant_locations_with_http_info(self, merchant_guid, **kwargs):  # noqa: E501
        """List merchant locations  # noqa: E501

        Returns a list of all the merchant locations associated with a merchant, including physical location, latitude, longitude, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_merchant_locations_with_http_info(merchant_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_guid: The unique identifier for a `merchant`. (required)
        :return: MerchantLocationsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_merchant_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_guid' is set
        if ('merchant_guid' not in params or
                params['merchant_guid'] is None):
            raise ValueError("Missing the required parameter `merchant_guid` when calling `list_merchant_locations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_guid' in params:
            path_params['merchant_guid'] = params['merchant_guid']  # noqa: E501

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
            '/merchants/{merchant_guid}/merchant_locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantLocationsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_merchants(self, **kwargs):  # noqa: E501
        """List merchants  # noqa: E501

        Returns a list of merchnants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_merchants(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MerchantsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_merchants_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_merchants_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_merchants_with_http_info(self, **kwargs):  # noqa: E501
        """List merchants  # noqa: E501

        Returns a list of merchnants.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_merchants_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MerchantsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_merchants" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/merchants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_merchant(self, merchant_guid, **kwargs):  # noqa: E501
        """Read merchant  # noqa: E501

        Returns information about a particular merchant, such as a logo, name, and website.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_merchant(merchant_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_guid: The unique identifier for a `merchant`. (required)
        :return: MerchantResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_merchant_with_http_info(merchant_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_merchant_with_http_info(merchant_guid, **kwargs)  # noqa: E501
            return data

    def read_merchant_with_http_info(self, merchant_guid, **kwargs):  # noqa: E501
        """Read merchant  # noqa: E501

        Returns information about a particular merchant, such as a logo, name, and website.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_merchant_with_http_info(merchant_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_guid: The unique identifier for a `merchant`. (required)
        :return: MerchantResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_merchant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_guid' is set
        if ('merchant_guid' not in params or
                params['merchant_guid'] is None):
            raise ValueError("Missing the required parameter `merchant_guid` when calling `read_merchant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_guid' in params:
            path_params['merchant_guid'] = params['merchant_guid']  # noqa: E501

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
            '/merchants/{merchant_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_merchant_location(self, merchant_guid, merchant_location_guid, **kwargs):  # noqa: E501
        """Read merchant location  # noqa: E501

        Retuns a specific location associated with a merchant, including physical location, latitude, longitude, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_merchant_location(merchant_guid, merchant_location_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_guid: The unique identifier for a `merchant`. (required)
        :param str merchant_location_guid: The unique identifier for a `merchant_location`. (required)
        :return: MerchantLocationResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_merchant_location_with_http_info(merchant_guid, merchant_location_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.read_merchant_location_with_http_info(merchant_guid, merchant_location_guid, **kwargs)  # noqa: E501
            return data

    def read_merchant_location_with_http_info(self, merchant_guid, merchant_location_guid, **kwargs):  # noqa: E501
        """Read merchant location  # noqa: E501

        Retuns a specific location associated with a merchant, including physical location, latitude, longitude, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_merchant_location_with_http_info(merchant_guid, merchant_location_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_guid: The unique identifier for a `merchant`. (required)
        :param str merchant_location_guid: The unique identifier for a `merchant_location`. (required)
        :return: MerchantLocationResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_guid', 'merchant_location_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_merchant_location" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_guid' is set
        if ('merchant_guid' not in params or
                params['merchant_guid'] is None):
            raise ValueError("Missing the required parameter `merchant_guid` when calling `read_merchant_location`")  # noqa: E501
        # verify the required parameter 'merchant_location_guid' is set
        if ('merchant_location_guid' not in params or
                params['merchant_location_guid'] is None):
            raise ValueError("Missing the required parameter `merchant_location_guid` when calling `read_merchant_location`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_guid' in params:
            path_params['merchant_guid'] = params['merchant_guid']  # noqa: E501
        if 'merchant_location_guid' in params:
            path_params['merchant_location_guid'] = params['merchant_location_guid']  # noqa: E501

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
            '/merchants/{merchant_guid}/merchant_locations/{merchant_location_guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantLocationResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
