# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Member(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'aggregated_at': 'str',
        'connection_status': 'str',
        'guid': 'str',
        'identifier': 'str',
        'institution_code': 'str',
        'is_being_aggregated': 'bool',
        'metadata': 'str',
        'name': 'str',
        'oauth_window_uri': 'str',
        'status': 'str',
        'successfully_aggregated_at': 'str',
        'user_guid': 'str'
    }

    attribute_map = {
        'aggregated_at': 'aggregated_at',
        'connection_status': 'connection_status',
        'guid': 'guid',
        'identifier': 'identifier',
        'institution_code': 'institution_code',
        'is_being_aggregated': 'is_being_aggregated',
        'metadata': 'metadata',
        'name': 'name',
        'oauth_window_uri': 'oauth_window_uri',
        'status': 'status',
        'successfully_aggregated_at': 'successfully_aggregated_at',
        'user_guid': 'user_guid'
    }

    def __init__(self, aggregated_at=None, connection_status=None, guid=None, identifier=None, institution_code=None, is_being_aggregated=None, metadata=None, name=None, oauth_window_uri=None, status=None, successfully_aggregated_at=None, user_guid=None):  # noqa: E501

        self._aggregated_at = None
        self._connection_status = None
        self._guid = None
        self._identifier = None
        self._institution_code = None
        self._is_being_aggregated = None
        self._metadata = None
        self._name = None
        self._oauth_window_uri = None
        self._status = None
        self._successfully_aggregated_at = None
        self._user_guid = None
        self.discriminator = None

        if aggregated_at is not None:
            self.aggregated_at = aggregated_at
        if connection_status is not None:
            self.connection_status = connection_status
        if guid is not None:
            self.guid = guid
        if identifier is not None:
            self.identifier = identifier
        if institution_code is not None:
            self.institution_code = institution_code
        if is_being_aggregated is not None:
            self.is_being_aggregated = is_being_aggregated
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if oauth_window_uri is not None:
            self.oauth_window_uri = oauth_window_uri
        if status is not None:
            self.status = status
        if successfully_aggregated_at is not None:
            self.successfully_aggregated_at = successfully_aggregated_at
        if user_guid is not None:
            self.user_guid = user_guid

    @property
    def aggregated_at(self):
        """Gets the aggregated_at of this Member.  # noqa: E501


        :return: The aggregated_at of this Member.  # noqa: E501
        :rtype: str
        """
        return self._aggregated_at

    @aggregated_at.setter
    def aggregated_at(self, aggregated_at):
        """Sets the aggregated_at of this Member.


        :param aggregated_at: The aggregated_at of this Member.  # noqa: E501
        :type: str
        """

        self._aggregated_at = aggregated_at

    @property
    def connection_status(self):
        """Gets the connection_status of this Member.  # noqa: E501


        :return: The connection_status of this Member.  # noqa: E501
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this Member.


        :param connection_status: The connection_status of this Member.  # noqa: E501
        :type: str
        """

        self._connection_status = connection_status

    @property
    def guid(self):
        """Gets the guid of this Member.  # noqa: E501


        :return: The guid of this Member.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Member.


        :param guid: The guid of this Member.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def identifier(self):
        """Gets the identifier of this Member.  # noqa: E501


        :return: The identifier of this Member.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Member.


        :param identifier: The identifier of this Member.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def institution_code(self):
        """Gets the institution_code of this Member.  # noqa: E501


        :return: The institution_code of this Member.  # noqa: E501
        :rtype: str
        """
        return self._institution_code

    @institution_code.setter
    def institution_code(self, institution_code):
        """Sets the institution_code of this Member.


        :param institution_code: The institution_code of this Member.  # noqa: E501
        :type: str
        """

        self._institution_code = institution_code

    @property
    def is_being_aggregated(self):
        """Gets the is_being_aggregated of this Member.  # noqa: E501


        :return: The is_being_aggregated of this Member.  # noqa: E501
        :rtype: bool
        """
        return self._is_being_aggregated

    @is_being_aggregated.setter
    def is_being_aggregated(self, is_being_aggregated):
        """Sets the is_being_aggregated of this Member.


        :param is_being_aggregated: The is_being_aggregated of this Member.  # noqa: E501
        :type: bool
        """

        self._is_being_aggregated = is_being_aggregated

    @property
    def metadata(self):
        """Gets the metadata of this Member.  # noqa: E501


        :return: The metadata of this Member.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Member.


        :param metadata: The metadata of this Member.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this Member.  # noqa: E501


        :return: The name of this Member.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Member.


        :param name: The name of this Member.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oauth_window_uri(self):
        """Gets the oauth_window_uri of this Member.  # noqa: E501


        :return: The oauth_window_uri of this Member.  # noqa: E501
        :rtype: str
        """
        return self._oauth_window_uri

    @oauth_window_uri.setter
    def oauth_window_uri(self, oauth_window_uri):
        """Sets the oauth_window_uri of this Member.


        :param oauth_window_uri: The oauth_window_uri of this Member.  # noqa: E501
        :type: str
        """

        self._oauth_window_uri = oauth_window_uri

    @property
    def status(self):
        """Gets the status of this Member.  # noqa: E501


        :return: The status of this Member.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Member.


        :param status: The status of this Member.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def successfully_aggregated_at(self):
        """Gets the successfully_aggregated_at of this Member.  # noqa: E501


        :return: The successfully_aggregated_at of this Member.  # noqa: E501
        :rtype: str
        """
        return self._successfully_aggregated_at

    @successfully_aggregated_at.setter
    def successfully_aggregated_at(self, successfully_aggregated_at):
        """Sets the successfully_aggregated_at of this Member.


        :param successfully_aggregated_at: The successfully_aggregated_at of this Member.  # noqa: E501
        :type: str
        """

        self._successfully_aggregated_at = successfully_aggregated_at

    @property
    def user_guid(self):
        """Gets the user_guid of this Member.  # noqa: E501


        :return: The user_guid of this Member.  # noqa: E501
        :rtype: str
        """
        return self._user_guid

    @user_guid.setter
    def user_guid(self, user_guid):
        """Sets the user_guid of this Member.


        :param user_guid: The user_guid of this Member.  # noqa: E501
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
        if issubclass(Member, dict):
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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
