# atrium-python.ConnectWidgetApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connect_widget**](ConnectWidgetApi.md#get_connect_widget) | **POST** /users/{user_guid}/connect_widget_url | Embedding in a website


# **get_connect_widget**
> ConnectWidget get_connect_widget(user_guid, body)

Embedding in a website

This endpoint will return a URL for an embeddable version of MX Connect.

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
api_instance = atrium-python.ConnectWidgetApi(atrium-python.ApiClient(configuration))
user_guid = 'user_guid_example' # str | The unique identifier for a `user`.
body = atrium-python.ConnectWidgetRequestBody() # ConnectWidgetRequestBody | Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials)

try:
    # Embedding in a website
    api_response = api_instance.get_connect_widget(user_guid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectWidgetApi->get_connect_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **body** | [**ConnectWidgetRequestBody**](ConnectWidgetRequestBody.md)| Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) | 

### Return type

[**ConnectWidget**](ConnectWidget.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

