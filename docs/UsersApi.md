# atrium-python.UsersApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_guid} | Delete user
[**list_users**](UsersApi.md#list_users) | **GET** /users | List users
[**read_user**](UsersApi.md#read_user) | **GET** /users/{user_guid} | Read user
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_guid} | Update user


# **create_user**
> User create_user(body)

Create user

Call this endpoint to create a new user. Atrium will respond with the newly-created user object if successful. This endpoint accepts several parameters: identifier, metadata, and is_disabled.<br> Disabling a user means that accounts and transactions associated with it will not be updated in the background by MX. It will also restrict access to that user's data until they are no longer disabled. Users who are disabled for the entirety of an Atrium billing period will not be factored into that month's bill. 

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
api_instance = atrium-python.UsersApi(atrium-python.ApiClient(configuration))
body = atrium-python.UserCreateRequestBody() # UserCreateRequestBody | User object to be created with optional parameters (identifier, is_disabled, metadata)

try:
    # Create user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequestBody**](UserCreateRequestBody.md)| User object to be created with optional parameters (identifier, is_disabled, metadata) | 

### Return type

[**User**](User.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_guid)

Delete user

Calling this endpoint will permanently delete a user from Atrium. If successful, the API will respond with Status: 204 No Content. 

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
api_instance = atrium-python.UsersApi(atrium-python.ApiClient(configuration))
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Delete user
    api_instance.delete_user(user_guid)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> Users list_users(page=page, records_per_page=records_per_page)

List users

Use this endpoint to list every user you've created in Atrium.

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
api_instance = atrium-python.UsersApi(atrium-python.ApiClient(configuration))
page = 12 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List users
    api_response = api_instance.list_users(page=page, records_per_page=records_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**Users**](Users.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_user**
> User read_user(user_guid)

Read user

Use this endpoint to read the attributes of a specific user.

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
api_instance = atrium-python.UsersApi(atrium-python.ApiClient(configuration))
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.

try:
    # Read user
    api_response = api_instance.read_user(user_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->read_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**User**](User.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_guid, body=body)

Update user

Use this endpoint to update the attributes of a specific user. Atrium will respond with the updated user object.<br> Disabling a user means that accounts and transactions associated with it will not be updated in the background by MX. It will also restrict access to that user's data until they are no longer disabled. Users who are disabled for the entirety of an Atrium billing period will not be factored into that month's bill.<br> To disable a user, update it and set the is_disabled parameter to true. Set it to false to re-enable the user. 

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
api_instance = atrium-python.UsersApi(atrium-python.ApiClient(configuration))
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.
body = atrium-python.UserUpdateRequestBody() # UserUpdateRequestBody | User object to be updated with optional parameters (identifier, is_disabled, metadata) (optional)

try:
    # Update user
    api_response = api_instance.update_user(user_guid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **body** | [**UserUpdateRequestBody**](UserUpdateRequestBody.md)| User object to be updated with optional parameters (identifier, is_disabled, metadata) | [optional] 

### Return type

[**User**](User.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

