# atrium.IdentityApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**identify_member**](IdentityApi.md#identify_member) | **POST** /users/{user_guid}/members/{member_guid}/identify | Identify
[**list_account_owners**](IdentityApi.md#list_account_owners) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List member account owners


# **identify_member**
> MemberResponseBody identify_member(member_guid, user_guid)

Identify

The identify endpoint begins an identification process for an already-existing member.

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
    # Identify
    response = client.identity.identify_member(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling IdentityApi->identify_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_owners**
> AccountOwnersResponseBody list_account_owners(member_guid, user_guid)

List member account owners

This endpoint returns an array with information about every account associated with a particular member.

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
    # List member account owners
    response = client.identity.list_account_owners(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling IdentityApi->list_account_owners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**AccountOwnersResponseBody**](AccountOwnersResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

