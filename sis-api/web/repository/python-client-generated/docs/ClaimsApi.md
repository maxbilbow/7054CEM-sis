# swagger_client.ClaimsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_for_package**](ClaimsApi.md#get_for_package) | **GET** /package/{package_id}/claim | Get all claims for a package
[**get_for_user**](ClaimsApi.md#get_for_user) | **GET** /user/{user_id}/claim | Get all claims for a user
[**get_one**](ClaimsApi.md#get_one) | **GET** /claim/{claim_id} | Get all claims for a package
[**new_claim**](ClaimsApi.md#new_claim) | **POST** /user/{user_id}/insurance_package/{package_id} | Create a new claim

# **get_for_package**
> Claims get_for_package(package_id)

Get all claims for a package

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimsApi()
package_id = 56 # int | The id of the package

try:
    # Get all claims for a package
    api_response = api_instance.get_for_package(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimsApi->get_for_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **int**| The id of the package | 

### Return type

[**Claims**](Claims.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_for_user**
> Claims get_for_user(user_id)

Get all claims for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimsApi()
user_id = 56 # int | The id of the user

try:
    # Get all claims for a user
    api_response = api_instance.get_for_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimsApi->get_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

[**Claims**](Claims.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one**
> Claim get_one(claim_id)

Get all claims for a package

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimsApi()
claim_id = 56 # int | The id of the claim

try:
    # Get all claims for a package
    api_response = api_instance.get_one(claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimsApi->get_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claim_id** | **int**| The id of the claim | 

### Return type

[**Claim**](Claim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_claim**
> Claim new_claim(body, user_id, package_id)

Create a new claim

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimsApi()
body = swagger_client.Claim() # Claim | 
user_id = 56 # int | The id of the user
package_id = 56 # int | The id of the package to claim against

try:
    # Create a new claim
    api_response = api_instance.new_claim(body, user_id, package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimsApi->new_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Claim**](Claim.md)|  | 
 **user_id** | **int**| The id of the user | 
 **package_id** | **int**| The id of the package to claim against | 

### Return type

[**Claim**](Claim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

