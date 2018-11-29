# atrium-python.AccountsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_account_transactions**](AccountsApi.md#list_account_transactions) | **GET** /users/{user_guid}/accounts/{account_guid}/transactions | List account transactions
[**list_user_accounts**](AccountsApi.md#list_user_accounts) | **GET** /users/{user_guid}/accounts | List accounts for a user
[**read_account**](AccountsApi.md#read_account) | **GET** /users/{user_guid}/accounts/{account_guid} | Read an account
[**read_account_by_member_guid**](AccountsApi.md#read_account_by_member_guid) | **GET** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Read an account


# **list_account_transactions**
> Transactions list_account_transactions(account_guid, user_guid, from_date=from_date, to_date=to_date, page=page, records_per_page=records_per_page)

List account transactions

This endpoint allows you to see every transaction that belongs to a specific account. The default from_date is 90 days prior to the request, and the default to_date is 5 days from the time of the request.<br> The from_date and to_date parameters can optionally be appended to the request. 

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique identifier for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**Transactions**](Transactions.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_accounts**
> Accounts list_user_accounts(user_guid, page=page, records_per_page=records_per_page)

List accounts for a user

Use this endpoint to view information about every account that belongs to a user. You'll need the user's GUID to access this list. The information will include the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the account balance, the date the account was started, etc.

### Example
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
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.
page = 12 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List accounts for a user
    api_response = api_instance.list_user_accounts(user_guid, page=page, records_per_page=records_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_user_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**Accounts**](Accounts.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_account**
> Account read_account(account_guid, user_guid)

Read an account

Reading an account allows you to get information about a specific account that belongs to a user. That includes the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the balance, the date the account was started, and much more.<br> There are two endpoints for reading an account. Both will return the same information.<br> It's important to remember that balance and available_balance will normally be positive numbers — for all account types. But this should be interpreted differently for debt accounts and asset accounts.<br> An asset account, e.g., CHECKING, SAVINGS, or INVESTMENT, will have a positive balance unless it is in an overdraft condition, in which case the balance will be negative.<br> On the other hand, a debt account, e.g., CREDIT CARD, LOAN, MORTGAGE, would have a positivebalance when the user owes money on the account. It would have a negative balance if the account has been overpaid. 

### Example
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

try:
    # Read an account
    api_response = api_instance.read_account(account_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->read_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique identifier for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**Account**](Account.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_account_by_member_guid**
> Account read_account_by_member_guid(account_guid, member_guid, user_guid)

Read an account

Reading an account allows you to get information about a specific account that belongs to a user. That includes the account type — e.g., CHECKING, MONEY_MARKET, or PROPERTY — the balance, the date the account was started, and much more.<br> There are two endpoints for reading an account. Both will return the same information.<br> It's important to remember that balance and available_balance will normally be positive numbers — for all account types. But this should be interpreted differently for debt accounts and asset accounts.<br> An asset account, e.g., CHECKING, SAVINGS, or INVESTMENT, will have a positive balance unless it is in an overdraft condition, in which case the balance will be negative.<br> On the other hand, a debt account, e.g., CREDIT CARD, LOAN, MORTGAGE, would have a positivebalance when the user owes money on the account. It would have a negative balance if the account has been overpaid. 

### Example
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
member_guid = 'member_guid_example' # str | The unique identifier for a `member`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Read an account
    api_response = api_instance.read_account_by_member_guid(account_guid, member_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->read_account_by_member_guid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique identifier for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**Account**](Account.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

