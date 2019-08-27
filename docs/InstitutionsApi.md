# atrium.InstitutionsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_institutions**](InstitutionsApi.md#list_institutions) | **GET** /institutions | List institutions
[**read_institution**](InstitutionsApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution
[**read_institution_credentials**](InstitutionsApi.md#read_institution_credentials) | **GET** /institutions/{institution_code}/credentials | Read institution credentials


# **list_institutions**
> InstitutionsResponseBody list_institutions(name=name, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)

List institutions

This endpoint allows you to see what institutions are available for connection. Information returned will include the institution_code assigned to a particular institution, URLs for the financial institution's logo, and the URL for its website.<br> This endpoint takes an optional query string, name={string}. This will list only institutions in which the appended string appears. 

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

name = name_example # str | This will list only institutions in which the appended string appears. (optional)
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)
supports_account_identification = true # bool | Filter only institutions which support account identification. (optional)
supports_account_statement = true # bool | Filter only institutions which support account statements. (optional)
supports_account_verification = true # bool | Filter only institutions which support account verification. (optional)
supports_transaction_history = true # bool | Filter only institutions which support extended transaction history. (optional)

try:
    # List institutions
    response = client.institutions.list_institutions(name=name, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)
    pprint(response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->list_institutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| This will list only institutions in which the appended string appears. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **supports_account_identification** | **bool**| Filter only institutions which support account identification. | [optional] 
 **supports_account_statement** | **bool**| Filter only institutions which support account statements. | [optional] 
 **supports_account_verification** | **bool**| Filter only institutions which support account verification. | [optional] 
 **supports_transaction_history** | **bool**| Filter only institutions which support extended transaction history. | [optional] 

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

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

institution_code = "example_institution_code" # str | The institution_code of the institution.

try:
    # Read institution
    response = client.institutions.read_institution(institution_code)
    pprint(response)
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

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

institution_code = "example_institution_code" # str | The institution_code of the institution.

try:
    # Read institution credentials
    response = client.institutions.read_institution_credentials(institution_code)
    pprint(response)
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

