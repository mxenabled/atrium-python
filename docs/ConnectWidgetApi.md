# atrium.ConnectWidgetApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connect_widget**](ConnectWidgetApi.md#get_connect_widget) | **POST** /users/{user_guid}/connect_widget_url | Embedding in a website


# **get_connect_widget**
> ConnectWidgetResponseBody get_connect_widget(user_guid, body)

Embedding in a website

This endpoint will return a URL for an embeddable version of MX Connect.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

user_guid = "USR-123" # str | The unique identifier for a `user`.
body = atrium.ConnectWidgetRequestBody() # ConnectWidgetRequestBody | Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials)

try:
    # Embedding in a website
    response = client.connect_widget.get_connect_widget(user_guid, body)
    pprint(response)
except ApiException as e:
    print("Exception when calling ConnectWidgetApi->get_connect_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **body** | [**ConnectWidgetRequestBody**](ConnectWidgetRequestBody.md)| Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) | 

### Return type

[**ConnectWidgetResponseBody**](ConnectWidgetResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

