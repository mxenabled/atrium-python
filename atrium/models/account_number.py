# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class AccountNumber(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'account_guid': 'str',
        'account_number': 'str',
        'institution_number': 'str',
        'member_guid': 'str',
        'routing_number': 'str',
        'transit_number': 'str',
        'user_guid': 'str'
    }

    attribute_map = {
        'account_guid': 'account_guid',
        'account_number': 'account_number',
        'institution_number': 'institution_number',
        'member_guid': 'member_guid',
        'routing_number': 'routing_number',
        'transit_number': 'transit_number',
        'user_guid': 'user_guid'
    }

    def __init__(self, account_guid=None, account_number=None, institution_number=None, member_guid=None, routing_number=None, transit_number=None, user_guid=None):  # noqa: E501

        self._account_guid = None
        self._account_number = None
        self._institution_number = None
        self._member_guid = None
        self._routing_number = None
        self._transit_number = None
        self._user_guid = None
        self.discriminator = None

        if account_guid is not None:
            self.account_guid = account_guid
        if account_number is not None:
            self.account_number = account_number
        if institution_number is not None:
            self.institution_number = institution_number
        if member_guid is not None:
            self.member_guid = member_guid
        if routing_number is not None:
            self.routing_number = routing_number
        if transit_number is not None:
            self.transit_number = transit_number
        if user_guid is not None:
            self.user_guid = user_guid

    @property
    def account_guid(self):
        """Gets the account_guid of this AccountNumber.  # noqa: E501


        :return: The account_guid of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._account_guid

    @account_guid.setter
    def account_guid(self, account_guid):
        """Sets the account_guid of this AccountNumber.


        :param account_guid: The account_guid of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._account_guid = account_guid

    @property
    def account_number(self):
        """Gets the account_number of this AccountNumber.  # noqa: E501


        :return: The account_number of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AccountNumber.


        :param account_number: The account_number of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def institution_number(self):
        """Gets the institution_number of this AccountNumber.  # noqa: E501


        :return: The institution_number of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._institution_number

    @institution_number.setter
    def institution_number(self, institution_number):
        """Sets the institution_number of this AccountNumber.


        :param institution_number: The institution_number of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._institution_number = institution_number

    @property
    def member_guid(self):
        """Gets the member_guid of this AccountNumber.  # noqa: E501


        :return: The member_guid of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._member_guid

    @member_guid.setter
    def member_guid(self, member_guid):
        """Sets the member_guid of this AccountNumber.


        :param member_guid: The member_guid of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._member_guid = member_guid

    @property
    def routing_number(self):
        """Gets the routing_number of this AccountNumber.  # noqa: E501


        :return: The routing_number of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this AccountNumber.


        :param routing_number: The routing_number of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._routing_number = routing_number

    @property
    def transit_number(self):
        """Gets the transit_number of this AccountNumber.  # noqa: E501


        :return: The transit_number of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._transit_number

    @transit_number.setter
    def transit_number(self, transit_number):
        """Sets the transit_number of this AccountNumber.


        :param transit_number: The transit_number of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._transit_number = transit_number

    @property
    def user_guid(self):
        """Gets the user_guid of this AccountNumber.  # noqa: E501


        :return: The user_guid of this AccountNumber.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this AccountNumber.


        :param user_guid: The user_guid of this AccountNumber.  # noqa: E501
        :type: str
        """

        self._user_guid = user_guid

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
        if issubclass(AccountNumber, dict):
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
        if not isinstance(other, AccountNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
