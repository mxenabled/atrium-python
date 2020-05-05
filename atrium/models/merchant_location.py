# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class MerchantLocation(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'city': 'str',
        'guid': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'merchant_guid': 'str',
        'phone_number': 'str',
        'postal_code': 'str',
        'state': 'str',
        'store_number': 'str',
        'street_address': 'str'
    }

    attribute_map = {
        'city': 'city',
        'guid': 'guid',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'merchant_guid': 'merchant_guid',
        'phone_number': 'phone_number',
        'postal_code': 'postal_code',
        'state': 'state',
        'store_number': 'store_number',
        'street_address': 'street_address'
    }

    def __init__(self, city=None, guid=None, latitude=None, longitude=None, merchant_guid=None, phone_number=None, postal_code=None, state=None, store_number=None, street_address=None):  # noqa: E501

        self._city = None
        self._guid = None
        self._latitude = None
        self._longitude = None
        self._merchant_guid = None
        self._phone_number = None
        self._postal_code = None
        self._state = None
        self._store_number = None
        self._street_address = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if guid is not None:
            self.guid = guid
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if merchant_guid is not None:
            self.merchant_guid = merchant_guid
        if phone_number is not None:
            self.phone_number = phone_number
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if store_number is not None:
            self.store_number = store_number
        if street_address is not None:
            self.street_address = street_address

    @property
    def city(self):
        """Gets the city of this MerchantLocation.  # noqa: E501


        :return: The city of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this MerchantLocation.


        :param city: The city of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def guid(self):
        """Gets the guid of this MerchantLocation.  # noqa: E501


        :return: The guid of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this MerchantLocation.


        :param guid: The guid of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def latitude(self):
        """Gets the latitude of this MerchantLocation.  # noqa: E501


        :return: The latitude of this MerchantLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this MerchantLocation.


        :param latitude: The latitude of this MerchantLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this MerchantLocation.  # noqa: E501


        :return: The longitude of this MerchantLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this MerchantLocation.


        :param longitude: The longitude of this MerchantLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def merchant_guid(self):
        """Gets the merchant_guid of this MerchantLocation.  # noqa: E501


        :return: The merchant_guid of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._merchant_guid

    @merchant_guid.setter
    def merchant_guid(self, merchant_guid):
        """Sets the merchant_guid of this MerchantLocation.


        :param merchant_guid: The merchant_guid of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._merchant_guid = merchant_guid

    @property
    def phone_number(self):
        """Gets the phone_number of this MerchantLocation.  # noqa: E501


        :return: The phone_number of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this MerchantLocation.


        :param phone_number: The phone_number of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def postal_code(self):
        """Gets the postal_code of this MerchantLocation.  # noqa: E501


        :return: The postal_code of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this MerchantLocation.


        :param postal_code: The postal_code of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this MerchantLocation.  # noqa: E501


        :return: The state of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MerchantLocation.


        :param state: The state of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def store_number(self):
        """Gets the store_number of this MerchantLocation.  # noqa: E501


        :return: The store_number of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._store_number

    @store_number.setter
    def store_number(self, store_number):
        """Sets the store_number of this MerchantLocation.


        :param store_number: The store_number of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._store_number = store_number

    @property
    def street_address(self):
        """Gets the street_address of this MerchantLocation.  # noqa: E501


        :return: The street_address of this MerchantLocation.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this MerchantLocation.


        :param street_address: The street_address of this MerchantLocation.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

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
        if issubclass(MerchantLocation, dict):
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
        if not isinstance(other, MerchantLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
