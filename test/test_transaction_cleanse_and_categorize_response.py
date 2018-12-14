# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


from __future__ import absolute_import

import unittest

import atrium
from atrium.models.transaction_cleanse_and_categorize_response import TransactionCleanseAndCategorizeResponse  # noqa: E501
from atrium.rest import ApiException


class TestTransactionCleanseAndCategorizeResponse(unittest.TestCase):
    """TransactionCleanseAndCategorizeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionCleanseAndCategorizeResponse(self):
        """Test TransactionCleanseAndCategorizeResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = atrium.models.transaction_cleanse_and_categorize_response.TransactionCleanseAndCategorizeResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
