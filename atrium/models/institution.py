# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Institution(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'code': 'str',
        'medium_logo_url': 'str',
        'name': 'str',
        'small_logo_url': 'str',
        'supports_account_identification': 'bool',
        'supports_account_statement': 'bool',
        'supports_account_verification': 'bool',
        'supports_transaction_history': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'code': 'code',
        'medium_logo_url': 'medium_logo_url',
        'name': 'name',
        'small_logo_url': 'small_logo_url',
        'supports_account_identification': 'supports_account_identification',
        'supports_account_statement': 'supports_account_statement',
        'supports_account_verification': 'supports_account_verification',
        'supports_transaction_history': 'supports_transaction_history',
        'url': 'url'
    }

    def __init__(self, code=None, medium_logo_url=None, name=None, small_logo_url=None, supports_account_identification=None, supports_account_statement=None, supports_account_verification=None, supports_transaction_history=None, url=None):  # noqa: E501

        self._code = None
        self._medium_logo_url = None
        self._name = None
        self._small_logo_url = None
        self._supports_account_identification = None
        self._supports_account_statement = None
        self._supports_account_verification = None
        self._supports_transaction_history = None
        self._url = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if medium_logo_url is not None:
            self.medium_logo_url = medium_logo_url
        if name is not None:
            self.name = name
        if small_logo_url is not None:
            self.small_logo_url = small_logo_url
        if supports_account_identification is not None:
            self.supports_account_identification = supports_account_identification
        if supports_account_statement is not None:
            self.supports_account_statement = supports_account_statement
        if supports_account_verification is not None:
            self.supports_account_verification = supports_account_verification
        if supports_transaction_history is not None:
            self.supports_transaction_history = supports_transaction_history
        if url is not None:
            self.url = url

    @property
    def code(self):
        """Gets the code of this Institution.  # noqa: E501


        :return: The code of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Institution.


        :param code: The code of this Institution.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def medium_logo_url(self):
        """Gets the medium_logo_url of this Institution.  # noqa: E501


        :return: The medium_logo_url of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._medium_logo_url

    @medium_logo_url.setter
    def medium_logo_url(self, medium_logo_url):
        """Sets the medium_logo_url of this Institution.


        :param medium_logo_url: The medium_logo_url of this Institution.  # noqa: E501
        :type: str
        """

        self._medium_logo_url = medium_logo_url

    @property
    def name(self):
        """Gets the name of this Institution.  # noqa: E501


        :return: The name of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Institution.


        :param name: The name of this Institution.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def small_logo_url(self):
        """Gets the small_logo_url of this Institution.  # noqa: E501


        :return: The small_logo_url of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._small_logo_url

    @small_logo_url.setter
    def small_logo_url(self, small_logo_url):
        """Sets the small_logo_url of this Institution.


        :param small_logo_url: The small_logo_url of this Institution.  # noqa: E501
        :type: str
        """

        self._small_logo_url = small_logo_url

    @property
    def supports_account_identification(self):
        """Gets the supports_account_identification of this Institution.  # noqa: E501


        :return: The supports_account_identification of this Institution.  # noqa: E501
        :rtype: bool
        """
        return self._supports_account_identification

    @supports_account_identification.setter
    def supports_account_identification(self, supports_account_identification):
        """Sets the supports_account_identification of this Institution.


        :param supports_account_identification: The supports_account_identification of this Institution.  # noqa: E501
        :type: bool
        """

        self._supports_account_identification = supports_account_identification

    @property
    def supports_account_statement(self):
        """Gets the supports_account_statement of this Institution.  # noqa: E501


        :return: The supports_account_statement of this Institution.  # noqa: E501
        :rtype: bool
        """
        return self._supports_account_statement

    @supports_account_statement.setter
    def supports_account_statement(self, supports_account_statement):
        """Sets the supports_account_statement of this Institution.


        :param supports_account_statement: The supports_account_statement of this Institution.  # noqa: E501
        :type: bool
        """

        self._supports_account_statement = supports_account_statement

    @property
    def supports_account_verification(self):
        """Gets the supports_account_verification of this Institution.  # noqa: E501


        :return: The supports_account_verification of this Institution.  # noqa: E501
        :rtype: bool
        """
        return self._supports_account_verification

    @supports_account_verification.setter
    def supports_account_verification(self, supports_account_verification):
        """Sets the supports_account_verification of this Institution.


        :param supports_account_verification: The supports_account_verification of this Institution.  # noqa: E501
        :type: bool
        """

        self._supports_account_verification = supports_account_verification

    @property
    def supports_transaction_history(self):
        """Gets the supports_transaction_history of this Institution.  # noqa: E501


        :return: The supports_transaction_history of this Institution.  # noqa: E501
        :rtype: bool
        """
        return self._supports_transaction_history

    @supports_transaction_history.setter
    def supports_transaction_history(self, supports_transaction_history):
        """Sets the supports_transaction_history of this Institution.


        :param supports_transaction_history: The supports_transaction_history of this Institution.  # noqa: E501
        :type: bool
        """

        self._supports_transaction_history = supports_transaction_history

    @property
    def url(self):
        """Gets the url of this Institution.  # noqa: E501


        :return: The url of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Institution.


        :param url: The url of this Institution.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Institution, dict):
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
        if not isinstance(other, Institution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
