# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from atrium.models.challenge import Challenge  # noqa: F401,E501


class MemberConnectionStatus(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'aggregated_at': 'str',
        'challenges': 'list[Challenge]',
        'connection_status': 'str',
        'guid': 'str',
        'has_processed_accounts': 'bool',
        'has_processed_transactions': 'bool',
        'is_authenticated': 'bool',
        'is_being_aggregated': 'bool',
        'status': 'str',
        'successfully_aggregated_at': 'str'
    }

    attribute_map = {
        'aggregated_at': 'aggregated_at',
        'challenges': 'challenges',
        'connection_status': 'connection_status',
        'guid': 'guid',
        'has_processed_accounts': 'has_processed_accounts',
        'has_processed_transactions': 'has_processed_transactions',
        'is_authenticated': 'is_authenticated',
        'is_being_aggregated': 'is_being_aggregated',
        'status': 'status',
        'successfully_aggregated_at': 'successfully_aggregated_at'
    }

    def __init__(self, aggregated_at=None, challenges=None, connection_status=None, guid=None, has_processed_accounts=None, has_processed_transactions=None, is_authenticated=None, is_being_aggregated=None, status=None, successfully_aggregated_at=None):  # noqa: E501

        self._aggregated_at = None
        self._challenges = None
        self._connection_status = None
        self._guid = None
        self._has_processed_accounts = None
        self._has_processed_transactions = None
        self._is_authenticated = None
        self._is_being_aggregated = None
        self._status = None
        self._successfully_aggregated_at = None
        self.discriminator = None

        if aggregated_at is not None:
            self.aggregated_at = aggregated_at
        if challenges is not None:
            self.challenges = challenges
        if connection_status is not None:
            self.connection_status = connection_status
        if guid is not None:
            self.guid = guid
        if has_processed_accounts is not None:
            self.has_processed_accounts = has_processed_accounts
        if has_processed_transactions is not None:
            self.has_processed_transactions = has_processed_transactions
        if is_authenticated is not None:
            self.is_authenticated = is_authenticated
        if is_being_aggregated is not None:
            self.is_being_aggregated = is_being_aggregated
        if status is not None:
            self.status = status
        if successfully_aggregated_at is not None:
            self.successfully_aggregated_at = successfully_aggregated_at

    @property
    def aggregated_at(self):
        """Gets the aggregated_at of this MemberConnectionStatus.  # noqa: E501


        :return: The aggregated_at of this MemberConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._aggregated_at

    @aggregated_at.setter
    def aggregated_at(self, aggregated_at):
        """Sets the aggregated_at of this MemberConnectionStatus.


        :param aggregated_at: The aggregated_at of this MemberConnectionStatus.  # noqa: E501
        :type: str
        """

        self._aggregated_at = aggregated_at

    @property
    def challenges(self):
        """Gets the challenges of this MemberConnectionStatus.  # noqa: E501


        :return: The challenges of this MemberConnectionStatus.  # noqa: E501
        :rtype: list[Challenge]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """Sets the challenges of this MemberConnectionStatus.


        :param challenges: The challenges of this MemberConnectionStatus.  # noqa: E501
        :type: list[Challenge]
        """

        self._challenges = challenges

    @property
    def connection_status(self):
        """Gets the connection_status of this MemberConnectionStatus.  # noqa: E501


        :return: The connection_status of this MemberConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this MemberConnectionStatus.


        :param connection_status: The connection_status of this MemberConnectionStatus.  # noqa: E501
        :type: str
        """

        self._connection_status = connection_status

    @property
    def guid(self):
        """Gets the guid of this MemberConnectionStatus.  # noqa: E501


        :return: The guid of this MemberConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this MemberConnectionStatus.


        :param guid: The guid of this MemberConnectionStatus.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def has_processed_accounts(self):
        """Gets the has_processed_accounts of this MemberConnectionStatus.  # noqa: E501


        :return: The has_processed_accounts of this MemberConnectionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._has_processed_accounts

    @has_processed_accounts.setter
    def has_processed_accounts(self, has_processed_accounts):
        """Sets the has_processed_accounts of this MemberConnectionStatus.


        :param has_processed_accounts: The has_processed_accounts of this MemberConnectionStatus.  # noqa: E501
        :type: bool
        """

        self._has_processed_accounts = has_processed_accounts

    @property
    def has_processed_transactions(self):
        """Gets the has_processed_transactions of this MemberConnectionStatus.  # noqa: E501


        :return: The has_processed_transactions of this MemberConnectionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._has_processed_transactions

    @has_processed_transactions.setter
    def has_processed_transactions(self, has_processed_transactions):
        """Sets the has_processed_transactions of this MemberConnectionStatus.


        :param has_processed_transactions: The has_processed_transactions of this MemberConnectionStatus.  # noqa: E501
        :type: bool
        """

        self._has_processed_transactions = has_processed_transactions

    @property
    def is_authenticated(self):
        """Gets the is_authenticated of this MemberConnectionStatus.  # noqa: E501


        :return: The is_authenticated of this MemberConnectionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_authenticated

    @is_authenticated.setter
    def is_authenticated(self, is_authenticated):
        """Sets the is_authenticated of this MemberConnectionStatus.


        :param is_authenticated: The is_authenticated of this MemberConnectionStatus.  # noqa: E501
        :type: bool
        """

        self._is_authenticated = is_authenticated

    @property
    def is_being_aggregated(self):
        """Gets the is_being_aggregated of this MemberConnectionStatus.  # noqa: E501


        :return: The is_being_aggregated of this MemberConnectionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_being_aggregated

    @is_being_aggregated.setter
    def is_being_aggregated(self, is_being_aggregated):
        """Sets the is_being_aggregated of this MemberConnectionStatus.


        :param is_being_aggregated: The is_being_aggregated of this MemberConnectionStatus.  # noqa: E501
        :type: bool
        """

        self._is_being_aggregated = is_being_aggregated

    @property
    def status(self):
        """Gets the status of this MemberConnectionStatus.  # noqa: E501


        :return: The status of this MemberConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MemberConnectionStatus.


        :param status: The status of this MemberConnectionStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def successfully_aggregated_at(self):
        """Gets the successfully_aggregated_at of this MemberConnectionStatus.  # noqa: E501


        :return: The successfully_aggregated_at of this MemberConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._successfully_aggregated_at

    @successfully_aggregated_at.setter
    def successfully_aggregated_at(self, successfully_aggregated_at):
        """Sets the successfully_aggregated_at of this MemberConnectionStatus.


        :param successfully_aggregated_at: The successfully_aggregated_at of this MemberConnectionStatus.  # noqa: E501
        :type: str
        """

        self._successfully_aggregated_at = successfully_aggregated_at

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
        if issubclass(MemberConnectionStatus, dict):
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
        if not isinstance(other, MemberConnectionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
