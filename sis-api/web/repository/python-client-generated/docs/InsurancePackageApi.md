# swagger_client.InsurancePackageApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_package**](InsurancePackageApi.md#create_package) | **POST** /user/{user_id}/insurance_package | Create new package
[**delete_package**](InsurancePackageApi.md#delete_package) | **DELETE** /user/{user_id}/insurance_package/{package_id} | Delete application
[**get_active**](InsurancePackageApi.md#get_active) | **GET** /user/{user_id}/insurance_package | Get active packages
[**get_all**](InsurancePackageApi.md#get_all) | **GET** /user/{user_id}/insurance_package/{package_id} | Gets all packages for a user
[**update**](InsurancePackageApi.md#update) | **PUT** /user/{user_id}/insurance_package | Update package

# **create_package**
> create_package(body, user_id)

Create new package

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InsurancePackageApi()
body = swagger_client.InsurancePolicy()  # InsurancePolicy | Package to create
user_id = 56  # int | The id of the user

try:
    # Create new package
    api_instance.create_package(body, user_id)
except ApiException as e:
    print("Exception when calling InsurancePackageApi->create_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsurancePolicy**](InsurancePackage.md)| Package to create | 
 **user_id** | **int**| The id of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_package**
> delete_package(user_id, package_id)

Delete application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InsurancePackageApi()
user_id = 56 # int | The id of the user to remove
package_id = 56 # int | The id of the insurance package

try:
    # Delete application
    api_instance.delete_package(user_id, package_id)
except ApiException as e:
    print("Exception when calling InsurancePackageApi->delete_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user to remove | 
 **package_id** | **int**| The id of the insurance package | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active**
> InsurancePackages get_active(user_id)

Get active packages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InsurancePackageApi()
user_id = 56 # int | The id of the user

try:
    # Get active packages
    api_response = api_instance.get_active(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsurancePackageApi->get_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

[**InsurancePackages**](InsurancePackages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> InsurancePolicy get_all(user_id, package_id)

Gets all packages for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InsurancePackageApi()
user_id = 56 # int | The id of the user
package_id = 56 # int | The id of the insurance package

try:
    # Gets all packages for a user
    api_response = api_instance.get_all(user_id, package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsurancePackageApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **package_id** | **int**| The id of the insurance package | 

### Return type

[**InsurancePolicy**](InsurancePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(body, user_id)

Update package

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InsurancePackageApi()
body = swagger_client.InsurancePolicy()  # InsurancePolicy | Package to create
user_id = 56  # int | The id of the user

try:
    # Update package
    api_instance.update_by_pk(body, user_id)
except ApiException as e:
    print("Exception when calling InsurancePackageApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsurancePolicy**](InsurancePackage.md)| Package to create | 
 **user_id** | **int**| The id of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

