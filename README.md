# atrium
The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access. 

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install atrium
```

Then import the package:
```python
import atrium
```

## Example Usage

Please see `docs` directory for additional endpoint examples

```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

account_guid = "ACT-123" # str | The unique identifier for an `account`.
user_guid = "USR-123" # str | The unique identifier for a `user`.
from_date = "2016-09-20" # str | Filter transactions from this date. (optional)
to_date = "2016-10-20" # str | Filter transactions to this date. (optional)
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List account transactions
    response = client.accounts.list_account_transactions(account_guid, user_guid, from_date=from_date, to_date=to_date, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_account_transactions: %s\n" % e)

```

## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**list_account_transactions**](docs/AccountsApi.md#list_account_transactions) | **GET** /users/{user_guid}/accounts/{account_guid}/transactions | List account transactions
*AccountsApi* | [**list_user_accounts**](docs/AccountsApi.md#list_user_accounts) | **GET** /users/{user_guid}/accounts | List accounts for a user
*AccountsApi* | [**read_account**](docs/AccountsApi.md#read_account) | **GET** /users/{user_guid}/accounts/{account_guid} | Read an account
*AccountsApi* | [**read_account_by_member_guid**](docs/AccountsApi.md#read_account_by_member_guid) | **GET** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Read an account
*ConnectWidgetApi* | [**get_connect_widget**](docs/ConnectWidgetApi.md#get_connect_widget) | **POST** /users/{user_guid}/connect_widget_url | Embedding in a website
*HoldingsApi* | [**list_holdings**](docs/HoldingsApi.md#list_holdings) | **GET** /users/{user_guid}/holdings | List holdings
*HoldingsApi* | [**list_holdings_by_account**](docs/HoldingsApi.md#list_holdings_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/holdings | List holdings by account
*HoldingsApi* | [**list_holdings_by_member**](docs/HoldingsApi.md#list_holdings_by_member) | **GET** /users/{user_guid}/members/{member_guid}/holdings | List holdings by member
*HoldingsApi* | [**read_holding**](docs/HoldingsApi.md#read_holding) | **GET** /users/{user_guid}/holdings/{holding_guid} | Read holding
*IdentityApi* | [**identify_member**](docs/IdentityApi.md#identify_member) | **POST** /users/{user_guid}/members/{member_guid}/identify | Identify
*IdentityApi* | [**list_account_owners**](docs/IdentityApi.md#list_account_owners) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List member account owners
*InstitutionsApi* | [**list_institutions**](docs/InstitutionsApi.md#list_institutions) | **GET** /institutions | List institutions
*InstitutionsApi* | [**read_institution**](docs/InstitutionsApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution
*InstitutionsApi* | [**read_institution_credentials**](docs/InstitutionsApi.md#read_institution_credentials) | **GET** /institutions/{institution_code}/credentials | Read institution credentials
*MembersApi* | [**aggregate_member**](docs/MembersApi.md#aggregate_member) | **POST** /users/{user_guid}/members/{member_guid}/aggregate | Aggregate member
*MembersApi* | [**aggregate_member_balances**](docs/MembersApi.md#aggregate_member_balances) | **POST** /users/{user_guid}/members/{member_guid}/balance | Aggregate member account balances
*MembersApi* | [**create_member**](docs/MembersApi.md#create_member) | **POST** /users/{user_guid}/members | Create member
*MembersApi* | [**delete_member**](docs/MembersApi.md#delete_member) | **DELETE** /users/{user_guid}/members/{member_guid} | Delete member
*MembersApi* | [**extend_history**](docs/MembersApi.md#extend_history) | **POST** /users/{user_guid}/members/{member_guid}/extend_history | Extend history
*MembersApi* | [**list_member_accounts**](docs/MembersApi.md#list_member_accounts) | **GET** /users/{user_guid}/members/{member_guid}/accounts | List member accounts
*MembersApi* | [**list_member_credentials**](docs/MembersApi.md#list_member_credentials) | **GET** /users/{user_guid}/members/{member_guid}/credentials | List member credentials
*MembersApi* | [**list_member_mfa_challenges**](docs/MembersApi.md#list_member_mfa_challenges) | **GET** /users/{user_guid}/members/{member_guid}/challenges | List member MFA challenges
*MembersApi* | [**list_member_transactions**](docs/MembersApi.md#list_member_transactions) | **GET** /users/{user_guid}/members/{member_guid}/transactions | List member transactions
*MembersApi* | [**list_members**](docs/MembersApi.md#list_members) | **GET** /users/{user_guid}/members | List members
*MembersApi* | [**read_member**](docs/MembersApi.md#read_member) | **GET** /users/{user_guid}/members/{member_guid} | Read member
*MembersApi* | [**read_member_status**](docs/MembersApi.md#read_member_status) | **GET** /users/{user_guid}/members/{member_guid}/status | Read member connection status
*MembersApi* | [**read_o_auth_window_uri**](docs/MembersApi.md#read_o_auth_window_uri) | **GET** /users/{user_guid}/members/{member_guid}/oauth_window_uri | Read OAuth Window URI
*MembersApi* | [**resume_member**](docs/MembersApi.md#resume_member) | **PUT** /users/{user_guid}/members/{member_guid}/resume | Resume aggregation from MFA
*MembersApi* | [**update_member**](docs/MembersApi.md#update_member) | **PUT** /users/{user_guid}/members/{member_guid} | Update member
*MerchantsApi* | [**list_merchant_locations**](docs/MerchantsApi.md#list_merchant_locations) | **GET** /merchants/{merchant_guid}/merchant_locations | List merchant locations
*MerchantsApi* | [**list_merchants**](docs/MerchantsApi.md#list_merchants) | **GET** /merchants | List merchants
*MerchantsApi* | [**read_merchant**](docs/MerchantsApi.md#read_merchant) | **GET** /merchants/{merchant_guid} | Read merchant
*MerchantsApi* | [**read_merchant_location**](docs/MerchantsApi.md#read_merchant_location) | **GET** /merchants/{merchant_guid}/merchant_locations/{merchant_location_guid} | Read merchant location
*StatementsApi* | [**download_statement_pdf**](docs/StatementsApi.md#download_statement_pdf) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid}.pdf | Download statement PDF
*StatementsApi* | [**fetch_statements**](docs/StatementsApi.md#fetch_statements) | **POST** /users/{user_guid}/members/{member_guid}/fetch_statements | Fetch statements
*StatementsApi* | [**list_member_statements**](docs/StatementsApi.md#list_member_statements) | **GET** /users/{user_guid}/members/{member_guid}/statements | List member statements
*StatementsApi* | [**read_member_statement**](docs/StatementsApi.md#read_member_statement) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid} | Read statement JSON
*TransactionsApi* | [**cleanse_and_categorize_transactions**](docs/TransactionsApi.md#cleanse_and_categorize_transactions) | **POST** /transactions/cleanse_and_categorize | Categorize transactions
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
 - [AccountNumber](docs/AccountNumber.md)
 - [AccountNumbersResponseBody](docs/AccountNumbersResponseBody.md)
 - [AccountOwner](docs/AccountOwner.md)
 - [AccountOwnersResponseBody](docs/AccountOwnersResponseBody.md)
 - [AccountResponseBody](docs/AccountResponseBody.md)
 - [AccountsResponseBody](docs/AccountsResponseBody.md)
 - [Challenge](docs/Challenge.md)
 - [ChallengeImageOption](docs/ChallengeImageOption.md)
 - [ChallengeOption](docs/ChallengeOption.md)
 - [ChallengesResponseBody](docs/ChallengesResponseBody.md)
 - [ConnectWidget](docs/ConnectWidget.md)
 - [ConnectWidgetRequestBody](docs/ConnectWidgetRequestBody.md)
 - [ConnectWidgetResponseBody](docs/ConnectWidgetResponseBody.md)
 - [CredentialOption](docs/CredentialOption.md)
 - [CredentialRequest](docs/CredentialRequest.md)
 - [CredentialResponse](docs/CredentialResponse.md)
 - [CredentialsResponseBody](docs/CredentialsResponseBody.md)
 - [Holding](docs/Holding.md)
 - [HoldingResponseBody](docs/HoldingResponseBody.md)
 - [HoldingsResponseBody](docs/HoldingsResponseBody.md)
 - [Institution](docs/Institution.md)
 - [InstitutionResponseBody](docs/InstitutionResponseBody.md)
 - [InstitutionsResponseBody](docs/InstitutionsResponseBody.md)
 - [Member](docs/Member.md)
 - [MemberConnectionStatus](docs/MemberConnectionStatus.md)
 - [MemberConnectionStatusResponseBody](docs/MemberConnectionStatusResponseBody.md)
 - [MemberCreateRequest](docs/MemberCreateRequest.md)
 - [MemberCreateRequestBody](docs/MemberCreateRequestBody.md)
 - [MemberResponseBody](docs/MemberResponseBody.md)
 - [MemberResumeRequest](docs/MemberResumeRequest.md)
 - [MemberResumeRequestBody](docs/MemberResumeRequestBody.md)
 - [MemberUpdateRequest](docs/MemberUpdateRequest.md)
 - [MemberUpdateRequestBody](docs/MemberUpdateRequestBody.md)
 - [MembersResponseBody](docs/MembersResponseBody.md)
 - [Merchant](docs/Merchant.md)
 - [MerchantLocation](docs/MerchantLocation.md)
 - [MerchantLocationResponseBody](docs/MerchantLocationResponseBody.md)
 - [MerchantLocationsResponseBody](docs/MerchantLocationsResponseBody.md)
 - [MerchantResponseBody](docs/MerchantResponseBody.md)
 - [MerchantsResponseBody](docs/MerchantsResponseBody.md)
 - [Pagination](docs/Pagination.md)
 - [Statement](docs/Statement.md)
 - [StatementResponseBody](docs/StatementResponseBody.md)
 - [StatementsResponseBody](docs/StatementsResponseBody.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionCleanseAndCategorizeRequest](docs/TransactionCleanseAndCategorizeRequest.md)
 - [TransactionCleanseAndCategorizeResponse](docs/TransactionCleanseAndCategorizeResponse.md)
 - [TransactionResponseBody](docs/TransactionResponseBody.md)
 - [TransactionsCleanseAndCategorizeRequestBody](docs/TransactionsCleanseAndCategorizeRequestBody.md)
 - [TransactionsCleanseAndCategorizeResponseBody](docs/TransactionsCleanseAndCategorizeResponseBody.md)
 - [TransactionsResponseBody](docs/TransactionsResponseBody.md)
 - [User](docs/User.md)
 - [UserCreateRequestBody](docs/UserCreateRequestBody.md)
 - [UserResponseBody](docs/UserResponseBody.md)
 - [UserUpdateRequestBody](docs/UserUpdateRequestBody.md)
 - [UsersResponseBody](docs/UsersResponseBody.md)

