# atrium-python.VerificationApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_account_numbers**](VerificationApi.md#list_account_numbers) | **GET** /users/{user_guid}/members/{member_guid}/account_numbers | Read account numbers
[**list_account_numbers_by_account**](VerificationApi.md#list_account_numbers_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/account_numbers | Read account numbers by account GUID
[**verify_member**](VerificationApi.md#verify_member) | **POST** /users/{user_guid}/members/{member_guid}/verify | Verify


# **list_account_numbers**
> AccountNumbers list_account_numbers(member_guid, user_guid)

Read account numbers

Use this endpoint to check whether account and routing numbers are available for accounts associated with a particular member. It returns the account_numbers object, which contains account and routing number data for each account associated with the member.

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
api_instance = atrium-python.VerificationApi(atrium-python.ApiClient(configuration))
member_guid = 'member_guid_example' # str | The unique identifier for a `member`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Read account numbers
    api_response = api_instance.list_account_numbers(member_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->list_account_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**AccountNumbers**](AccountNumbers.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_numbers_by_account**
> AccountNumbers list_account_numbers_by_account(account_guid, user_guid)

Read account numbers by account GUID

Use this endpoint to check whether account and routing numbers are available for a specific account. It returns the account_numbers object, which contains account and routing number data.

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
api_instance = atrium-python.VerificationApi(atrium-python.ApiClient(configuration))
account_guid = 'account_guid_example' # str | The unique identifier for an `account`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Read account numbers by account GUID
    api_response = api_instance.list_account_numbers_by_account(account_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->list_account_numbers_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique identifier for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**AccountNumbers**](AccountNumbers.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_member**
> Member verify_member(member_guid, user_guid)

Verify

The verify endpoint begins a verification process for a member.

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
api_instance = atrium-python.VerificationApi(atrium-python.ApiClient(configuration))
member_guid = 'member_guid_example' # str | The unique identifier for a `member`.
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Verify
    api_response = api_instance.verify_member(member_guid, user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->verify_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**Member**](Member.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

