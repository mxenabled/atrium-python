# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Statement(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'account_guid': 'str',
        'content_hash': 'str',
        'created_at': 'str',
        'guid': 'str',
        'member_guid': 'str',
        'uri': 'str',
        'user_guid': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'account_guid': 'account_guid',
        'content_hash': 'content_hash',
        'created_at': 'created_at',
        'guid': 'guid',
        'member_guid': 'member_guid',
        'uri': 'uri',
        'user_guid': 'user_guid',
        'updated_at': 'updated_at'
    }

    def __init__(self, account_guid=None, content_hash=None, created_at=None, guid=None, member_guid=None, uri=None, user_guid=None, updated_at=None):  # noqa: E501

        self._account_guid = None
        self._content_hash = None
        self._created_at = None
        self._guid = None
        self._member_guid = None
        self._uri = None
        self._user_guid = None
        self._updated_at = None
        self.discriminator = None

        if account_guid is not None:
            self.account_guid = account_guid
        if content_hash is not None:
            self.content_hash = content_hash
        if created_at is not None:
            self.created_at = created_at
        if guid is not None:
            self.guid = guid
        if member_guid is not None:
            self.member_guid = member_guid
        if uri is not None:
            self.uri = uri
        if user_guid is not None:
            self.user_guid = user_guid
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def account_guid(self):
        """Gets the account_guid of this Statement.  # noqa: E501

        The unique identifier for the `account` associated with the `statement`. Defined by MX.  # noqa: E501

        :return: The account_guid of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._account_guid

    @account_guid.setter
    def account_guid(self, account_guid):
        """Sets the account_guid of this Statement.

        The unique identifier for the `account` associated with the `statement`. Defined by MX.  # noqa: E501

        :param account_guid: The account_guid of this Statement.  # noqa: E501
        :type: str
        """

        self._account_guid = account_guid

    @property
    def content_hash(self):
        """Gets the content_hash of this Statement.  # noqa: E501

        SHA256 digest of the pdf payload  # noqa: E501

        :return: The content_hash of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._content_hash

    @content_hash.setter
    def content_hash(self, content_hash):
        """Sets the content_hash of this Statement.

        SHA256 digest of the pdf payload  # noqa: E501

        :param content_hash: The content_hash of this Statement.  # noqa: E501
        :type: str
        """

        self._content_hash = content_hash

    @property
    def created_at(self):
        """Gets the created_at of this Statement.  # noqa: E501

        The date and time the `statement` was created.  # noqa: E501

        :return: The created_at of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Statement.

        The date and time the `statement` was created.  # noqa: E501

        :param created_at: The created_at of this Statement.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def guid(self):
        """Gets the guid of this Statement.  # noqa: E501

        The unique identifier for the `statement`. Defined by MX.  # noqa: E501

        :return: The guid of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Statement.

        The unique identifier for the `statement`. Defined by MX.  # noqa: E501

        :param guid: The guid of this Statement.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def member_guid(self):
        """Gets the member_guid of this Statement.  # noqa: E501

        The unique identifier for the `member` associated with the `statement`.  Defined by MX.  # noqa: E501

        :return: The member_guid of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._member_guid

    @member_guid.setter
    def member_guid(self, member_guid):
        """Sets the member_guid of this Statement.

        The unique identifier for the `member` associated with the `statement`.  Defined by MX.  # noqa: E501

        :param member_guid: The member_guid of this Statement.  # noqa: E501
        :type: str
        """

        self._member_guid = member_guid

    @property
    def uri(self):
        """Gets the uri of this Statement.  # noqa: E501

        A URI for accessing the byte payload of the `statement`.  # noqa: E501

        :return: The uri of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Statement.

        A URI for accessing the byte payload of the `statement`.  # noqa: E501

        :param uri: The uri of this Statement.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def user_guid(self):
        """Gets the user_guid of this Statement.  # noqa: E501

        The unique identifier for the `user` associated with the `statement`.  Defined by MX.  # noqa: E501

        :return: The user_guid of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this Statement.

        The unique identifier for the `user` associated with the `statement`.  Defined by MX.  # noqa: E501

        :param user_guid: The user_guid of this Statement.  # noqa: E501
        :type: str
        """

        self._user_guid = user_guid

    @property
    def updated_at(self):
        """Gets the updated_at of this Statement.  # noqa: E501

        The date and time at which the `statement` was last updated.  # noqa: E501

        :return: The updated_at of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Statement.

        The date and time at which the `statement` was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Statement.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(Statement, dict):
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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
