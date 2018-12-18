# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from atrium.models.credential_option import CredentialOption  # noqa: F401,E501


class CredentialResponse(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'field_name': 'str',
        'guid': 'str',
        'label': 'str',
        'options': 'list[CredentialOption]',
        'type': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'guid': 'guid',
        'label': 'label',
        'options': 'options',
        'type': 'type'
    }

    def __init__(self, field_name=None, guid=None, label=None, options=None, type=None):  # noqa: E501

        self._field_name = None
        self._guid = None
        self._label = None
        self._options = None
        self._type = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if guid is not None:
            self.guid = guid
        if label is not None:
            self.label = label
        if options is not None:
            self.options = options
        if type is not None:
            self.type = type

    @property
    def field_name(self):
        """Gets the field_name of this CredentialResponse.  # noqa: E501


        :return: The field_name of this CredentialResponse.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this CredentialResponse.


        :param field_name: The field_name of this CredentialResponse.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def guid(self):
        """Gets the guid of this CredentialResponse.  # noqa: E501


        :return: The guid of this CredentialResponse.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this CredentialResponse.


        :param guid: The guid of this CredentialResponse.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def label(self):
        """Gets the label of this CredentialResponse.  # noqa: E501


        :return: The label of this CredentialResponse.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CredentialResponse.


        :param label: The label of this CredentialResponse.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def options(self):
        """Gets the options of this CredentialResponse.  # noqa: E501


        :return: The options of this CredentialResponse.  # noqa: E501
        :rtype: list[CredentialOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CredentialResponse.


        :param options: The options of this CredentialResponse.  # noqa: E501
        :type: list[CredentialOption]
        """

        self._options = options

    @property
    def type(self):
        """Gets the type of this CredentialResponse.  # noqa: E501


        :return: The type of this CredentialResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredentialResponse.


        :param type: The type of this CredentialResponse.  # noqa: E501
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
        if issubclass(CredentialResponse, dict):
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
        if not isinstance(other, CredentialResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
