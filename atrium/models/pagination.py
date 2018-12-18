# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Pagination(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'current_page': 'int',
        'per_page': 'int',
        'total_entries': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'current_page': 'current_page',
        'per_page': 'per_page',
        'total_entries': 'total_entries',
        'total_pages': 'total_pages'
    }

    def __init__(self, current_page=None, per_page=None, total_entries=None, total_pages=None):  # noqa: E501

        self._current_page = None
        self._per_page = None
        self._total_entries = None
        self._total_pages = None
        self.discriminator = None

        if current_page is not None:
            self.current_page = current_page
        if per_page is not None:
            self.per_page = per_page
        if total_entries is not None:
            self.total_entries = total_entries
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def current_page(self):
        """Gets the current_page of this Pagination.  # noqa: E501


        :return: The current_page of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this Pagination.


        :param current_page: The current_page of this Pagination.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def per_page(self):
        """Gets the per_page of this Pagination.  # noqa: E501


        :return: The per_page of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this Pagination.


        :param per_page: The per_page of this Pagination.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def total_entries(self):
        """Gets the total_entries of this Pagination.  # noqa: E501


        :return: The total_entries of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._total_entries

    @total_entries.setter
    def total_entries(self, total_entries):
        """Sets the total_entries of this Pagination.


        :param total_entries: The total_entries of this Pagination.  # noqa: E501
        :type: int
        """

        self._total_entries = total_entries

    @property
    def total_pages(self):
        """Gets the total_pages of this Pagination.  # noqa: E501


        :return: The total_pages of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this Pagination.


        :param total_pages: The total_pages of this Pagination.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

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
        if issubclass(Pagination, dict):
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
        if not isinstance(other, Pagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
