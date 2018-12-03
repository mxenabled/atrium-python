# atrium.IdentityApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**identify_member**](IdentityApi.md#identify_member) | **POST** /users/{user_guid}/members/{member_guid}/identify | Identify
[**list_account_owners**](IdentityApi.md#list_account_owners) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List member account owners


# **identify_member**
> Member identify_member(member_guid, user_guid)

Identify

The identify endpoint begins an identification process for an already-existing member.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = atrium.Configuration()
configuration.api_key['MX-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MX-API-Key'] = 'Bearer'
# Configure API key authorization: clientID
configuration = atrium.Configuration()
configuration.api_key['MX-Client-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MX-Client-ID'] = 'Bearer'

# create an instance of the API class
api_instance = atrium.IdentityApi(atrium.ApiClient(configuration))
member_guid = 'member_guid_example' # str | The unique identifier for a `member`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Identify
    api_response = api_instance.identify_member(member_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->identify_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**Member**](Member.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_owners**
> AccountOwners list_account_owners(member_guid, user_guid)

List member account owners

This endpoint returns an array with information about every account associated with a particular member.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = atrium.Configuration()
configuration.api_key['MX-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MX-API-Key'] = 'Bearer'
# Configure API key authorization: clientID
configuration = atrium.Configuration()
configuration.api_key['MX-Client-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MX-Client-ID'] = 'Bearer'

# create an instance of the API class
api_instance = atrium.IdentityApi(atrium.ApiClient(configuration))
member_guid = 'member_guid_example' # str | The unique identifier for a `member`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # List member account owners
    api_response = api_instance.list_account_owners(member_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->list_account_owners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**AccountOwners**](AccountOwners.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

