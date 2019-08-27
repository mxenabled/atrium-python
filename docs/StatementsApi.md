# atrium.StatementsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_statement_pdf**](StatementsApi.md#download_statement_pdf) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid}.pdf | Download statement PDF
[**fetch_statements**](StatementsApi.md#fetch_statements) | **POST** /users/{user_guid}/members/{member_guid}/fetch_statements | Fetch statements
[**list_member_statements**](StatementsApi.md#list_member_statements) | **GET** /users/{user_guid}/members/{member_guid}/statements | List member statements
[**read_member_statement**](StatementsApi.md#read_member_statement) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid} | Read statement JSON


# **download_statement_pdf**
> file download_statement_pdf(member_guid, user_guid, statement_guid)

Download statement PDF

Use this endpoint to download a specified statement. The endpoint URL is the same as the URI given in each `statement` object. 

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

member_guid = "MBR-123" # str | The unique identifier for a `member`.
user_guid = "USR-123" # str | The unique identifier for a `user`.
statement_guid = "STA-123" # str | The unique identifier for an `statement`.

try:
    # Download statement PDF
    response = client.statements.download_statement_pdf(member_guid, user_guid, statement_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling StatementsApi->download_statement_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **statement_guid** | **str**| The unique identifier for an &#x60;statement&#x60;. | 

### Return type

[**file**](file.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_statements**
> MemberResponseBody fetch_statements(member_guid, user_guid)

Fetch statements

The fetch statements endpoint begins fetching statements for a member.

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

member_guid = "MBR-123" # str | The unique identifier for a `member`.
user_guid = "USR-123" # str | The unique identifier for a `user`.

try:
    # Fetch statements
    response = client.statements.fetch_statements(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling StatementsApi->fetch_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_statements**
> StatementsResponseBody list_member_statements(member_guid, user_guid, page=page, records_per_page=records_per_page)

List member statements

Certain institutions in Atrium allow developers to access account statements associated with a particular `member`. Use this endpoint to get an array of available statements.  Before this endpoint can be used, `fetch_statements` should be performed on the relevant `member`. 

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

member_guid = "MBR-123" # str | The unique identifier for a `member`.
user_guid = "USR-123" # str | The unique identifier for a `user`.
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List member statements
    response = client.statements.list_member_statements(member_guid, user_guid, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling StatementsApi->list_member_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**StatementsResponseBody**](StatementsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_member_statement**
> StatementResponseBody read_member_statement(member_guid, user_guid, statement_guid)

Read statement JSON

Use this endpoint to download a specified statement. The endpoint URL is the same as the URI given in each `statement` object. 

### Example
```python
from __future__ import print_function
import time
import atrium
from atrium.rest import ApiException
from pprint import pprint

# create an instance of the AtriumClient
client = atrium.AtriumClient("YOUR_API_KEY", "YOUR_CLIENT_ID", "https://vestibule.mx.com")

member_guid = "MBR-123" # str | The unique identifier for a `member`.
user_guid = "USR-123" # str | The unique identifier for a `user`.
statement_guid = "STA-123" # str | The unique identifier for an `statement`.

try:
    # Read statement JSON
    response = client.statements.read_member_statement(member_guid, user_guid, statement_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling StatementsApi->read_member_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **statement_guid** | **str**| The unique identifier for an &#x60;statement&#x60;. | 

### Return type

[**StatementResponseBody**](StatementResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

