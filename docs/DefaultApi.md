# openapi_client.DefaultApi

All URIs are relative to *http://localhost/api/v0.8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](DefaultApi.md#create_bucket) | **POST** /buckets | 
[**create_object**](DefaultApi.md#create_object) | **POST** /buckets/{bucket}/objects | 
[**create_session**](DefaultApi.md#create_session) | **POST** /session/{bucket}/object | 
[**delete_bucket**](DefaultApi.md#delete_bucket) | **DELETE** /buckets/{bucket} | 
[**delete_object**](DefaultApi.md#delete_object) | **DELETE** /buckets/{bucket}/objects/{object} | 
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /users/{user}/management | 
[**download_object_data**](DefaultApi.md#download_object_data) | **GET** /buckets/{bucket}/objects/{object}/download | 
[**get_bucket**](DefaultApi.md#get_bucket) | **GET** /buckets/{bucket} | 
[**get_metrics**](DefaultApi.md#get_metrics) | **GET** /metrics | 
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{user}/management | 
[**get_user_by_address**](DefaultApi.md#get_user_by_address) | **GET** /users/searchByAddress/{address} | 
[**get_user_list**](DefaultApi.md#get_user_list) | **GET** /users/list | 
[**list_buckets**](DefaultApi.md#list_buckets) | **GET** /buckets | 
[**list_objects**](DefaultApi.md#list_objects) | **GET** /buckets/{bucket}/objects | 
[**object_metadata**](DefaultApi.md#object_metadata) | **GET** /buckets/{bucket}/objects/{object}/metadata | 
[**save_user**](DefaultApi.md#save_user) | **POST** /users/{user}/management | 
[**set_eacl**](DefaultApi.md#set_eacl) | **POST** /eacl/{bucket} | 
[**store_session**](DefaultApi.md#store_session) | **POST** /session/store | 
[**top_up_storage_node**](DefaultApi.md#top_up_storage_node) | **POST** /cluster/topup | 


# **create_bucket**
> create_bucket(x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature, create_bucket_request=create_bucket_request)



Create a new bucket.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.create_bucket_request import CreateBucketRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64.
    x_morph_payload = 'x_morph_payload_example' # str | Payload in base64. This data client used to sign request. Required if x-morph-payload-signature is set. (optional)
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. (optional)
    create_bucket_request = openapi_client.CreateBucketRequest() # CreateBucketRequest | Parameters of the new bucket in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.create_bucket(x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature, create_bucket_request=create_bucket_request)
    except Exception as e:
        print("Exception when calling DefaultApi->create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | 
 **x_morph_payload** | **str**| Payload in base64. This data client used to sign request. Required if x-morph-payload-signature is set. | [optional] 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | [optional] 
 **create_bucket_request** | [**CreateBucketRequest**](CreateBucketRequest.md)| Parameters of the new bucket in JSON. Required only for payload generation request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bucket successfully created. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Missing signature. |  * x-morph-payload - Payload in base64 which should be signed by client. <br>  |
**409** | Bucket already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object**
> create_object(bucket, x_morph_public_key, x_morph_unified_session_token, name, data, lifetime=lifetime)



Create a new object in the bucket.

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64.
    x_morph_unified_session_token = 'x_morph_unified_session_token_example' # str | Unified session token.
    name = 'name_example' # str | Object name.
    data = None # bytearray | 
    lifetime = 56 # int | Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. (optional)

    try:
        api_instance.create_object(bucket, x_morph_public_key, x_morph_unified_session_token, name, data, lifetime=lifetime)
    except Exception as e:
        print("Exception when calling DefaultApi->create_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | 
 **x_morph_unified_session_token** | **str**| Unified session token. | 
 **name** | **str**| Object name. | 
 **data** | **bytearray**|  | 
 **lifetime** | **int**| Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Object successfully created. |  -  |
**400** | At least one object parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  -  |
**403** | User is not authorized to make this action in the bucket |  -  |
**409** | Object already exists. |  -  |
**507** | User doesn&#39;t have enough space. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> List[SessionToken] create_session(bucket, x_morph_public_key)



Create session tokens for object operations.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.session_token import SessionToken
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64.

    try:
        api_response = api_instance.create_session(bucket, x_morph_public_key)
        print("The response of DefaultApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | 

### Return type

[**List[SessionToken]**](SessionToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> delete_bucket(bucket, x_morph_public_key=x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature)



Delete bucket from the system.

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64. (optional)
    x_morph_payload = 'x_morph_payload_example' # str | Payload in base64. This data client used to sign request. Required if x-morph-payload-signature is set. (optional)
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. (optional)

    try:
        api_instance.delete_bucket(bucket, x_morph_public_key=x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | [optional] 
 **x_morph_payload** | **str**| Payload in base64. This data client used to sign request. Required if x-morph-payload-signature is set. | [optional] 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bucket successfully removed. |  -  |
**401** | Missing signature. |  * x-morph-payload - Payload in base64 which should be signed by client. <br>  |
**404** | Bucket not found (not created or already removed). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object**
> delete_object(bucket, object, x_morph_unified_session_token)



Delete object from the bucket.

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'object_example' # str | Object name.
    x_morph_unified_session_token = 'x_morph_unified_session_token_example' # str | Unified session token.

    try:
        api_instance.delete_object(bucket, object, x_morph_unified_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name. | 
 **x_morph_unified_session_token** | **str**| Unified session token. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object successfully removed. |  -  |
**401** | Authentication token is invalid, missing or expired. |  -  |
**403** | User is not authorized to make this action in the bucket |  -  |
**404** | Bucket or object not found (not created or already removed). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user, x_morph_address, x_morph_payload_signature=x_morph_payload_signature, user_management_delete_request=user_management_delete_request)



Delete a user. If superKey passed, the signature should be calculated using body payload, otherwise use username as payload.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_management_delete_request import UserManagementDeleteRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, superkey or any users name.' # str | User name.
    x_morph_address = 'NSqa4SBqn1h8KTkyVbTSASi3eaHCbEumLv.' # str | Account's address.
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. (optional)
    user_management_delete_request = openapi_client.UserManagementDeleteRequest() # UserManagementDeleteRequest |  (optional)

    try:
        api_instance.delete_user(user, x_morph_address, x_morph_payload_signature=x_morph_payload_signature, user_management_delete_request=user_management_delete_request)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_address** | **str**| Account&#39;s address. | 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | [optional] 
 **user_management_delete_request** | [**UserManagementDeleteRequest**](UserManagementDeleteRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully deleted. |  -  |
**400** | Passed user name is invalid. |  -  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_object_data**
> bytearray download_object_data(bucket, object, x_morph_unified_session_token=x_morph_unified_session_token)



Download the object data.

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'object_example' # str | Object name.
    x_morph_unified_session_token = 'x_morph_unified_session_token_example' # str | Unified session token. (optional)

    try:
        api_response = api_instance.download_object_data(bucket, object, x_morph_unified_session_token=x_morph_unified_session_token)
        print("The response of DefaultApi->download_object_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_object_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name. | 
 **x_morph_unified_session_token** | **str**| Unified session token. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication token is invalid, missing or expired. |  -  |
**403** | User is not authorized to make this action in the bucket |  -  |
**404** | Bucket or object not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucket**
> GetBucketResponse get_bucket(bucket)



Get information about the bucket by name.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.get_bucket_response import GetBucketResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.

    try:
        api_response = api_instance.get_bucket(bucket)
        print("The response of DefaultApi->get_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 

### Return type

[**GetBucketResponse**](GetBucketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bucket reference is missing or invalid. |  -  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**
> GetMetricsResponse get_metrics()



Scrape system metrics.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.get_metrics_response import GetMetricsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_metrics()
        print("The response of DefaultApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetricsResponse**](GetMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserResponse get_user(user)



Get user or superkey file. File name must be without extension.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.get_user_response import GetUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, superkey or any users name.' # str | User name.

    try:
        api_response = api_instance.get_user(user)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User found. |  -  |
**400** | User name is empty. |  -  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_address**
> GetUserResponse get_user_by_address(address)



Get user key by owner address.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.get_user_response import GetUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    address = 'NayAFknUh2iNAtJuYkqEENQDEaX27YnsTL.' # str | User address.

    try:
        api_response = api_instance.get_user_by_address(address)
        print("The response of DefaultApi->get_user_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| User address. | 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User found. |  -  |
**400** | Address is empty. |  -  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_list**
> GetUserListResponse get_user_list()



Get user list.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.get_user_list_response import GetUserListResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_user_list()
        print("The response of DefaultApi->get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserListResponse**](GetUserListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full list of users in system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buckets**
> ListBucketsResponse list_buckets(x_morph_public_key=x_morph_public_key)



List all buckets in the system.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.list_buckets_response import ListBucketsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64. (optional)

    try:
        api_response = api_instance.list_buckets(x_morph_public_key=x_morph_public_key)
        print("The response of DefaultApi->list_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | [optional] 

### Return type

[**ListBucketsResponse**](ListBucketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_objects**
> ListObjectsResponse list_objects(bucket, x_morph_unified_session_token)



List all objects in the bucket with brief metadata.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.list_objects_response import ListObjectsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_unified_session_token = 'x_morph_unified_session_token_example' # str | Unified session token.

    try:
        api_response = api_instance.list_objects(bucket, x_morph_unified_session_token)
        print("The response of DefaultApi->list_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_unified_session_token** | **str**| Unified session token. | 

### Return type

[**ListObjectsResponse**](ListObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication token is invalid, missing or expired. |  -  |
**403** | User is not authorized to make this action in the bucket |  -  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_metadata**
> ObjectMetadataResponse object_metadata(bucket, object, x_morph_unified_session_token)



Get the object metadata.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.object_metadata_response import ObjectMetadataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'object_example' # str | Object name.
    x_morph_unified_session_token = 'x_morph_unified_session_token_example' # str | Unified session token.

    try:
        api_response = api_instance.object_metadata(bucket, object, x_morph_unified_session_token)
        print("The response of DefaultApi->object_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->object_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name. | 
 **x_morph_unified_session_token** | **str**| Unified session token. | 

### Return type

[**ObjectMetadataResponse**](ObjectMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication token is invalid, missing or expired. |  -  |
**403** | User is not authorized to make this action in the bucket |  -  |
**404** | Bucket or object not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user**
> save_user(x_morph_address, user, x_morph_payload_signature=x_morph_payload_signature, user_management_request=user_management_request)



Register user or change user role.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_management_request import UserManagementRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_address = 'NSqa4SBqn1h8KTkyVbTSASi3eaHCbEumLv.' # str | Account's address.
    user = 'mike, superkey or any users name.' # str | User name.
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. (optional)
    user_management_request = openapi_client.UserManagementRequest() # UserManagementRequest |  (optional)

    try:
        api_instance.save_user(x_morph_address, user, x_morph_payload_signature=x_morph_payload_signature, user_management_request=user_management_request)
    except Exception as e:
        print("Exception when calling DefaultApi->save_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_address** | **str**| Account&#39;s address. | 
 **user** | **str**| User name. | 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | [optional] 
 **user_management_request** | [**UserManagementRequest**](UserManagementRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User successfully registered. |  -  |
**400** | Passed wallet or account data is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_eacl**
> set_eacl(bucket, x_morph_public_key=x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature, set_eacl_request=set_eacl_request)



Set EACL to the bucket.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.set_eacl_request import SetEaclRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64. (optional)
    x_morph_payload = 'x_morph_payload_example' # str | Payload in base64. This data client used to sign request. Required if x-morph-payload-signature is set. (optional)
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. (optional)
    set_eacl_request = openapi_client.SetEaclRequest() # SetEaclRequest | Parameters of the new EACL in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.set_eacl(bucket, x_morph_public_key=x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature, set_eacl_request=set_eacl_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_eacl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | [optional] 
 **x_morph_payload** | **str**| Payload in base64. This data client used to sign request. Required if x-morph-payload-signature is set. | [optional] 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | [optional] 
 **set_eacl_request** | [**SetEaclRequest**](SetEaclRequest.md)| Parameters of the new EACL in JSON. Required only for payload generation request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EACL successfully put. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Missing signature. |  * x-morph-payload - Payload in base64 which should be signed by client. <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_session**
> StoreSessionResponse store_session(x_morph_public_key, signed_session_token=signed_session_token)



Exchange object operations session tokens for a unified one. It will be used instead of them in object operations.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.signed_session_token import SignedSessionToken
from openapi_client.models.store_session_response import StoreSessionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_public_key = 'x_morph_public_key_example' # str | Account's public key, encoded in base64.
    signed_session_token = [openapi_client.SignedSessionToken()] # List[SignedSessionToken] |  (optional)

    try:
        api_response = api_instance.store_session(x_morph_public_key, signed_session_token=signed_session_token)
        print("The response of DefaultApi->store_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->store_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_public_key** | **str**| Account&#39;s public key, encoded in base64. | 
 **signed_session_token** | [**List[SignedSessionToken]**](SignedSessionToken.md)|  | [optional] 

### Return type

[**StoreSessionResponse**](StoreSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token successfully created. |  -  |
**400** | At least one object parameter is invalid (e.g. required parameter is missing). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_up_storage_node**
> top_up_storage_node(storage_node_top_up_account=storage_node_top_up_account)



Top up storage node account with minimal deposit to pay network candidate fee.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.storage_node_top_up_account import StorageNodeTopUpAccount
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v0.8
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api/v0.8"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    storage_node_top_up_account = openapi_client.StorageNodeTopUpAccount() # StorageNodeTopUpAccount |  (optional)

    try:
        api_instance.top_up_storage_node(storage_node_top_up_account=storage_node_top_up_account)
    except Exception as e:
        print("Exception when calling DefaultApi->top_up_storage_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_node_top_up_account** | [**StorageNodeTopUpAccount**](StorageNodeTopUpAccount.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balance successfully recharged. |  -  |
**400** | Address is invalid. |  -  |
**500** | Address topping-up is failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

