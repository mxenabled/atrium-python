# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


from __future__ import absolute_import

import unittest

import atrium
from atrium.api.holdings import HoldingsApi  # noqa: E501
from atrium.rest import ApiException


class TestHoldingsApi(unittest.TestCase):
    """HoldingsApi unit test stubs"""

    def setUp(self):
        self.api = atrium.api.holdings.HoldingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_holdings(self):
        """Test case for list_holdings

        List holdings  # noqa: E501
        """
        pass

    def test_list_holdings_by_account(self):
        """Test case for list_holdings_by_account

        List holdings by account  # noqa: E501
        """
        pass

    def test_list_holdings_by_member(self):
        """Test case for list_holdings_by_member

        List holdings by member  # noqa: E501
        """
        pass

    def test_read_holding(self):
        """Test case for read_holding

        Read holding  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
