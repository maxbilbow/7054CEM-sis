# swagger_client.ClaimHistoryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_note**](ClaimHistoryApi.md#add_note) | **POST** /claim/{claim_id}/history | Add note
[**get_history**](ClaimHistoryApi.md#get_history) | **GET** /claim/{claim_id}/history | Get history for a claim
[**get_note**](ClaimHistoryApi.md#get_note) | **GET** /claim-history/{note_id} | Get claim note

# **add_note**
> ClaimNote add_note(body, claim_id)

Add note

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimHistoryApi()
body = swagger_client.ClaimNote() # ClaimNote | 
claim_id = 56 # int | The id of the claim

try:
    # Add note
    api_response = api_instance.add_note(body, claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimHistoryApi->add_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClaimNote**](ClaimNote.md)|  | 
 **claim_id** | **int**| The id of the claim | 

### Return type

[**ClaimNote**](ClaimNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history**
> ClaimHistory get_history(claim_id)

Get history for a claim

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimHistoryApi()
claim_id = 56 # int | The id of the claim

try:
    # Get history for a claim
    api_response = api_instance.get_history(claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimHistoryApi->get_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claim_id** | **int**| The id of the claim | 

### Return type

[**ClaimHistory**](ClaimHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> ClaimNote get_note(note_id)

Get claim note

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimHistoryApi()
note_id = 56 # int | The id of the history item

try:
    # Get claim note
    api_response = api_instance.get_note(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimHistoryApi->get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| The id of the history item | 

### Return type

[**ClaimNote**](ClaimNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

