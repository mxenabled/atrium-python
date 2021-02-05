# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class ConnectWidgetRequestBody(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'is_mobile_webview': 'bool',
        'color_scheme': 'str',
        'current_institution_code': 'str',
        'current_member_guid': 'str',
        'disable_institution_search': 'bool',
        'include_transactions': 'bool',
        'mode': 'str',
        'ui_message_version': 'float',
        'ui_message_webview_url_scheme': 'str',
        'update_credentials': 'bool',
        'wait_for_full_aggregation': 'bool'
    }

    attribute_map = {
        'is_mobile_webview': 'is_mobile_webview',
        'color_scheme': 'color_scheme',
        'current_institution_code': 'current_institution_code',
        'current_member_guid': 'current_member_guid',
        'disable_institution_search': 'disable_institution_search',
        'include_transactions': 'include_transactions',
        'mode': 'mode',
        'ui_message_version': 'ui_message_version',
        'ui_message_webview_url_scheme': 'ui_message_webview_url_scheme',
        'update_credentials': 'update_credentials',
        'wait_for_full_aggregation': 'wait_for_full_aggregation'
    }

    def __init__(self, is_mobile_webview=None, color_scheme=None, current_institution_code=None, current_member_guid=None, disable_institution_search=None, include_transactions=None, mode=None, ui_message_version=None, ui_message_webview_url_scheme=None, update_credentials=None, wait_for_full_aggregation=None):  # noqa: E501

        self._is_mobile_webview = None
        self._color_scheme = None
        self._current_institution_code = None
        self._current_member_guid = None
        self._disable_institution_search = None
        self._include_transactions = None
        self._mode = None
        self._ui_message_version = None
        self._ui_message_webview_url_scheme = None
        self._update_credentials = None
        self._wait_for_full_aggregation = None
        self.discriminator = None

        if is_mobile_webview is not None:
            self.is_mobile_webview = is_mobile_webview
        if color_scheme is not None:
            self.color_scheme = color_scheme
        if current_institution_code is not None:
            self.current_institution_code = current_institution_code
        if current_member_guid is not None:
            self.current_member_guid = current_member_guid
        if disable_institution_search is not None:
            self.disable_institution_search = disable_institution_search
        if include_transactions is not None:
            self.include_transactions = include_transactions
        if mode is not None:
            self.mode = mode
        if ui_message_version is not None:
            self.ui_message_version = ui_message_version
        if ui_message_webview_url_scheme is not None:
            self.ui_message_webview_url_scheme = ui_message_webview_url_scheme
        if update_credentials is not None:
            self.update_credentials = update_credentials
        if wait_for_full_aggregation is not None:
            self.wait_for_full_aggregation = wait_for_full_aggregation

    @property
    def is_mobile_webview(self):
        """Gets the is_mobile_webview of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The is_mobile_webview of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_mobile_webview

    @is_mobile_webview.setter
    def is_mobile_webview(self, is_mobile_webview):
        """Sets the is_mobile_webview of this ConnectWidgetRequestBody.


        :param is_mobile_webview: The is_mobile_webview of this ConnectWidgetRequestBody.  # noqa: E501
        :type: bool
        """

        self._is_mobile_webview = is_mobile_webview

    @property
    def color_scheme(self):
        """Gets the color_scheme of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The color_scheme of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._color_scheme

    @color_scheme.setter
    def color_scheme(self, color_scheme):
        """Sets the color_scheme of this ConnectWidgetRequestBody.


        :param color_scheme: The color_scheme of this ConnectWidgetRequestBody.  # noqa: E501
        :type: str
        """

        self._color_scheme = color_scheme

    @property
    def current_institution_code(self):
        """Gets the current_institution_code of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The current_institution_code of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._current_institution_code

    @current_institution_code.setter
    def current_institution_code(self, current_institution_code):
        """Sets the current_institution_code of this ConnectWidgetRequestBody.


        :param current_institution_code: The current_institution_code of this ConnectWidgetRequestBody.  # noqa: E501
        :type: str
        """

        self._current_institution_code = current_institution_code

    @property
    def current_member_guid(self):
        """Gets the current_member_guid of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The current_member_guid of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._current_member_guid

    @current_member_guid.setter
    def current_member_guid(self, current_member_guid):
        """Sets the current_member_guid of this ConnectWidgetRequestBody.


        :param current_member_guid: The current_member_guid of this ConnectWidgetRequestBody.  # noqa: E501
        :type: str
        """

        self._current_member_guid = current_member_guid

    @property
    def disable_institution_search(self):
        """Gets the disable_institution_search of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The disable_institution_search of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._disable_institution_search

    @disable_institution_search.setter
    def disable_institution_search(self, disable_institution_search):
        """Sets the disable_institution_search of this ConnectWidgetRequestBody.


        :param disable_institution_search: The disable_institution_search of this ConnectWidgetRequestBody.  # noqa: E501
        :type: bool
        """

        self._disable_institution_search = disable_institution_search

    @property
    def include_transactions(self):
        """Gets the include_transactions of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The include_transactions of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._include_transactions

    @include_transactions.setter
    def include_transactions(self, include_transactions):
        """Sets the include_transactions of this ConnectWidgetRequestBody.


        :param include_transactions: The include_transactions of this ConnectWidgetRequestBody.  # noqa: E501
        :type: bool
        """

        self._include_transactions = include_transactions

    @property
    def mode(self):
        """Gets the mode of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The mode of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ConnectWidgetRequestBody.


        :param mode: The mode of this ConnectWidgetRequestBody.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def ui_message_version(self):
        """Gets the ui_message_version of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The ui_message_version of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: float
        """
        return self._ui_message_version

    @ui_message_version.setter
    def ui_message_version(self, ui_message_version):
        """Sets the ui_message_version of this ConnectWidgetRequestBody.


        :param ui_message_version: The ui_message_version of this ConnectWidgetRequestBody.  # noqa: E501
        :type: float
        """

        self._ui_message_version = ui_message_version

    @property
    def ui_message_webview_url_scheme(self):
        """Gets the ui_message_webview_url_scheme of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The ui_message_webview_url_scheme of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._ui_message_webview_url_scheme

    @ui_message_webview_url_scheme.setter
    def ui_message_webview_url_scheme(self, ui_message_webview_url_scheme):
        """Sets the ui_message_webview_url_scheme of this ConnectWidgetRequestBody.


        :param ui_message_webview_url_scheme: The ui_message_webview_url_scheme of this ConnectWidgetRequestBody.  # noqa: E501
        :type: str
        """

        self._ui_message_webview_url_scheme = ui_message_webview_url_scheme

    @property
    def update_credentials(self):
        """Gets the update_credentials of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The update_credentials of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._update_credentials

    @update_credentials.setter
    def update_credentials(self, update_credentials):
        """Sets the update_credentials of this ConnectWidgetRequestBody.


        :param update_credentials: The update_credentials of this ConnectWidgetRequestBody.  # noqa: E501
        :type: bool
        """

        self._update_credentials = update_credentials

    @property
    def wait_for_full_aggregation(self):
        """Gets the wait_for_full_aggregation of this ConnectWidgetRequestBody.  # noqa: E501


        :return: The wait_for_full_aggregation of this ConnectWidgetRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._wait_for_full_aggregation

    @wait_for_full_aggregation.setter
    def wait_for_full_aggregation(self, wait_for_full_aggregation):
        """Sets the wait_for_full_aggregation of this ConnectWidgetRequestBody.


        :param wait_for_full_aggregation: The wait_for_full_aggregation of this ConnectWidgetRequestBody.  # noqa: E501
        :type: bool
        """

        self._wait_for_full_aggregation = wait_for_full_aggregation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.mx_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConnectWidgetRequestBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectWidgetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
