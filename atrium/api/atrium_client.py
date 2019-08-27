from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

import atrium

class AtriumClient(object):
    def __init__(self, api_key, client_id, environment = "https://vestibule.mx.com"):
        configuration = atrium.Configuration()
        configuration.headers['MX-API-Key'] = api_key
        configuration.headers['MX-Client-ID'] = client_id
        configuration.host = environment
        
        self.accounts = atrium.AccountsApi(atrium.ApiClient(configuration))
        self.connect_widget = atrium.ConnectWidgetApi(atrium.ApiClient(configuration))
        self.holdings = atrium.HoldingsApi(atrium.ApiClient(configuration))
        self.identity = atrium.IdentityApi(atrium.ApiClient(configuration))
        self.institutions = atrium.InstitutionsApi(atrium.ApiClient(configuration))
        self.members = atrium.MembersApi(atrium.ApiClient(configuration))
        self.merchants = atrium.MerchantsApi(atrium.ApiClient(configuration))
        self.statements = atrium.StatementsApi(atrium.ApiClient(configuration))
        self.transactions = atrium.TransactionsApi(atrium.ApiClient(configuration))
        self.users = atrium.UsersApi(atrium.ApiClient(configuration))
        self.verification = atrium.VerificationApi(atrium.ApiClient(configuration))
