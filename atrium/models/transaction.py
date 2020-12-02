# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Transaction(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'account_guid': 'str',
        'amount': 'float',
        'category': 'str',
        'check_number': 'int',
        'check_number_string': 'str',
        'created_at': 'str',
        'currency_code': 'str',
        '_date': 'str',
        'description': 'str',
        'guid': 'str',
        'is_bill_pay': 'bool',
        'is_direct_deposit': 'bool',
        'is_expense': 'bool',
        'is_fee': 'bool',
        'is_income': 'bool',
        'is_international': 'bool',
        'is_overdraft_fee': 'bool',
        'is_payroll_advance': 'bool',
        'is_subscription': 'bool',
        'latitude': 'float',
        'longitude': 'float',
        'member_guid': 'str',
        'memo': 'str',
        'merchant_category_code': 'int',
        'merchant_guid': 'str',
        'original_description': 'str',
        'posted_at': 'str',
        'status': 'str',
        'top_level_category': 'str',
        'transacted_at': 'str',
        'type': 'str',
        'updated_at': 'str',
        'user_guid': 'str'
    }

    attribute_map = {
        'account_guid': 'account_guid',
        'amount': 'amount',
        'category': 'category',
        'check_number': 'check_number',
        'check_number_string': 'check_number_string',
        'created_at': 'created_at',
        'currency_code': 'currency_code',
        '_date': 'date',
        'description': 'description',
        'guid': 'guid',
        'is_bill_pay': 'is_bill_pay',
        'is_direct_deposit': 'is_direct_deposit',
        'is_expense': 'is_expense',
        'is_fee': 'is_fee',
        'is_income': 'is_income',
        'is_international': 'is_international',
        'is_overdraft_fee': 'is_overdraft_fee',
        'is_payroll_advance': 'is_payroll_advance',
        'is_subscription': 'is_subscription',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'member_guid': 'member_guid',
        'memo': 'memo',
        'merchant_category_code': 'merchant_category_code',
        'merchant_guid': 'merchant_guid',
        'original_description': 'original_description',
        'posted_at': 'posted_at',
        'status': 'status',
        'top_level_category': 'top_level_category',
        'transacted_at': 'transacted_at',
        'type': 'type',
        'updated_at': 'updated_at',
        'user_guid': 'user_guid'
    }

    def __init__(self, account_guid=None, amount=None, category=None, check_number=None, check_number_string=None, created_at=None, currency_code=None, _date=None, description=None, guid=None, is_bill_pay=None, is_direct_deposit=None, is_expense=None, is_fee=None, is_income=None, is_international=None, is_overdraft_fee=None, is_payroll_advance=None, is_subscription=None, latitude=None, longitude=None, member_guid=None, memo=None, merchant_category_code=None, merchant_guid=None, original_description=None, posted_at=None, status=None, top_level_category=None, transacted_at=None, type=None, updated_at=None, user_guid=None):  # noqa: E501

        self._account_guid = None
        self._amount = None
        self._category = None
        self._check_number = None
        self._check_number_string = None
        self._created_at = None
        self._currency_code = None
        self.__date = None
        self._description = None
        self._guid = None
        self._is_bill_pay = None
        self._is_direct_deposit = None
        self._is_expense = None
        self._is_fee = None
        self._is_income = None
        self._is_international = None
        self._is_overdraft_fee = None
        self._is_payroll_advance = None
        self._is_subscription = None
        self._latitude = None
        self._longitude = None
        self._member_guid = None
        self._memo = None
        self._merchant_category_code = None
        self._merchant_guid = None
        self._original_description = None
        self._posted_at = None
        self._status = None
        self._top_level_category = None
        self._transacted_at = None
        self._type = None
        self._updated_at = None
        self._user_guid = None
        self.discriminator = None

        if account_guid is not None:
            self.account_guid = account_guid
        if amount is not None:
            self.amount = amount
        if category is not None:
            self.category = category
        if check_number is not None:
            self.check_number = check_number
        if check_number_string is not None:
            self.check_number_string = check_number_string
        if created_at is not None:
            self.created_at = created_at
        if currency_code is not None:
            self.currency_code = currency_code
        if _date is not None:
            self._date = _date
        if description is not None:
            self.description = description
        if guid is not None:
            self.guid = guid
        if is_bill_pay is not None:
            self.is_bill_pay = is_bill_pay
        if is_direct_deposit is not None:
            self.is_direct_deposit = is_direct_deposit
        if is_expense is not None:
            self.is_expense = is_expense
        if is_fee is not None:
            self.is_fee = is_fee
        if is_income is not None:
            self.is_income = is_income
        if is_international is not None:
            self.is_international = is_international
        if is_overdraft_fee is not None:
            self.is_overdraft_fee = is_overdraft_fee
        if is_payroll_advance is not None:
            self.is_payroll_advance = is_payroll_advance
        if is_subscription is not None:
            self.is_subscription = is_subscription
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if member_guid is not None:
            self.member_guid = member_guid
        if memo is not None:
            self.memo = memo
        if merchant_category_code is not None:
            self.merchant_category_code = merchant_category_code
        if merchant_guid is not None:
            self.merchant_guid = merchant_guid
        if original_description is not None:
            self.original_description = original_description
        if posted_at is not None:
            self.posted_at = posted_at
        if status is not None:
            self.status = status
        if top_level_category is not None:
            self.top_level_category = top_level_category
        if transacted_at is not None:
            self.transacted_at = transacted_at
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if user_guid is not None:
            self.user_guid = user_guid

    @property
    def account_guid(self):
        """Gets the account_guid of this Transaction.  # noqa: E501


        :return: The account_guid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._account_guid

    @account_guid.setter
    def account_guid(self, account_guid):
        """Sets the account_guid of this Transaction.


        :param account_guid: The account_guid of this Transaction.  # noqa: E501
        :type: str
        """

        self._account_guid = account_guid

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501


        :return: The amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def category(self):
        """Gets the category of this Transaction.  # noqa: E501


        :return: The category of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Transaction.


        :param category: The category of this Transaction.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def check_number(self):
        """Gets the check_number of this Transaction.  # noqa: E501


        :return: The check_number of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._check_number

    @check_number.setter
    def check_number(self, check_number):
        """Sets the check_number of this Transaction.


        :param check_number: The check_number of this Transaction.  # noqa: E501
        :type: int
        """

        self._check_number = check_number

    @property
    def check_number_string(self):
        """Gets the check_number_string of this Transaction.  # noqa: E501


        :return: The check_number_string of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._check_number_string

    @check_number_string.setter
    def check_number_string(self, check_number_string):
        """Sets the check_number_string of this Transaction.


        :param check_number_string: The check_number_string of this Transaction.  # noqa: E501
        :type: str
        """

        self._check_number_string = check_number_string

    @property
    def created_at(self):
        """Gets the created_at of this Transaction.  # noqa: E501


        :return: The created_at of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Transaction.


        :param created_at: The created_at of this Transaction.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def currency_code(self):
        """Gets the currency_code of this Transaction.  # noqa: E501


        :return: The currency_code of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Transaction.


        :param currency_code: The currency_code of this Transaction.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def _date(self):
        """Gets the _date of this Transaction.  # noqa: E501


        :return: The _date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Transaction.


        :param _date: The _date of this Transaction.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this Transaction.  # noqa: E501


        :return: The description of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Transaction.


        :param description: The description of this Transaction.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def guid(self):
        """Gets the guid of this Transaction.  # noqa: E501


        :return: The guid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Transaction.


        :param guid: The guid of this Transaction.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def is_bill_pay(self):
        """Gets the is_bill_pay of this Transaction.  # noqa: E501


        :return: The is_bill_pay of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_bill_pay

    @is_bill_pay.setter
    def is_bill_pay(self, is_bill_pay):
        """Sets the is_bill_pay of this Transaction.


        :param is_bill_pay: The is_bill_pay of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_bill_pay = is_bill_pay

    @property
    def is_direct_deposit(self):
        """Gets the is_direct_deposit of this Transaction.  # noqa: E501


        :return: The is_direct_deposit of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_direct_deposit

    @is_direct_deposit.setter
    def is_direct_deposit(self, is_direct_deposit):
        """Sets the is_direct_deposit of this Transaction.


        :param is_direct_deposit: The is_direct_deposit of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_direct_deposit = is_direct_deposit

    @property
    def is_expense(self):
        """Gets the is_expense of this Transaction.  # noqa: E501


        :return: The is_expense of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_expense

    @is_expense.setter
    def is_expense(self, is_expense):
        """Sets the is_expense of this Transaction.


        :param is_expense: The is_expense of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_expense = is_expense

    @property
    def is_fee(self):
        """Gets the is_fee of this Transaction.  # noqa: E501


        :return: The is_fee of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_fee

    @is_fee.setter
    def is_fee(self, is_fee):
        """Sets the is_fee of this Transaction.


        :param is_fee: The is_fee of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_fee = is_fee

    @property
    def is_income(self):
        """Gets the is_income of this Transaction.  # noqa: E501


        :return: The is_income of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_income

    @is_income.setter
    def is_income(self, is_income):
        """Sets the is_income of this Transaction.


        :param is_income: The is_income of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_income = is_income

    @property
    def is_international(self):
        """Gets the is_international of this Transaction.  # noqa: E501


        :return: The is_international of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this Transaction.


        :param is_international: The is_international of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

    @property
    def is_overdraft_fee(self):
        """Gets the is_overdraft_fee of this Transaction.  # noqa: E501


        :return: The is_overdraft_fee of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_overdraft_fee

    @is_overdraft_fee.setter
    def is_overdraft_fee(self, is_overdraft_fee):
        """Sets the is_overdraft_fee of this Transaction.


        :param is_overdraft_fee: The is_overdraft_fee of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_overdraft_fee = is_overdraft_fee

    @property
    def is_payroll_advance(self):
        """Gets the is_payroll_advance of this Transaction.  # noqa: E501


        :return: The is_payroll_advance of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_payroll_advance

    @is_payroll_advance.setter
    def is_payroll_advance(self, is_payroll_advance):
        """Sets the is_payroll_advance of this Transaction.


        :param is_payroll_advance: The is_payroll_advance of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_payroll_advance = is_payroll_advance

    @property
    def is_subscription(self):
        """Gets the is_subscription of this Transaction.  # noqa: E501


        :return: The is_subscription of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscription

    @is_subscription.setter
    def is_subscription(self, is_subscription):
        """Sets the is_subscription of this Transaction.


        :param is_subscription: The is_subscription of this Transaction.  # noqa: E501
        :type: bool
        """

        self._is_subscription = is_subscription

    @property
    def latitude(self):
        """Gets the latitude of this Transaction.  # noqa: E501


        :return: The latitude of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Transaction.


        :param latitude: The latitude of this Transaction.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Transaction.  # noqa: E501


        :return: The longitude of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Transaction.


        :param longitude: The longitude of this Transaction.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def member_guid(self):
        """Gets the member_guid of this Transaction.  # noqa: E501


        :return: The member_guid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._member_guid

    @member_guid.setter
    def member_guid(self, member_guid):
        """Sets the member_guid of this Transaction.


        :param member_guid: The member_guid of this Transaction.  # noqa: E501
        :type: str
        """

        self._member_guid = member_guid

    @property
    def memo(self):
        """Gets the memo of this Transaction.  # noqa: E501


        :return: The memo of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this Transaction.


        :param memo: The memo of this Transaction.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def merchant_category_code(self):
        """Gets the merchant_category_code of this Transaction.  # noqa: E501


        :return: The merchant_category_code of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """Sets the merchant_category_code of this Transaction.


        :param merchant_category_code: The merchant_category_code of this Transaction.  # noqa: E501
        :type: int
        """

        self._merchant_category_code = merchant_category_code

    @property
    def merchant_guid(self):
        """Gets the merchant_guid of this Transaction.  # noqa: E501


        :return: The merchant_guid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._merchant_guid

    @merchant_guid.setter
    def merchant_guid(self, merchant_guid):
        """Sets the merchant_guid of this Transaction.


        :param merchant_guid: The merchant_guid of this Transaction.  # noqa: E501
        :type: str
        """

        self._merchant_guid = merchant_guid

    @property
    def original_description(self):
        """Gets the original_description of this Transaction.  # noqa: E501


        :return: The original_description of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._original_description

    @original_description.setter
    def original_description(self, original_description):
        """Sets the original_description of this Transaction.


        :param original_description: The original_description of this Transaction.  # noqa: E501
        :type: str
        """

        self._original_description = original_description

    @property
    def posted_at(self):
        """Gets the posted_at of this Transaction.  # noqa: E501


        :return: The posted_at of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._posted_at

    @posted_at.setter
    def posted_at(self, posted_at):
        """Sets the posted_at of this Transaction.


        :param posted_at: The posted_at of this Transaction.  # noqa: E501
        :type: str
        """

        self._posted_at = posted_at

    @property
    def status(self):
        """Gets the status of this Transaction.  # noqa: E501


        :return: The status of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Transaction.


        :param status: The status of this Transaction.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def top_level_category(self):
        """Gets the top_level_category of this Transaction.  # noqa: E501


        :return: The top_level_category of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._top_level_category

    @top_level_category.setter
    def top_level_category(self, top_level_category):
        """Sets the top_level_category of this Transaction.


        :param top_level_category: The top_level_category of this Transaction.  # noqa: E501
        :type: str
        """

        self._top_level_category = top_level_category

    @property
    def transacted_at(self):
        """Gets the transacted_at of this Transaction.  # noqa: E501


        :return: The transacted_at of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transacted_at

    @transacted_at.setter
    def transacted_at(self, transacted_at):
        """Sets the transacted_at of this Transaction.


        :param transacted_at: The transacted_at of this Transaction.  # noqa: E501
        :type: str
        """

        self._transacted_at = transacted_at

    @property
    def type(self):
        """Gets the type of this Transaction.  # noqa: E501


        :return: The type of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transaction.


        :param type: The type of this Transaction.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Transaction.  # noqa: E501


        :return: The updated_at of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Transaction.


        :param updated_at: The updated_at of this Transaction.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user_guid(self):
        """Gets the user_guid of this Transaction.  # noqa: E501


        :return: The user_guid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this Transaction.


        :param user_guid: The user_guid of this Transaction.  # noqa: E501
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
        if issubclass(Transaction, dict):
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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
