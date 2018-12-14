# atrium.InstitutionsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_institutions**](InstitutionsApi.md#list_institutions) | **GET** /institutions | List institutions
[**read_institution**](InstitutionsApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution
[**read_institution_credentials**](InstitutionsApi.md#read_institution_credentials) | **GET** /institutions/{institution_code}/credentials | Read institution credentials


# **list_institutions**
> InstitutionsResponseBody list_institutions(name=name, page=page, records_per_page=records_per_page)

List institutions

This endpoint allows you to see what institutions are available for connection. Information returned will include the institution_code assigned to a particular institution, URLs for the financial institution's logo, and the URL for its website.<br> This endpoint takes an optional query string, name={string}. This will list only institutions in which the appended string appears. 

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# Configure API Key authorization
configuration = atrium.Configuration()
configuration.headers['MX-API-Key'] = 'YOUR_API_KEY'

# Configure Client ID authorization
configuration.headers['MX-Client-ID'] = 'YOUR_CLIENT_ID'

# create an instance of the API class
api_instance = atrium.InstitutionsApi()
name = 'name_example' # str | This will list only institutions in which the appended string appears. (optional)
page = 12 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List institutions
    api_response = api_instance.list_institutions(name=name, page=page, records_per_page=records_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->list_institutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| This will list only institutions in which the appended string appears. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**InstitutionsResponseBody**](InstitutionsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_institution**
> InstitutionResponseBody read_institution(institution_code)

Read institution

This endpoint allows you to see information for a specific institution.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# Configure API Key authorization
configuration = atrium.Configuration()
configuration.headers['MX-API-Key'] = 'YOUR_API_KEY'

# Configure Client ID authorization
configuration.headers['MX-Client-ID'] = 'YOUR_CLIENT_ID'

# create an instance of the API class
api_instance = atrium.InstitutionsApi()
institution_code = 'institution_code_example' # str | The institution_code of the institution.

try:
    # Read institution
    api_response = api_instance.read_institution(institution_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->read_institution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_code** | **str**| The institution_code of the institution. | 

### Return type

[**InstitutionResponseBody**](InstitutionResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_institution_credentials**
> CredentialsResponseBody read_institution_credentials(institution_code)

Read institution credentials

Use this endpoint to see which credentials will be needed to create a member for a specific institution.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# Configure API Key authorization
configuration = atrium.Configuration()
configuration.headers['MX-API-Key'] = 'YOUR_API_KEY'

# Configure Client ID authorization
configuration.headers['MX-Client-ID'] = 'YOUR_CLIENT_ID'

# create an instance of the API class
api_instance = atrium.InstitutionsApi()
institution_code = 'institution_code_example' # str | The institution_code of the institution.

try:
    # Read institution credentials
    api_response = api_instance.read_institution_credentials(institution_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->read_institution_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_code** | **str**| The institution_code of the institution. | 

### Return type

[**CredentialsResponseBody**](CredentialsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

