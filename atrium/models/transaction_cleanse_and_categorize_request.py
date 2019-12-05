# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class TransactionCleanseAndCategorizeRequest(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'amount': 'float',
        'description': 'str',
        'identifier': 'str',
        'merchant_category_code': 'float',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'description': 'description',
        'identifier': 'identifier',
        'merchant_category_code': 'merchant_category_code',
        'type': 'type'
    }

    def __init__(self, amount=None, description=None, identifier=None, merchant_category_code=None, type=None):  # noqa: E501

        self._amount = None
        self._description = None
        self._identifier = None
        self._merchant_category_code = None
        self._type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if identifier is not None:
            self.identifier = identifier
        if merchant_category_code is not None:
            self.merchant_category_code = merchant_category_code
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this TransactionCleanseAndCategorizeRequest.  # noqa: E501


        :return: The amount of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionCleanseAndCategorizeRequest.


        :param amount: The amount of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this TransactionCleanseAndCategorizeRequest.  # noqa: E501


        :return: The description of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionCleanseAndCategorizeRequest.


        :param description: The description of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def identifier(self):
        """Gets the identifier of this TransactionCleanseAndCategorizeRequest.  # noqa: E501


        :return: The identifier of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TransactionCleanseAndCategorizeRequest.


        :param identifier: The identifier of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def merchant_category_code(self):
        """Gets the merchant_category_code of this TransactionCleanseAndCategorizeRequest.  # noqa: E501


        :return: The merchant_category_code of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :rtype: float
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """Sets the merchant_category_code of this TransactionCleanseAndCategorizeRequest.


        :param merchant_category_code: The merchant_category_code of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :type: float
        """

        self._merchant_category_code = merchant_category_code

    @property
    def type(self):
        """Gets the type of this TransactionCleanseAndCategorizeRequest.  # noqa: E501


        :return: The type of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionCleanseAndCategorizeRequest.


        :param type: The type of this TransactionCleanseAndCategorizeRequest.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(TransactionCleanseAndCategorizeRequest, dict):
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
        if not isinstance(other, TransactionCleanseAndCategorizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
