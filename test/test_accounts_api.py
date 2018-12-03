# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


from __future__ import absolute_import

import unittest

import atrium-python
from atrium-python.api.accounts_api import AccountsApi  # noqa: E501
from atrium-python.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = atrium-python.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_account_transactions(self):
        """Test case for list_account_transactions

        List account transactions  # noqa: E501
        """
        pass

    def test_list_user_accounts(self):
        """Test case for list_user_accounts

        List accounts for a user  # noqa: E501
        """
        pass

    def test_read_account(self):
        """Test case for read_account

        Read an account  # noqa: E501
        """
        pass

    def test_read_account_by_member_guid(self):
        """Test case for read_account_by_member_guid

        Read an account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()