# atrium-python
The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access. 

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/mxenabled/atrium-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mxenabled/atrium-python.git`)

Then import the package:
```python
import atrium-python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import atrium-python
```

## Example Usage

Please see `docs` directory for additional endpoint examples

```python
from __future__ import print_function
import time
import atrium-python
from atrium-python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = atrium-python.Configuration()
configuration.api_key['MX-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MX-API-Key'] = 'Bearer'
# Configure API key authorization: clientID
configuration = atrium-python.Configuration()
configuration.api_key['MX-Client-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MX-Client-ID'] = 'Bearer'

# create an instance of the API class
api_instance = atrium-python.AccountsApi(atrium-python.ApiClient(configuration))
account_guid = 'account_guid_example' # str | The unique identifier for an `account`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.
from_date = 'from_date_example' # str | Filter transactions from this date. (optional)
to_date = 'to_date_example' # str | Filter transactions to this date. (optional)
page = 12 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List account transactions
    api_response = api_instance.list_account_transactions(account_guid, user_guid, from_date=from_date, to_date=to_date, page=page, records_per_page=records_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_account_transactions: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://vestibule.mx.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**list_account_transactions**](docs/AccountsApi.md#list_account_transactions) | **GET** /users/{user_guid}/accounts/{account_guid}/transactions | List account transactions
*AccountsApi* | [**list_user_accounts**](docs/AccountsApi.md#list_user_accounts) | **GET** /users/{user_guid}/accounts | List accounts for a user
*AccountsApi* | [**read_account**](docs/AccountsApi.md#read_account) | **GET** /users/{user_guid}/accounts/{account_guid} | Read an account
*AccountsApi* | [**read_account_by_member_guid**](docs/AccountsApi.md#read_account_by_member_guid) | **GET** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Read an account
*ConnectWidgetApi* | [**get_connect_widget**](docs/ConnectWidgetApi.md#get_connect_widget) | **POST** /users/{user_guid}/connect_widget_url | Embedding in a website
*IdentityApi* | [**identify_member**](docs/IdentityApi.md#identify_member) | **POST** /users/{user_guid}/members/{member_guid}/identify | Identify
*IdentityApi* | [**list_account_owners**](docs/IdentityApi.md#list_account_owners) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List member account owners
*InstitutionsApi* | [**list_institutions**](docs/InstitutionsApi.md#list_institutions) | **GET** /institutions | List institutions
*InstitutionsApi* | [**read_institution**](docs/InstitutionsApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution
*InstitutionsApi* | [**read_institution_credentials**](docs/InstitutionsApi.md#read_institution_credentials) | **GET** /institutions/{institution_code}/credentials | Read institution credentials
*MembersApi* | [**aggregate_member**](docs/MembersApi.md#aggregate_member) | **POST** /users/{user_guid}/members/{member_guid}/aggregate | Aggregate member
*MembersApi* | [**create_member**](docs/MembersApi.md#create_member) | **POST** /users/{user_guid}/members | Create member
*MembersApi* | [**delete_member**](docs/MembersApi.md#delete_member) | **DELETE** /users/{user_guid}/members/{member_guid} | Delete member
*MembersApi* | [**list_member_accounts**](docs/MembersApi.md#list_member_accounts) | **GET** /users/{user_guid}/members/{member_guid}/accounts | List member accounts
*MembersApi* | [**list_member_credentials**](docs/MembersApi.md#list_member_credentials) | **GET** /users/{user_guid}/members/{member_guid}/credentials | List member credentials
*MembersApi* | [**list_member_mfa_challenges**](docs/MembersApi.md#list_member_mfa_challenges) | **GET** /users/{user_guid}/members/{member_guid}/challenges | List member MFA challenges
*MembersApi* | [**list_member_transactions**](docs/MembersApi.md#list_member_transactions) | **GET** /users/{user_guid}/members/{member_guid}/transactions | List member transactions
*MembersApi* | [**list_members**](docs/MembersApi.md#list_members) | **GET** /users/{user_guid}/members | List members
*MembersApi* | [**read_member**](docs/MembersApi.md#read_member) | **GET** /users/{user_guid}/members/{member_guid} | Read member
*MembersApi* | [**read_member_status**](docs/MembersApi.md#read_member_status) | **GET** /users/{user_guid}/members/{member_guid}/status | Read member connection status
*MembersApi* | [**resume_member**](docs/MembersApi.md#resume_member) | **PUT** /users/{user_guid}/members/{member_guid}/resume | Resume aggregation from MFA
*MembersApi* | [**update_member**](docs/MembersApi.md#update_member) | **PUT** /users/{user_guid}/members/{member_guid} | Update member
*TransactionsApi* | [**cleanse_and_categorize_transactions**](docs/TransactionsApi.md#cleanse_and_categorize_transactions) | **POST** /cleanse_and_categorize | Categorize transactions
*TransactionsApi* | [**list_user_transactions**](docs/TransactionsApi.md#list_user_transactions) | **GET** /users/{user_guid}/transactions | List transactions for a user
*TransactionsApi* | [**read_transaction**](docs/TransactionsApi.md#read_transaction) | **GET** /users/{user_guid}/transactions/{transaction_guid} | Read a transaction
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /users | Create user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /users/{user_guid} | Delete user
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /users | List users
*UsersApi* | [**read_user**](docs/UsersApi.md#read_user) | **GET** /users/{user_guid} | Read user
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /users/{user_guid} | Update user
*VerificationApi* | [**list_account_numbers**](docs/VerificationApi.md#list_account_numbers) | **GET** /users/{user_guid}/members/{member_guid}/account_numbers | Read account numbers
*VerificationApi* | [**list_account_numbers_by_account**](docs/VerificationApi.md#list_account_numbers_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/account_numbers | Read account numbers by account GUID
*VerificationApi* | [**verify_member**](docs/VerificationApi.md#verify_member) | **POST** /users/{user_guid}/members/{member_guid}/verify | Verify


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountAttributes](docs/AccountAttributes.md)
 - [AccountNumberAttributes](docs/AccountNumberAttributes.md)
 - [AccountNumbers](docs/AccountNumbers.md)
 - [AccountOwnerAttributes](docs/AccountOwnerAttributes.md)
 - [AccountOwners](docs/AccountOwners.md)
 - [Accounts](docs/Accounts.md)
 - [ChallengeAttributes](docs/ChallengeAttributes.md)
 - [ChallengeOptionAttributes](docs/ChallengeOptionAttributes.md)
 - [Challenges](docs/Challenges.md)
 - [ConnectWidget](docs/ConnectWidget.md)
 - [ConnectWidgetAttributes](docs/ConnectWidgetAttributes.md)
 - [ConnectWidgetRequestBody](docs/ConnectWidgetRequestBody.md)
 - [CredentialAttributes](docs/CredentialAttributes.md)
 - [CredentialOptionAttributes](docs/CredentialOptionAttributes.md)
 - [CredentialResponseAttributes](docs/CredentialResponseAttributes.md)
 - [Credentials](docs/Credentials.md)
 - [Institution](docs/Institution.md)
 - [InstitutionAttributes](docs/InstitutionAttributes.md)
 - [Institutions](docs/Institutions.md)
 - [Member](docs/Member.md)
 - [MemberAttributes](docs/MemberAttributes.md)
 - [MemberConnectionStatus](docs/MemberConnectionStatus.md)
 - [MemberConnectionStatusAttributes](docs/MemberConnectionStatusAttributes.md)
 - [MemberCreateRequestBody](docs/MemberCreateRequestBody.md)
 - [MemberCreateRequestBodyAttributes](docs/MemberCreateRequestBodyAttributes.md)
 - [MemberResumeRequestBody](docs/MemberResumeRequestBody.md)
 - [MemberResumeRequestBodyAttributes](docs/MemberResumeRequestBodyAttributes.md)
 - [MemberUpdateRequestBody](docs/MemberUpdateRequestBody.md)
 - [MemberUpdateRequestBodyAttributes](docs/MemberUpdateRequestBodyAttributes.md)
 - [Members](docs/Members.md)
 - [Pagination](docs/Pagination.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionAttributes](docs/TransactionAttributes.md)
 - [Transactions](docs/Transactions.md)
 - [TransactionsCleanseAndCategorize](docs/TransactionsCleanseAndCategorize.md)
 - [TransactionsCleanseAndCategorizeAttributes](docs/TransactionsCleanseAndCategorizeAttributes.md)
 - [TransactionsCleanseAndCategorizeRequestBody](docs/TransactionsCleanseAndCategorizeRequestBody.md)
 - [TransactionsCleanseAndCategorizeRequestBodyAttributes](docs/TransactionsCleanseAndCategorizeRequestBodyAttributes.md)
 - [User](docs/User.md)
 - [UserAttributes](docs/UserAttributes.md)
 - [UserCreateRequestBody](docs/UserCreateRequestBody.md)
 - [UserUpdateRequestBody](docs/UserUpdateRequestBody.md)
 - [Users](docs/Users.md)

