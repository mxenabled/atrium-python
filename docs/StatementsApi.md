# atrium.StatementsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_statements**](StatementsApi.md#fetch_statements) | **POST** /users/{user_guid}/members/{member_guid}/fetch_statements | Fetch statements
[**list_member_statements**](StatementsApi.md#list_member_statements) | **GET** /users/{user_guid}/members/{member_guid}/statements | List member statements


# **fetch_statements**
> MemberResponseBody fetch_statements(member_guid, user_guid)

Fetch statements

The fetch statements endpoint begins fetching statements for a member.

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
    # Fetch statements
    response = client.statements.fetch_statements(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling StatementsApi->fetch_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_statements**
> StatementsResponseBody list_member_statements(member_guid, user_guid, page=page, records_per_page=records_per_page)

List member statements

Certain institutions in Atrium allow developers to access account statements associated with a particular `member`. Use this endpoint to get an array of available statements.  Before this endpoint can be used, `fetch_statements` should be performed on the relevant `member`. 

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
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List member statements
    response = client.statements.list_member_statements(member_guid, user_guid, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling StatementsApi->list_member_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**StatementsResponseBody**](StatementsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

