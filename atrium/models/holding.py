# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Holding(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'account_guid': 'str',
        'cost_basis': 'float',
        'created_at': 'str',
        'currency_code': 'str',
        'cusip': 'str',
        'daily_change': 'float',
        'description': 'str',
        'guid': 'str',
        'holding_type': 'str',
        'market_value': 'float',
        'member_guid': 'str',
        'purchase_price': 'float',
        'shares': 'float',
        'symbol': 'str',
        'updated_at': 'str',
        'user_guid': 'str'
    }

    attribute_map = {
        'account_guid': 'account_guid',
        'cost_basis': 'cost_basis',
        'created_at': 'created_at',
        'currency_code': 'currency_code',
        'cusip': 'cusip',
        'daily_change': 'daily_change',
        'description': 'description',
        'guid': 'guid',
        'holding_type': 'holding_type',
        'market_value': 'market_value',
        'member_guid': 'member_guid',
        'purchase_price': 'purchase_price',
        'shares': 'shares',
        'symbol': 'symbol',
        'updated_at': 'updated_at',
        'user_guid': 'user_guid'
    }

    def __init__(self, account_guid=None, cost_basis=None, created_at=None, currency_code=None, cusip=None, daily_change=None, description=None, guid=None, holding_type=None, market_value=None, member_guid=None, purchase_price=None, shares=None, symbol=None, updated_at=None, user_guid=None):  # noqa: E501

        self._account_guid = None
        self._cost_basis = None
        self._created_at = None
        self._currency_code = None
        self._cusip = None
        self._daily_change = None
        self._description = None
        self._guid = None
        self._holding_type = None
        self._market_value = None
        self._member_guid = None
        self._purchase_price = None
        self._shares = None
        self._symbol = None
        self._updated_at = None
        self._user_guid = None
        self.discriminator = None

        if account_guid is not None:
            self.account_guid = account_guid
        if cost_basis is not None:
            self.cost_basis = cost_basis
        if created_at is not None:
            self.created_at = created_at
        if currency_code is not None:
            self.currency_code = currency_code
        if cusip is not None:
            self.cusip = cusip
        if daily_change is not None:
            self.daily_change = daily_change
        if description is not None:
            self.description = description
        if guid is not None:
            self.guid = guid
        if holding_type is not None:
            self.holding_type = holding_type
        if market_value is not None:
            self.market_value = market_value
        if member_guid is not None:
            self.member_guid = member_guid
        if purchase_price is not None:
            self.purchase_price = purchase_price
        if shares is not None:
            self.shares = shares
        if symbol is not None:
            self.symbol = symbol
        if updated_at is not None:
            self.updated_at = updated_at
        if user_guid is not None:
            self.user_guid = user_guid

    @property
    def account_guid(self):
        """Gets the account_guid of this Holding.  # noqa: E501


        :return: The account_guid of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._account_guid

    @account_guid.setter
    def account_guid(self, account_guid):
        """Sets the account_guid of this Holding.


        :param account_guid: The account_guid of this Holding.  # noqa: E501
        :type: str
        """

        self._account_guid = account_guid

    @property
    def cost_basis(self):
        """Gets the cost_basis of this Holding.  # noqa: E501


        :return: The cost_basis of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._cost_basis

    @cost_basis.setter
    def cost_basis(self, cost_basis):
        """Sets the cost_basis of this Holding.


        :param cost_basis: The cost_basis of this Holding.  # noqa: E501
        :type: float
        """

        self._cost_basis = cost_basis

    @property
    def created_at(self):
        """Gets the created_at of this Holding.  # noqa: E501


        :return: The created_at of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Holding.


        :param created_at: The created_at of this Holding.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def currency_code(self):
        """Gets the currency_code of this Holding.  # noqa: E501


        :return: The currency_code of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Holding.


        :param currency_code: The currency_code of this Holding.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def cusip(self):
        """Gets the cusip of this Holding.  # noqa: E501


        :return: The cusip of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._cusip

    @cusip.setter
    def cusip(self, cusip):
        """Sets the cusip of this Holding.


        :param cusip: The cusip of this Holding.  # noqa: E501
        :type: str
        """

        self._cusip = cusip

    @property
    def daily_change(self):
        """Gets the daily_change of this Holding.  # noqa: E501


        :return: The daily_change of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._daily_change

    @daily_change.setter
    def daily_change(self, daily_change):
        """Sets the daily_change of this Holding.


        :param daily_change: The daily_change of this Holding.  # noqa: E501
        :type: float
        """

        self._daily_change = daily_change

    @property
    def description(self):
        """Gets the description of this Holding.  # noqa: E501


        :return: The description of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Holding.


        :param description: The description of this Holding.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def guid(self):
        """Gets the guid of this Holding.  # noqa: E501


        :return: The guid of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Holding.


        :param guid: The guid of this Holding.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def holding_type(self):
        """Gets the holding_type of this Holding.  # noqa: E501


        :return: The holding_type of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._holding_type

    @holding_type.setter
    def holding_type(self, holding_type):
        """Sets the holding_type of this Holding.


        :param holding_type: The holding_type of this Holding.  # noqa: E501
        :type: str
        """

        self._holding_type = holding_type

    @property
    def market_value(self):
        """Gets the market_value of this Holding.  # noqa: E501


        :return: The market_value of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this Holding.


        :param market_value: The market_value of this Holding.  # noqa: E501
        :type: float
        """

        self._market_value = market_value

    @property
    def member_guid(self):
        """Gets the member_guid of this Holding.  # noqa: E501


        :return: The member_guid of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._member_guid

    @member_guid.setter
    def member_guid(self, member_guid):
        """Sets the member_guid of this Holding.


        :param member_guid: The member_guid of this Holding.  # noqa: E501
        :type: str
        """

        self._member_guid = member_guid

    @property
    def purchase_price(self):
        """Gets the purchase_price of this Holding.  # noqa: E501


        :return: The purchase_price of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this Holding.


        :param purchase_price: The purchase_price of this Holding.  # noqa: E501
        :type: float
        """

        self._purchase_price = purchase_price

    @property
    def shares(self):
        """Gets the shares of this Holding.  # noqa: E501


        :return: The shares of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this Holding.


        :param shares: The shares of this Holding.  # noqa: E501
        :type: float
        """

        self._shares = shares

    @property
    def symbol(self):
        """Gets the symbol of this Holding.  # noqa: E501


        :return: The symbol of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Holding.


        :param symbol: The symbol of this Holding.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def updated_at(self):
        """Gets the updated_at of this Holding.  # noqa: E501


        :return: The updated_at of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Holding.


        :param updated_at: The updated_at of this Holding.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user_guid(self):
        """Gets the user_guid of this Holding.  # noqa: E501


        :return: The user_guid of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this Holding.


        :param user_guid: The user_guid of this Holding.  # noqa: E501
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
        if issubclass(Holding, dict):
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
        if not isinstance(other, Holding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
