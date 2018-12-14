# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class TransactionCleanseAndCategorizeResponse(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'amount': 'float',
        'category': 'str',
        'description': 'str',
        'identifier': 'str',
        'type': 'str',
        'is_bill_pay': 'bool',
        'is_direct_deposit': 'bool',
        'is_expense': 'bool',
        'is_fee': 'bool',
        'is_income': 'bool',
        'is_international': 'bool',
        'is_overdraft_fee': 'bool',
        'is_payroll_advance': 'bool'
    }

    attribute_map = {
        'amount': 'amount',
        'category': 'category',
        'description': 'description',
        'identifier': 'identifier',
        'type': 'type',
        'is_bill_pay': 'is_bill_pay',
        'is_direct_deposit': 'is_direct_deposit',
        'is_expense': 'is_expense',
        'is_fee': 'is_fee',
        'is_income': 'is_income',
        'is_international': 'is_international',
        'is_overdraft_fee': 'is_overdraft_fee',
        'is_payroll_advance': 'is_payroll_advance'
    }

    def __init__(self, amount=None, category=None, description=None, identifier=None, type=None, is_bill_pay=None, is_direct_deposit=None, is_expense=None, is_fee=None, is_income=None, is_international=None, is_overdraft_fee=None, is_payroll_advance=None):  # noqa: E501

        self._amount = None
        self._category = None
        self._description = None
        self._identifier = None
        self._type = None
        self._is_bill_pay = None
        self._is_direct_deposit = None
        self._is_expense = None
        self._is_fee = None
        self._is_income = None
        self._is_international = None
        self._is_overdraft_fee = None
        self._is_payroll_advance = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if identifier is not None:
            self.identifier = identifier
        if type is not None:
            self.type = type
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

    @property
    def amount(self):
        """Gets the amount of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The amount of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionCleanseAndCategorizeResponse.


        :param amount: The amount of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def category(self):
        """Gets the category of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The category of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TransactionCleanseAndCategorizeResponse.


        :param category: The category of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The description of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionCleanseAndCategorizeResponse.


        :param description: The description of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def identifier(self):
        """Gets the identifier of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The identifier of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TransactionCleanseAndCategorizeResponse.


        :param identifier: The identifier of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def type(self):
        """Gets the type of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The type of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionCleanseAndCategorizeResponse.


        :param type: The type of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def is_bill_pay(self):
        """Gets the is_bill_pay of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_bill_pay of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_bill_pay

    @is_bill_pay.setter
    def is_bill_pay(self, is_bill_pay):
        """Sets the is_bill_pay of this TransactionCleanseAndCategorizeResponse.


        :param is_bill_pay: The is_bill_pay of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_bill_pay = is_bill_pay

    @property
    def is_direct_deposit(self):
        """Gets the is_direct_deposit of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_direct_deposit of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_direct_deposit

    @is_direct_deposit.setter
    def is_direct_deposit(self, is_direct_deposit):
        """Sets the is_direct_deposit of this TransactionCleanseAndCategorizeResponse.


        :param is_direct_deposit: The is_direct_deposit of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_direct_deposit = is_direct_deposit

    @property
    def is_expense(self):
        """Gets the is_expense of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_expense of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_expense

    @is_expense.setter
    def is_expense(self, is_expense):
        """Sets the is_expense of this TransactionCleanseAndCategorizeResponse.


        :param is_expense: The is_expense of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_expense = is_expense

    @property
    def is_fee(self):
        """Gets the is_fee of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_fee of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_fee

    @is_fee.setter
    def is_fee(self, is_fee):
        """Sets the is_fee of this TransactionCleanseAndCategorizeResponse.


        :param is_fee: The is_fee of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_fee = is_fee

    @property
    def is_income(self):
        """Gets the is_income of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_income of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_income

    @is_income.setter
    def is_income(self, is_income):
        """Sets the is_income of this TransactionCleanseAndCategorizeResponse.


        :param is_income: The is_income of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_income = is_income

    @property
    def is_international(self):
        """Gets the is_international of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_international of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this TransactionCleanseAndCategorizeResponse.


        :param is_international: The is_international of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

    @property
    def is_overdraft_fee(self):
        """Gets the is_overdraft_fee of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_overdraft_fee of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_overdraft_fee

    @is_overdraft_fee.setter
    def is_overdraft_fee(self, is_overdraft_fee):
        """Sets the is_overdraft_fee of this TransactionCleanseAndCategorizeResponse.


        :param is_overdraft_fee: The is_overdraft_fee of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_overdraft_fee = is_overdraft_fee

    @property
    def is_payroll_advance(self):
        """Gets the is_payroll_advance of this TransactionCleanseAndCategorizeResponse.  # noqa: E501


        :return: The is_payroll_advance of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_payroll_advance

    @is_payroll_advance.setter
    def is_payroll_advance(self, is_payroll_advance):
        """Sets the is_payroll_advance of this TransactionCleanseAndCategorizeResponse.


        :param is_payroll_advance: The is_payroll_advance of this TransactionCleanseAndCategorizeResponse.  # noqa: E501
        :type: bool
        """

        self._is_payroll_advance = is_payroll_advance

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
        if issubclass(TransactionCleanseAndCategorizeResponse, dict):
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
        if not isinstance(other, TransactionCleanseAndCategorizeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
