# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class Merchant(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'created_at': 'str',
        'guid': 'str',
        'logo_url': 'str',
        'name': 'str',
        'updated_at': 'str',
        'website_url': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'guid': 'guid',
        'logo_url': 'logo_url',
        'name': 'name',
        'updated_at': 'updated_at',
        'website_url': 'website_url'
    }

    def __init__(self, created_at=None, guid=None, logo_url=None, name=None, updated_at=None, website_url=None):  # noqa: E501

        self._created_at = None
        self._guid = None
        self._logo_url = None
        self._name = None
        self._updated_at = None
        self._website_url = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if guid is not None:
            self.guid = guid
        if logo_url is not None:
            self.logo_url = logo_url
        if name is not None:
            self.name = name
        if updated_at is not None:
            self.updated_at = updated_at
        if website_url is not None:
            self.website_url = website_url

    @property
    def created_at(self):
        """Gets the created_at of this Merchant.  # noqa: E501


        :return: The created_at of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Merchant.


        :param created_at: The created_at of this Merchant.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def guid(self):
        """Gets the guid of this Merchant.  # noqa: E501


        :return: The guid of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Merchant.


        :param guid: The guid of this Merchant.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def logo_url(self):
        """Gets the logo_url of this Merchant.  # noqa: E501


        :return: The logo_url of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Merchant.


        :param logo_url: The logo_url of this Merchant.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """Gets the name of this Merchant.  # noqa: E501


        :return: The name of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Merchant.


        :param name: The name of this Merchant.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this Merchant.  # noqa: E501


        :return: The updated_at of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Merchant.


        :param updated_at: The updated_at of this Merchant.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def website_url(self):
        """Gets the website_url of this Merchant.  # noqa: E501


        :return: The website_url of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this Merchant.


        :param website_url: The website_url of this Merchant.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

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
        if issubclass(Merchant, dict):
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
        if not isinstance(other, Merchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
