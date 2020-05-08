# atrium.MembersApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_member**](MembersApi.md#aggregate_member) | **POST** /users/{user_guid}/members/{member_guid}/aggregate | Aggregate member
[**aggregate_member_balances**](MembersApi.md#aggregate_member_balances) | **POST** /users/{user_guid}/members/{member_guid}/balance | Aggregate member account balances
[**create_member**](MembersApi.md#create_member) | **POST** /users/{user_guid}/members | Create member
[**delete_member**](MembersApi.md#delete_member) | **DELETE** /users/{user_guid}/members/{member_guid} | Delete member
[**extend_history**](MembersApi.md#extend_history) | **POST** /users/{user_guid}/members/{member_guid}/extend_history | Extend history
[**list_member_accounts**](MembersApi.md#list_member_accounts) | **GET** /users/{user_guid}/members/{member_guid}/accounts | List member accounts
[**list_member_credentials**](MembersApi.md#list_member_credentials) | **GET** /users/{user_guid}/members/{member_guid}/credentials | List member credentials
[**list_member_mfa_challenges**](MembersApi.md#list_member_mfa_challenges) | **GET** /users/{user_guid}/members/{member_guid}/challenges | List member MFA challenges
[**list_member_transactions**](MembersApi.md#list_member_transactions) | **GET** /users/{user_guid}/members/{member_guid}/transactions | List member transactions
[**list_members**](MembersApi.md#list_members) | **GET** /users/{user_guid}/members | List members
[**read_member**](MembersApi.md#read_member) | **GET** /users/{user_guid}/members/{member_guid} | Read member
[**read_member_status**](MembersApi.md#read_member_status) | **GET** /users/{user_guid}/members/{member_guid}/status | Read member connection status
[**read_o_auth_window_uri**](MembersApi.md#read_o_auth_window_uri) | **GET** /users/{user_guid}/members/{member_guid}/oauth_window_uri | Read OAuth Window URI
[**resume_member**](MembersApi.md#resume_member) | **PUT** /users/{user_guid}/members/{member_guid}/resume | Resume aggregation from MFA
[**update_member**](MembersApi.md#update_member) | **PUT** /users/{user_guid}/members/{member_guid} | Update member


# **aggregate_member**
> MemberResponseBody aggregate_member(member_guid, user_guid)

Aggregate member

Calling this endpoint initiates an aggregation event for the member. This brings in the latest account and transaction data from the connected institution. If this data has recently been updated, MX may not initiate an aggregation event. 

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
    # Aggregate member
    response = client.members.aggregate_member(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->aggregate_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_member_balances**
> MemberResponseBody aggregate_member_balances(member_guid, user_guid)

Aggregate member account balances

This endpoint operates much like the _aggregate member_ endpoint except that it gathers only account balance information; it does not gather any transaction data at all.

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
    # Aggregate member account balances
    response = client.members.aggregate_member_balances(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->aggregate_member_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_member**
> MemberResponseBody create_member(user_guid, body)

Create member

This endpoint allows you to create a new member. Members are created with the required parameters credentials and institution_code, and the optional parameters identifier and metadata.<br> When creating a member, you'll need to include the correct type of credential required by the financial institution and provided by the user. You can find out which credential type is required with the /institutions/{institution_code}/credentials endpoint.<br> If successful, Atrium will respond with the newly-created member object.<br> Once you successfully create a member, MX will immediately validate the provided credentials and attempt to aggregate data for accounts and transactions. 

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
body = atrium.MemberCreateRequestBody() # MemberCreateRequestBody | Member object to be created with optional parameters (identifier and metadata) and required parameters (credentials and institution_code)

try:
    # Create member
    response = client.members.create_member(user_guid, body)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->create_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **body** | [**MemberCreateRequestBody**](MemberCreateRequestBody.md)| Member object to be created with optional parameters (identifier and metadata) and required parameters (credentials and institution_code) | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member**
> delete_member(member_guid, user_guid)

Delete member

Accessing this endpoint will permanently delete a member.

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
    # Delete member
    client.members.delete_member(member_guid, user_guid)
except ApiException as e:
    print("Exception when calling MembersApi->delete_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_history**
> MemberResponseBody extend_history(member_guid, user_guid)

Extend history

The extend_history endpoint begins the process of fetching up to 24 months of data associated with a particular `member`.

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
    # Extend history
    response = client.members.extend_history(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->extend_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_accounts**
> AccountsResponseBody list_member_accounts(member_guid, user_guid, page=page, records_per_page=records_per_page)

List member accounts

This endpoint returns an array with information about every account associated with a particular member.

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
    # List member accounts
    response = client.members.list_member_accounts(member_guid, user_guid, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->list_member_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**AccountsResponseBody**](AccountsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_credentials**
> CredentialsResponseBody list_member_credentials(member_guid, user_guid)

List member credentials

This endpoint returns an array which contains information on every non-MFA credential associated with a specific member.

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
    # List member credentials
    response = client.members.list_member_credentials(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->list_member_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**CredentialsResponseBody**](CredentialsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_mfa_challenges**
> ChallengesResponseBody list_member_mfa_challenges(member_guid, user_guid)

List member MFA challenges

Use this endpoint for information on what multi-factor authentication challenges need to be answered in order to aggregate a member.<br> If the aggregation is not challenged, i.e., the member does not have a connection status of CHALLENGED, then code 204 No Content will be returned.<br> If the aggregation has been challenged, i.e., the member does have a connection status of CHALLENGED, then code 200 OK will be returned — along with the corresponding credentials. 

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
    # List member MFA challenges
    response = client.members.list_member_mfa_challenges(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->list_member_mfa_challenges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**ChallengesResponseBody**](ChallengesResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_transactions**
> TransactionsResponseBody list_member_transactions(member_guid, user_guid, from_date=from_date, to_date=to_date, page=page, records_per_page=records_per_page)

List member transactions

Use this endpoint to get all transactions from all accounts associated with a specific member.<br> This endpoint accepts optional URL query parameters — from_date and to_date — which are used to filter transactions according to the date they were posted. If no values are given for the query parameters, from_date will default to 90 days prior to the request and to_date will default to 5 days from the time of the request. 

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
from_date = "2016-09-20" # str | Filter transactions from this date. (optional)
to_date = "2016-10-20" # str | Filter transactions to this date. (optional)
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List member transactions
    response = client.members.list_member_transactions(member_guid, user_guid, from_date=from_date, to_date=to_date, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->list_member_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**TransactionsResponseBody**](TransactionsResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> MembersResponseBody list_members(user_guid, page=page, records_per_page=records_per_page)

List members

This endpoint returns an array which contains information on every member associated with a specific user.

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
page = 1 # int | Specify current page. (optional)
records_per_page = 12 # int | Specify records per page. (optional)

try:
    # List members
    response = client.members.list_members(user_guid, page=page, records_per_page=records_per_page)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**MembersResponseBody**](MembersResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_member**
> MemberResponseBody read_member(member_guid, user_guid)

Read member

Use this endpoint to read the attributes of a specific member.

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
    # Read member
    response = client.members.read_member(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->read_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_member_status**
> MemberConnectionStatusResponseBody read_member_status(member_guid, user_guid)

Read member connection status

This endpoint provides the status of the member's most recent aggregation event. This is an important step in the aggregation process, and the results returned by this endpoint should determine what you do next in order to successfully aggregate a member.<br> MX has introduced new, more detailed information on the current status of a member's connection to a financial institution and the state of its aggregation: the connection_status field. These are intended to replace and expand upon the information provided in the status field, which will soon be deprecated; support for the status field remains for the time being. 

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
    # Read member connection status
    response = client.members.read_member_status(member_guid, user_guid)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->read_member_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

### Return type

[**MemberConnectionStatusResponseBody**](MemberConnectionStatusResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_o_auth_window_uri**
> MemberResponseBody read_o_auth_window_uri(member_guid, user_guid, referral_source=referral_source, ui_message_webview_url_scheme=ui_message_webview_url_scheme)

Read OAuth Window URI

This endpoint will generate an `oauth_window_uri` for the specified `member`.

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
referral_source = "BROWSER" # str | Should be either BROWSER or APP depending on the implementation. (optional)
ui_message_webview_url_scheme = "ui_message_webview_url_scheme_example" # str | A scheme for routing the user back to the application state they were previously in. (optional)

try:
    # Read OAuth Window URI
    response = client.members.read_o_auth_window_uri(member_guid, user_guid, referral_source=referral_source, ui_message_webview_url_scheme=ui_message_webview_url_scheme)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->read_o_auth_window_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **referral_source** | **str**| Should be either BROWSER or APP depending on the implementation. | [optional] 
 **ui_message_webview_url_scheme** | **str**| A scheme for routing the user back to the application state they were previously in. | [optional] 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_member**
> MemberResponseBody resume_member(member_guid, user_guid, body)

Resume aggregation from MFA

This endpoint answers the challenges needed when a member has been challenged by multi-factor authentication.

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
body = atrium.MemberResumeRequestBody() # MemberResumeRequestBody | Member object with MFA challenge answers

try:
    # Resume aggregation from MFA
    response = client.members.resume_member(member_guid, user_guid, body)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->resume_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **body** | [**MemberResumeRequestBody**](MemberResumeRequestBody.md)| Member object with MFA challenge answers | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member**
> MemberResponseBody update_member(member_guid, user_guid, body=body)

Update member

Use this endpoint to update a member's attributes. Only the credentials, identifier, and metadata parameters can be updated. To get a list of the required credentials for the member, use the list member credentials endpoint. 

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
body = atrium.MemberUpdateRequestBody() # MemberUpdateRequestBody | Member object to be updated with optional parameters (credentials, identifier, metadata) (optional)

try:
    # Update member
    response = client.members.update_member(member_guid, user_guid, body=body)
    pprint(response)
except ApiException as e:
    print("Exception when calling MembersApi->update_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 
 **body** | [**MemberUpdateRequestBody**](MemberUpdateRequestBody.md)| Member object to be updated with optional parameters (credentials, identifier, metadata) | [optional] 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

