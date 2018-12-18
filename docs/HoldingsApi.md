# atrium.HoldingsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_holdings**](HoldingsApi.md#list_holdings) | **GET** /users/{user_guid}/holdings | List holdings
[**list_holdings_by_account**](HoldingsApi.md#list_holdings_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/holdings | List holdings by account
[**list_holdings_by_member**](HoldingsApi.md#list_holdings_by_member) | **GET** /users/{user_guid}/members/{member_guid}/holdings | List holdings by member
[**read_holding**](HoldingsApi.md#read_holding) | **GET** /users/{user_guid}/holdings/{holding_guid} | Read holding


# **list_holdings**
> HoldingsResponseBody list_holdings(user_guid)

List holdings

Use this endpoint to read all holdings associated with a specific user.

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

try:
    # List holdings
    response = client.holdings.list_holdings(user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling HoldingsApi->list_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**HoldingsResponseBody**](HoldingsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_holdings_by_account**
> HoldingsResponseBody list_holdings_by_account(account_guid, user_guid)

List holdings by account

Use this endpoint to read all holdings associated with a specific account.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID")

account_guid = "ACT-123" # str | The unique identifier for an `account`.
user_guid = "USR-123" # str | The unique identifier for a `user`.

try:
    # List holdings by account
    response = client.holdings.list_holdings_by_account(account_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling HoldingsApi->list_holdings_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique identifier for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**HoldingsResponseBody**](HoldingsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_holdings_by_member**
> HoldingsResponseBody list_holdings_by_member(member_guid, user_guid)

List holdings by member

Use this endpoint to read all holdings associated with a specific member.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID")

member_guid = "MBR-123" # str | The unique identifier for a `member`.
user_guid = "USR-123" # str | The unique identifier for a `user`.

try:
    # List holdings by member
    response = client.holdings.list_holdings_by_member(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling HoldingsApi->list_holdings_by_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**HoldingsResponseBody**](HoldingsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_holding**
> HoldingResponseBody read_holding(holding_guid, user_guid)

Read holding

Use this endpoint to read the attributes of a specific holding.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID")

holding_guid = "HOL-123" # str | The unique identifier for a `holding`.
user_guid = "USR-123" # str | The unique identifier for a `user`.

try:
    # Read holding
    response = client.holdings.read_holding(holding_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling HoldingsApi->read_holding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holding_guid** | **str**| The unique identifier for a &#x60;holding&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**HoldingResponseBody**](HoldingResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

