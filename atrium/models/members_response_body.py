# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from atrium.models.member import Member  # noqa: F401,E501
from atrium.models.pagination import Pagination  # noqa: F401,E501


class MembersResponseBody(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'members': 'list[Member]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'members': 'members',
        'pagination': 'pagination'
    }

    def __init__(self, members=None, pagination=None):  # noqa: E501

        self._members = None
        self._pagination = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if pagination is not None:
            self.pagination = pagination

    @property
    def members(self):
        """Gets the members of this MembersResponseBody.  # noqa: E501


        :return: The members of this MembersResponseBody.  # noqa: E501
        :rtype: list[Member]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this MembersResponseBody.


        :param members: The members of this MembersResponseBody.  # noqa: E501
        :type: list[Member]
        """

        self._members = members

    @property
    def pagination(self):
        """Gets the pagination of this MembersResponseBody.  # noqa: E501


        :return: The pagination of this MembersResponseBody.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this MembersResponseBody.


        :param pagination: The pagination of this MembersResponseBody.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

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
        if issubclass(MembersResponseBody, dict):
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
        if not isinstance(other, MembersResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
