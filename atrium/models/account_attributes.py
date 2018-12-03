# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class AccountAttributes(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'apr': 'float',
        'apy': 'float',
        'available_balance': 'float',
        'available_credit': 'float',
        'balance': 'float',
        'created_at': 'str',
        'credit_limit': 'float',
        'currency_code': 'str',
        'day_payment_is_due': 'int',
        'guid': 'str',
        'institution_code': 'str',
        'interest_rate': 'float',
        'is_closed': 'bool',
        'last_payment': 'float',
        'matures_on': 'str',
        'member_guid': 'str',
        'minimum_balance': 'float',
        'minimum_payment': 'float',
        'name': 'str',
        'original_balance': 'float',
        'payment_due_at': 'str',
        'payoff_balance': 'float',
        'started_on': 'str',
        'subtype': 'str',
        'total_account_value': 'float',
        'type': 'str',
        'updated_at': 'str',
        'user_guid': 'str'
    }

    attribute_map = {
        'apr': 'apr',
        'apy': 'apy',
        'available_balance': 'available_balance',
        'available_credit': 'available_credit',
        'balance': 'balance',
        'created_at': 'created_at',
        'credit_limit': 'credit_limit',
        'currency_code': 'currency_code',
        'day_payment_is_due': 'day_payment_is_due',
        'guid': 'guid',
        'institution_code': 'institution_code',
        'interest_rate': 'interest_rate',
        'is_closed': 'is_closed',
        'last_payment': 'last_payment',
        'matures_on': 'matures_on',
        'member_guid': 'member_guid',
        'minimum_balance': 'minimum_balance',
        'minimum_payment': 'minimum_payment',
        'name': 'name',
        'original_balance': 'original_balance',
        'payment_due_at': 'payment_due_at',
        'payoff_balance': 'payoff_balance',
        'started_on': 'started_on',
        'subtype': 'subtype',
        'total_account_value': 'total_account_value',
        'type': 'type',
        'updated_at': 'updated_at',
        'user_guid': 'user_guid'
    }

    def __init__(self, apr=None, apy=None, available_balance=None, available_credit=None, balance=None, created_at=None, credit_limit=None, currency_code=None, day_payment_is_due=None, guid=None, institution_code=None, interest_rate=None, is_closed=None, last_payment=None, matures_on=None, member_guid=None, minimum_balance=None, minimum_payment=None, name=None, original_balance=None, payment_due_at=None, payoff_balance=None, started_on=None, subtype=None, total_account_value=None, type=None, updated_at=None, user_guid=None):  # noqa: E501

        self._apr = None
        self._apy = None
        self._available_balance = None
        self._available_credit = None
        self._balance = None
        self._created_at = None
        self._credit_limit = None
        self._currency_code = None
        self._day_payment_is_due = None
        self._guid = None
        self._institution_code = None
        self._interest_rate = None
        self._is_closed = None
        self._last_payment = None
        self._matures_on = None
        self._member_guid = None
        self._minimum_balance = None
        self._minimum_payment = None
        self._name = None
        self._original_balance = None
        self._payment_due_at = None
        self._payoff_balance = None
        self._started_on = None
        self._subtype = None
        self._total_account_value = None
        self._type = None
        self._updated_at = None
        self._user_guid = None
        self.discriminator = None

        if apr is not None:
            self.apr = apr
        if apy is not None:
            self.apy = apy
        if available_balance is not None:
            self.available_balance = available_balance
        if available_credit is not None:
            self.available_credit = available_credit
        if balance is not None:
            self.balance = balance
        if created_at is not None:
            self.created_at = created_at
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if currency_code is not None:
            self.currency_code = currency_code
        if day_payment_is_due is not None:
            self.day_payment_is_due = day_payment_is_due
        if guid is not None:
            self.guid = guid
        if institution_code is not None:
            self.institution_code = institution_code
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if is_closed is not None:
            self.is_closed = is_closed
        if last_payment is not None:
            self.last_payment = last_payment
        if matures_on is not None:
            self.matures_on = matures_on
        if member_guid is not None:
            self.member_guid = member_guid
        if minimum_balance is not None:
            self.minimum_balance = minimum_balance
        if minimum_payment is not None:
            self.minimum_payment = minimum_payment
        if name is not None:
            self.name = name
        if original_balance is not None:
            self.original_balance = original_balance
        if payment_due_at is not None:
            self.payment_due_at = payment_due_at
        if payoff_balance is not None:
            self.payoff_balance = payoff_balance
        if started_on is not None:
            self.started_on = started_on
        if subtype is not None:
            self.subtype = subtype
        if total_account_value is not None:
            self.total_account_value = total_account_value
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if user_guid is not None:
            self.user_guid = user_guid

    @property
    def apr(self):
        """Gets the apr of this AccountAttributes.  # noqa: E501


        :return: The apr of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._apr

    @apr.setter
    def apr(self, apr):
        """Sets the apr of this AccountAttributes.


        :param apr: The apr of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._apr = apr

    @property
    def apy(self):
        """Gets the apy of this AccountAttributes.  # noqa: E501


        :return: The apy of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._apy

    @apy.setter
    def apy(self, apy):
        """Sets the apy of this AccountAttributes.


        :param apy: The apy of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._apy = apy

    @property
    def available_balance(self):
        """Gets the available_balance of this AccountAttributes.  # noqa: E501


        :return: The available_balance of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this AccountAttributes.


        :param available_balance: The available_balance of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._available_balance = available_balance

    @property
    def available_credit(self):
        """Gets the available_credit of this AccountAttributes.  # noqa: E501


        :return: The available_credit of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._available_credit

    @available_credit.setter
    def available_credit(self, available_credit):
        """Sets the available_credit of this AccountAttributes.


        :param available_credit: The available_credit of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._available_credit = available_credit

    @property
    def balance(self):
        """Gets the balance of this AccountAttributes.  # noqa: E501


        :return: The balance of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountAttributes.


        :param balance: The balance of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def created_at(self):
        """Gets the created_at of this AccountAttributes.  # noqa: E501


        :return: The created_at of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountAttributes.


        :param created_at: The created_at of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def credit_limit(self):
        """Gets the credit_limit of this AccountAttributes.  # noqa: E501


        :return: The credit_limit of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this AccountAttributes.


        :param credit_limit: The credit_limit of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._credit_limit = credit_limit

    @property
    def currency_code(self):
        """Gets the currency_code of this AccountAttributes.  # noqa: E501


        :return: The currency_code of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AccountAttributes.


        :param currency_code: The currency_code of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def day_payment_is_due(self):
        """Gets the day_payment_is_due of this AccountAttributes.  # noqa: E501


        :return: The day_payment_is_due of this AccountAttributes.  # noqa: E501
        :rtype: int
        """
        return self._day_payment_is_due

    @day_payment_is_due.setter
    def day_payment_is_due(self, day_payment_is_due):
        """Sets the day_payment_is_due of this AccountAttributes.


        :param day_payment_is_due: The day_payment_is_due of this AccountAttributes.  # noqa: E501
        :type: int
        """

        self._day_payment_is_due = day_payment_is_due

    @property
    def guid(self):
        """Gets the guid of this AccountAttributes.  # noqa: E501


        :return: The guid of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this AccountAttributes.


        :param guid: The guid of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def institution_code(self):
        """Gets the institution_code of this AccountAttributes.  # noqa: E501


        :return: The institution_code of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._institution_code

    @institution_code.setter
    def institution_code(self, institution_code):
        """Sets the institution_code of this AccountAttributes.


        :param institution_code: The institution_code of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._institution_code = institution_code

    @property
    def interest_rate(self):
        """Gets the interest_rate of this AccountAttributes.  # noqa: E501


        :return: The interest_rate of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this AccountAttributes.


        :param interest_rate: The interest_rate of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._interest_rate = interest_rate

    @property
    def is_closed(self):
        """Gets the is_closed of this AccountAttributes.  # noqa: E501


        :return: The is_closed of this AccountAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this AccountAttributes.


        :param is_closed: The is_closed of this AccountAttributes.  # noqa: E501
        :type: bool
        """

        self._is_closed = is_closed

    @property
    def last_payment(self):
        """Gets the last_payment of this AccountAttributes.  # noqa: E501


        :return: The last_payment of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._last_payment

    @last_payment.setter
    def last_payment(self, last_payment):
        """Sets the last_payment of this AccountAttributes.


        :param last_payment: The last_payment of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._last_payment = last_payment

    @property
    def matures_on(self):
        """Gets the matures_on of this AccountAttributes.  # noqa: E501


        :return: The matures_on of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._matures_on

    @matures_on.setter
    def matures_on(self, matures_on):
        """Sets the matures_on of this AccountAttributes.


        :param matures_on: The matures_on of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._matures_on = matures_on

    @property
    def member_guid(self):
        """Gets the member_guid of this AccountAttributes.  # noqa: E501


        :return: The member_guid of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._member_guid

    @member_guid.setter
    def member_guid(self, member_guid):
        """Sets the member_guid of this AccountAttributes.


        :param member_guid: The member_guid of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._member_guid = member_guid

    @property
    def minimum_balance(self):
        """Gets the minimum_balance of this AccountAttributes.  # noqa: E501


        :return: The minimum_balance of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, minimum_balance):
        """Sets the minimum_balance of this AccountAttributes.


        :param minimum_balance: The minimum_balance of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._minimum_balance = minimum_balance

    @property
    def minimum_payment(self):
        """Gets the minimum_payment of this AccountAttributes.  # noqa: E501


        :return: The minimum_payment of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._minimum_payment

    @minimum_payment.setter
    def minimum_payment(self, minimum_payment):
        """Sets the minimum_payment of this AccountAttributes.


        :param minimum_payment: The minimum_payment of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._minimum_payment = minimum_payment

    @property
    def name(self):
        """Gets the name of this AccountAttributes.  # noqa: E501


        :return: The name of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountAttributes.


        :param name: The name of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_balance(self):
        """Gets the original_balance of this AccountAttributes.  # noqa: E501


        :return: The original_balance of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._original_balance

    @original_balance.setter
    def original_balance(self, original_balance):
        """Sets the original_balance of this AccountAttributes.


        :param original_balance: The original_balance of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._original_balance = original_balance

    @property
    def payment_due_at(self):
        """Gets the payment_due_at of this AccountAttributes.  # noqa: E501


        :return: The payment_due_at of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._payment_due_at

    @payment_due_at.setter
    def payment_due_at(self, payment_due_at):
        """Sets the payment_due_at of this AccountAttributes.


        :param payment_due_at: The payment_due_at of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._payment_due_at = payment_due_at

    @property
    def payoff_balance(self):
        """Gets the payoff_balance of this AccountAttributes.  # noqa: E501


        :return: The payoff_balance of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._payoff_balance

    @payoff_balance.setter
    def payoff_balance(self, payoff_balance):
        """Sets the payoff_balance of this AccountAttributes.


        :param payoff_balance: The payoff_balance of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._payoff_balance = payoff_balance

    @property
    def started_on(self):
        """Gets the started_on of this AccountAttributes.  # noqa: E501


        :return: The started_on of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._started_on

    @started_on.setter
    def started_on(self, started_on):
        """Sets the started_on of this AccountAttributes.


        :param started_on: The started_on of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._started_on = started_on

    @property
    def subtype(self):
        """Gets the subtype of this AccountAttributes.  # noqa: E501


        :return: The subtype of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this AccountAttributes.


        :param subtype: The subtype of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def total_account_value(self):
        """Gets the total_account_value of this AccountAttributes.  # noqa: E501


        :return: The total_account_value of this AccountAttributes.  # noqa: E501
        :rtype: float
        """
        return self._total_account_value

    @total_account_value.setter
    def total_account_value(self, total_account_value):
        """Sets the total_account_value of this AccountAttributes.


        :param total_account_value: The total_account_value of this AccountAttributes.  # noqa: E501
        :type: float
        """

        self._total_account_value = total_account_value

    @property
    def type(self):
        """Gets the type of this AccountAttributes.  # noqa: E501


        :return: The type of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountAttributes.


        :param type: The type of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this AccountAttributes.  # noqa: E501


        :return: The updated_at of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AccountAttributes.


        :param updated_at: The updated_at of this AccountAttributes.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user_guid(self):
        """Gets the user_guid of this AccountAttributes.  # noqa: E501


        :return: The user_guid of this AccountAttributes.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this AccountAttributes.


        :param user_guid: The user_guid of this AccountAttributes.  # noqa: E501
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
        if issubclass(AccountAttributes, dict):
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
        if not isinstance(other, AccountAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other