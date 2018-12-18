# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from atrium.models.credential_request import CredentialRequest  # noqa: F401,E501


class MemberUpdateRequest(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'credentials': 'list[CredentialRequest]',
        'identifier': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'credentials': 'credentials',
        'identifier': 'identifier',
        'metadata': 'metadata'
    }

    def __init__(self, credentials=None, identifier=None, metadata=None):  # noqa: E501

        self._credentials = None
        self._identifier = None
        self._metadata = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials
        if identifier is not None:
            self.identifier = identifier
        if metadata is not None:
            self.metadata = metadata

    @property
    def credentials(self):
        """Gets the credentials of this MemberUpdateRequest.  # noqa: E501


        :return: The credentials of this MemberUpdateRequest.  # noqa: E501
        :rtype: list[CredentialRequest]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this MemberUpdateRequest.


        :param credentials: The credentials of this MemberUpdateRequest.  # noqa: E501
        :type: list[CredentialRequest]
        """

        self._credentials = credentials

    @property
    def identifier(self):
        """Gets the identifier of this MemberUpdateRequest.  # noqa: E501


        :return: The identifier of this MemberUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this MemberUpdateRequest.


        :param identifier: The identifier of this MemberUpdateRequest.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def metadata(self):
        """Gets the metadata of this MemberUpdateRequest.  # noqa: E501


        :return: The metadata of this MemberUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MemberUpdateRequest.


        :param metadata: The metadata of this MemberUpdateRequest.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

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
        if issubclass(MemberUpdateRequest, dict):
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
        if not isinstance(other, MemberUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
