# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class AccountOwner(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'account_guid': 'str',
        'address': 'str',
        'city': 'str',
        'country': 'str',
        'email': 'str',
        'guid': 'str',
        'member_guid': 'str',
        'owner_name': 'str',
        'postal_code': 'str',
        'state': 'str',
        'user_guid': 'str'
    }

    attribute_map = {
        'account_guid': 'account_guid',
        'address': 'address',
        'city': 'city',
        'country': 'country',
        'email': 'email',
        'guid': 'guid',
        'member_guid': 'member_guid',
        'owner_name': 'owner_name',
        'postal_code': 'postal_code',
        'state': 'state',
        'user_guid': 'user_guid'
    }

    def __init__(self, account_guid=None, address=None, city=None, country=None, email=None, guid=None, member_guid=None, owner_name=None, postal_code=None, state=None, user_guid=None):  # noqa: E501

        self._account_guid = None
        self._address = None
        self._city = None
        self._country = None
        self._email = None
        self._guid = None
        self._member_guid = None
        self._owner_name = None
        self._postal_code = None
        self._state = None
        self._user_guid = None
        self.discriminator = None

        if account_guid is not None:
            self.account_guid = account_guid
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if guid is not None:
            self.guid = guid
        if member_guid is not None:
            self.member_guid = member_guid
        if owner_name is not None:
            self.owner_name = owner_name
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if user_guid is not None:
            self.user_guid = user_guid

    @property
    def account_guid(self):
        """Gets the account_guid of this AccountOwner.  # noqa: E501


        :return: The account_guid of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._account_guid

    @account_guid.setter
    def account_guid(self, account_guid):
        """Sets the account_guid of this AccountOwner.


        :param account_guid: The account_guid of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._account_guid = account_guid

    @property
    def address(self):
        """Gets the address of this AccountOwner.  # noqa: E501


        :return: The address of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccountOwner.


        :param address: The address of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this AccountOwner.  # noqa: E501


        :return: The city of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AccountOwner.


        :param city: The city of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this AccountOwner.  # noqa: E501


        :return: The country of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AccountOwner.


        :param country: The country of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this AccountOwner.  # noqa: E501


        :return: The email of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountOwner.


        :param email: The email of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def guid(self):
        """Gets the guid of this AccountOwner.  # noqa: E501


        :return: The guid of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this AccountOwner.


        :param guid: The guid of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def member_guid(self):
        """Gets the member_guid of this AccountOwner.  # noqa: E501


        :return: The member_guid of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._member_guid

    @member_guid.setter
    def member_guid(self, member_guid):
        """Sets the member_guid of this AccountOwner.


        :param member_guid: The member_guid of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._member_guid = member_guid

    @property
    def owner_name(self):
        """Gets the owner_name of this AccountOwner.  # noqa: E501


        :return: The owner_name of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this AccountOwner.


        :param owner_name: The owner_name of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def postal_code(self):
        """Gets the postal_code of this AccountOwner.  # noqa: E501


        :return: The postal_code of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AccountOwner.


        :param postal_code: The postal_code of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this AccountOwner.  # noqa: E501


        :return: The state of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AccountOwner.


        :param state: The state of this AccountOwner.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def user_guid(self):
        """Gets the user_guid of this AccountOwner.  # noqa: E501


        :return: The user_guid of this AccountOwner.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this AccountOwner.


        :param user_guid: The user_guid of this AccountOwner.  # noqa: E501
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
        if issubclass(AccountOwner, dict):
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
        if not isinstance(other, AccountOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
