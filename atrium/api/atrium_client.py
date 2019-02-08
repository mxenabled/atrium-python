from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

import atrium

class AtriumClient(object):
    def __init__(self, api_key, client_id):
        configuration = atrium.Configuration()
        configuration.headers['MX-API-Key'] = api_key
        configuration.headers['MX-Client-ID'] = client_id
        
        self.accounts = atrium.AccountsApi()
        self.connect_widget = atrium.ConnectWidgetApi()
        self.holdings = atrium.HoldingsApi()
        self.identity = atrium.IdentityApi()
        self.institutions = atrium.InstitutionsApi()
        self.members = atrium.MembersApi()
        self.merchants = atrium.MerchantsApi()
        self.statements = atrium.StatementsApi()
        self.transactions = atrium.TransactionsApi()
        self.users = atrium.UsersApi()
        self.verification = atrium.VerificationApi()
