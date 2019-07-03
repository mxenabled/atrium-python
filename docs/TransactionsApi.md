# atrium.TransactionsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**cleanse_and_categorize_transactions**](TransactionsApi.md#cleanse_and_categorize_transactions) | **POST** /transactions/cleanse_and_categorize | Categorize transactions
[**list_user_transactions**](TransactionsApi.md#list_user_transactions) | **GET** /users/{user_guid}/transactions | List transactions for a user
[**read_transaction**](TransactionsApi.md#read_transaction) | **GET** /users/{user_guid}/transactions/{transaction_guid} | Read a transaction


# **cleanse_and_categorize_transactions**
> TransactionsCleanseAndCategorizeResponseBody cleanse_and_categorize_transactions(body)

Categorize transactions

Use this endpoint to categorize, cleanse, and classify transactions. These transactions are not persisted or stored on the MX platform.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID")

body = atrium.TransactionsCleanseAndCategorizeRequestBody() # TransactionsCleanseAndCategorizeRequestBody | User object to be created with optional parameters (amount, type) amd required parameters (description, identifier)

try:
    # Categorize transactions
    response = client.transactions.cleanse_and_categorize_transactions(body)
    pprint(response)
except ApiException as e:
    print("Exception when calling TransactionsApi->cleanse_and_categorize_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionsCleanseAndCategorizeRequestBody**](TransactionsCleanseAndCategorizeRequestBody.md)| User object to be created with optional parameters (amount, type) amd required parameters (description, identifier) | 

### Return type

[**TransactionsCleanseAndCategorizeResponseBody**](TransactionsCleanseAndCategorizeResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_transactions**
> TransactionsResponseBody list_user_transactions(user_guid, page=page, from_date=from_date, records_per_page=records_per_page, to_date=to_date)

List transactions for a user

Use this endpoint to get all transactions that belong to a specific user, across all the user's members and accounts.<br> This endpoint accepts optional query parameters, from_date and to_date, which filter transactions according to the date they were posted. If no values are given, from_date will default to 90 days prior to the request, and to_date will default to 5 days from the time of the request. 

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID")

user_guid = "USR-123" # str | The unique identifier for a `user`.
page = 1 # int | Specify current page. (optional)
from_date = "2016-09-20" # str | Filter transactions from this date. (optional)
records_per_page = 12 # int | Specify records per page. (optional)
to_date = "2016-10-20" # str | Filter transactions to this date. (optional)

try:
    # List transactions for a user
    response = client.transactions.list_user_transactions(user_guid, page=page, from_date=from_date, records_per_page=records_per_page, to_date=to_date)
    pprint(response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_user_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 

### Return type

[**TransactionsResponseBody**](TransactionsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_transaction**
> TransactionResponseBody read_transaction(transaction_guid, user_guid)

Read a transaction

This endpoint allows you to view information about a specific transaction that belongs to a user.<br>

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID")

transaction_guid = "TRN-123" # str | The unique identifier for a `transaction`.
user_guid = "USR-123" # str | The unique identifier for a `user`.

try:
    # Read a transaction
    response = client.transactions.read_transaction(transaction_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling TransactionsApi->read_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_guid** | **str**| The unique identifier for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**TransactionResponseBody**](TransactionResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

