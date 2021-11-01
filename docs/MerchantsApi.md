# atrium.MerchantsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_merchant_locations**](MerchantsApi.md#list_merchant_locations) | **GET** /merchants/{merchant_guid}/merchant_locations | List merchant locations
[**list_merchants**](MerchantsApi.md#list_merchants) | **GET** /merchants | List merchants
[**read_merchant**](MerchantsApi.md#read_merchant) | **GET** /merchants/{merchant_guid} | Read merchant
[**read_merchant_location**](MerchantsApi.md#read_merchant_location) | **GET** /merchants/{merchant_guid}/merchant_locations/{merchant_location_guid} | Read merchant location


# **list_merchant_locations**
> MerchantLocationsResponseBody list_merchant_locations(merchant_guid, page=page, records_per_page=records_per_page)

List merchant locations

Returns a list of all the merchant locations associated with a merchant, including physical location, latitude, longitude, etc.

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
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List merchant locations
    response = client.merchants.list_merchant_locations(merchant_guid, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling MerchantsApi->list_merchant_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_guid** | **str**| The unique identifier for a &#x60;merchant&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**MerchantLocationsResponseBody**](MerchantLocationsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_merchants**
> MerchantsResponseBody list_merchants(page=page, records_per_page=records_per_page)

List merchants

Returns a list of merchnants.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List merchants
    response = client.merchants.list_merchants(page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling MerchantsApi->list_merchants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**MerchantsResponseBody**](MerchantsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **read_merchant_location**
> MerchantLocationResponseBody read_merchant_location(merchant_guid, merchant_location_guid)

Read merchant location

Retuns a specific location associated with a merchant, including physical location, latitude, longitude, etc.

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
merchant_location_guid = "MCL-123" # str | The unique identifier for a `merchant_location`.

try:
    # Read merchant location
    response = client.merchants.read_merchant_location(merchant_guid, merchant_location_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MerchantsApi->read_merchant_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_guid** | **str**| The unique identifier for a &#x60;merchant&#x60;. | 
 **merchant_location_guid** | **str**| The unique identifier for a &#x60;merchant_location&#x60;. | 

### Return type

[**MerchantLocationResponseBody**](MerchantLocationResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

