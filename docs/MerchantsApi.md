# atrium.MerchantsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_merchant**](MerchantsApi.md#read_merchant) | **GET** /merchants/{merchant_guid} | Read merchant


# **read_merchant**
> MerchantResponseBody read_merchant(merchant_guid)

Read merchant

Returns information about a particular merchant, such as a logo, name, and website.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

merchant_guid = "MCH-123" # str | The unique identifier for a `merchant`.

try:
    # Read merchant
    response = client.merchants.read_merchant(merchant_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MerchantsApi->read_merchant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_guid** | **str**| The unique identifier for a &#x60;merchant&#x60;. | 

### Return type

[**MerchantResponseBody**](MerchantResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

