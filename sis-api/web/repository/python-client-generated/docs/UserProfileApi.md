# swagger_client.UserProfileApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_profile**](UserProfileApi.md#create_profile) | **POST** /user/{user_id}/profile | Create a user profile
[**get_profile**](UserProfileApi.md#get_profile) | **GET** /user/{user_id}/profile | Get a user profile
[**remove_profile**](UserProfileApi.md#remove_profile) | **DELETE** /user/{user_id}/profile | Remove a user profile
[**update_profile**](UserProfileApi.md#update_profile) | **PUT** /user/{user_id}/profile | Update and replace a user profile

# **create_profile**
> create_profile(body, user_id)

Create a user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApi()
body = swagger_client.UserProfile() # UserProfile | 
user_id = 56 # int | The id of the user to update

try:
    # Create a user profile
    api_instance.create_profile(body, user_id)
except ApiException as e:
    print("Exception when calling UserProfileApi->create_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserProfile**](UserProfile.md)|  | 
 **user_id** | **int**| The id of the user to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> UserProfile get_profile(user_id)

Get a user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApi()
user_id = 56 # int | The id of the user to retrieve

try:
    # Get a user profile
    api_response = api_instance.get_profile(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfileApi->get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user to retrieve | 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_profile**
> remove_profile(user_id)

Remove a user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApi()
user_id = 56 # int | The id of the user to remove

try:
    # Remove a user profile
    api_instance.remove_profile(user_id)
except ApiException as e:
    print("Exception when calling UserProfileApi->remove_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> update_profile(body, user_id)

Update and replace a user profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApi()
body = swagger_client.UserProfile() # UserProfile | 
user_id = 56 # int | The id of the user to update

try:
    # Update and replace a user profile
    api_instance.update_profile(body, user_id)
except ApiException as e:
    print("Exception when calling UserProfileApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserProfile**](UserProfile.md)|  | 
 **user_id** | **int**| The id of the user to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

