# openapi_client.DefaultApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](DefaultApi.md#create_bucket) | **POST** /v0.8/buckets | 
[**create_object**](DefaultApi.md#create_object) | **POST** /v0.8/buckets/{bucket}/objects | 
[**create_session**](DefaultApi.md#create_session) | **POST** /v0.8/session/{bucket}/object | 
[**delete_bucket**](DefaultApi.md#delete_bucket) | **DELETE** /v0.8/buckets/{bucket} | 
[**delete_object**](DefaultApi.md#delete_object) | **DELETE** /v0.8/buckets/{bucket}/objects/{object} | 
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /v0.8/users/{user}/management | 
[**download_object_data**](DefaultApi.md#download_object_data) | **GET** /v0.8/buckets/{bucket}/objects/{object}/download | 
[**get_bucket**](DefaultApi.md#get_bucket) | **GET** /v0.8/buckets/{bucket} | 
[**get_default_storage_quota**](DefaultApi.md#get_default_storage_quota) | **GET** /v0.8/management/quota | 
[**get_metrics**](DefaultApi.md#get_metrics) | **GET** /v0.8/metrics | 
[**get_user**](DefaultApi.md#get_user) | **GET** /v0.8/users/{user}/management | 
[**get_user_by_address**](DefaultApi.md#get_user_by_address) | **GET** /v0.8/users/searchByAddress/{address} | 
[**get_user_list**](DefaultApi.md#get_user_list) | **GET** /v0.8/users/list | 
[**list_buckets**](DefaultApi.md#list_buckets) | **GET** /v0.8/buckets | 
[**list_objects**](DefaultApi.md#list_objects) | **GET** /v0.8/buckets/{bucket}/objects | 
[**object_metadata**](DefaultApi.md#object_metadata) | **GET** /v0.8/buckets/{bucket}/objects/{object}/metadata | 
[**save_user**](DefaultApi.md#save_user) | **POST** /v0.8/users/{user}/management | 
[**set_default_storage_quota**](DefaultApi.md#set_default_storage_quota) | **POST** /v0.8/management/quota | 
[**set_eacl**](DefaultApi.md#set_eacl) | **POST** /v0.8/eacl/{bucket} | 
[**set_storage_quota**](DefaultApi.md#set_storage_quota) | **POST** /v0.8/users/{user}/management/quota | 
[**store_session**](DefaultApi.md#store_session) | **POST** /v0.8/session/store | 
[**top_up_storage_node**](DefaultApi.md#top_up_storage_node) | **POST** /v0.8/cluster/topup | 
[**v1_apply_sn_action**](DefaultApi.md#v1_apply_sn_action) | **POST** /v1/cluster/storage-node | 
[**v1_create_bucket**](DefaultApi.md#v1_create_bucket) | **POST** /v1/buckets | 
[**v1_create_object**](DefaultApi.md#v1_create_object) | **POST** /v1/buckets/{bucket}/objects | 
[**v1_delete_bucket**](DefaultApi.md#v1_delete_bucket) | **DELETE** /v1/buckets/{bucket} | 
[**v1_delete_object**](DefaultApi.md#v1_delete_object) | **DELETE** /v1/buckets/{bucket}/objects/{object} | 
[**v1_delete_user**](DefaultApi.md#v1_delete_user) | **DELETE** /v1/users/{user} | 
[**v1_download_object**](DefaultApi.md#v1_download_object) | **GET** /v1/buckets/{bucket}/objects/{object} | 
[**v1_get_bucket**](DefaultApi.md#v1_get_bucket) | **GET** /v1/buckets/{bucket} | 
[**v1_get_default_storage_quota**](DefaultApi.md#v1_get_default_storage_quota) | **GET** /v1/cluster/default-quota | 
[**v1_get_metrics**](DefaultApi.md#v1_get_metrics) | **GET** /v1/cluster/metrics | 
[**v1_get_user**](DefaultApi.md#v1_get_user) | **GET** /v1/users/{user} | 
[**v1_get_user_list**](DefaultApi.md#v1_get_user_list) | **GET** /v1/users | 
[**v1_initial_registration**](DefaultApi.md#v1_initial_registration) | **POST** /v1/initial-registration | 
[**v1_list_buckets**](DefaultApi.md#v1_list_buckets) | **GET** /v1/buckets | 
[**v1_list_objects**](DefaultApi.md#v1_list_objects) | **GET** /v1/buckets/{bucket}/objects | 
[**v1_login**](DefaultApi.md#v1_login) | **POST** /v1/login | 
[**v1_object_metadata**](DefaultApi.md#v1_object_metadata) | **GET** /v1/buckets/{bucket}/objects/{object}/metadata | 
[**v1_register_user**](DefaultApi.md#v1_register_user) | **POST** /v1/users/{user} | 
[**v1_s3_get_access_token**](DefaultApi.md#v1_s3_get_access_token) | **GET** /v1/s3/tokens | 
[**v1_set_default_storage_quota**](DefaultApi.md#v1_set_default_storage_quota) | **POST** /v1/cluster/default-quota | 
[**v1_set_eacl**](DefaultApi.md#v1_set_eacl) | **POST** /v1/buckets/{bucket}/eacl | 
[**v1_set_user_storage_quota**](DefaultApi.md#v1_set_user_storage_quota) | **POST** /v1/users/{user}/quota | 
[**v1_update_user**](DefaultApi.md#v1_update_user) | **PUT** /v1/users/{user} | 


# **create_bucket**
> create_bucket(x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature, create_bucket_request=create_bucket_request)



Create a new bucket.

### Example


```python
import openapi_client
from openapi_client.models.create_bucket_request import CreateBucketRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.session_token import SessionToken
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.user_management_delete_request import UserManagementDeleteRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
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
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.get_bucket_response import GetBucketResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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

# **get_default_storage_quota**
> GetDefaultStorageQuotaResponse get_default_storage_quota()



Get default storage quota for user.

### Example


```python
import openapi_client
from openapi_client.models.get_default_storage_quota_response import GetDefaultStorageQuotaResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_default_storage_quota()
        print("The response of DefaultApi->get_default_storage_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_default_storage_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDefaultStorageQuotaResponse**](GetDefaultStorageQuotaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**
> GetMetricsResponse get_metrics()



Scrape system metrics.

### Example


```python
import openapi_client
from openapi_client.models.get_metrics_response import GetMetricsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.get_user_response import GetUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.

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
import openapi_client
from openapi_client.models.get_user_response import GetUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.get_user_list_response import GetUserListResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.list_buckets_response import ListBucketsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.list_objects_response import ListObjectsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.object_metadata_response import ObjectMetadataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
import openapi_client
from openapi_client.models.user_management_request import UserManagementRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_address = 'NSqa4SBqn1h8KTkyVbTSASi3eaHCbEumLv.' # str | Account's address.
    user = 'mike, admin or any users name.' # str | User name.
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

# **set_default_storage_quota**
> set_default_storage_quota(x_morph_address, x_morph_payload_signature, set_default_storage_quota_request=set_default_storage_quota_request)



Set default storage quota for user.

### Example


```python
import openapi_client
from openapi_client.models.set_default_storage_quota_request import SetDefaultStorageQuotaRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_address = 'NSqa4SBqn1h8KTkyVbTSASi3eaHCbEumLv.' # str | Account's address.
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS.
    set_default_storage_quota_request = openapi_client.SetDefaultStorageQuotaRequest() # SetDefaultStorageQuotaRequest |  (optional)

    try:
        api_instance.set_default_storage_quota(x_morph_address, x_morph_payload_signature, set_default_storage_quota_request=set_default_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_default_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_address** | **str**| Account&#39;s address. | 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | 
 **set_default_storage_quota_request** | [**SetDefaultStorageQuotaRequest**](SetDefaultStorageQuotaRequest.md)|  | [optional] 

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
**200** | Quota changed. |  -  |
**400** | Passed data is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_eacl**
> set_eacl(bucket, x_morph_public_key=x_morph_public_key, x_morph_payload=x_morph_payload, x_morph_payload_signature=x_morph_payload_signature, set_eacl_request=set_eacl_request)



Set EACL to the bucket.

### Example


```python
import openapi_client
from openapi_client.models.set_eacl_request import SetEaclRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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

# **set_storage_quota**
> set_storage_quota(x_morph_address, x_morph_payload_signature, user, user_change_storage_quota_request=user_change_storage_quota_request)



Change user storage quota.

### Example


```python
import openapi_client
from openapi_client.models.user_change_storage_quota_request import UserChangeStorageQuotaRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_address = 'NSqa4SBqn1h8KTkyVbTSASi3eaHCbEumLv.' # str | Account's address.
    x_morph_payload_signature = 'x_morph_payload_signature_example' # str | Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS.
    user = 'mike, admin or any users name.' # str | User name.
    user_change_storage_quota_request = openapi_client.UserChangeStorageQuotaRequest() # UserChangeStorageQuotaRequest |  (optional)

    try:
        api_instance.set_storage_quota(x_morph_address, x_morph_payload_signature, user, user_change_storage_quota_request=user_change_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_address** | **str**| Account&#39;s address. | 
 **x_morph_payload_signature** | **str**| Payload signature in base64. If passed, x-morph-payload will be used to execute request in NeoFS. | 
 **user** | **str**| User name. | 
 **user_change_storage_quota_request** | [**UserChangeStorageQuotaRequest**](UserChangeStorageQuotaRequest.md)|  | [optional] 

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
**201** | User quota successfully changed. |  -  |
**400** | Passed data is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_session**
> StoreSessionResponse store_session(x_morph_public_key, signed_session_token=signed_session_token)



Exchange object operations session tokens for a unified one. It will be used instead of them in object operations.

### Example


```python
import openapi_client
from openapi_client.models.signed_session_token import SignedSessionToken
from openapi_client.models.store_session_response import StoreSessionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
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
> top_up_storage_node(storage_node_address=storage_node_address)



Top up storage node account with minimal deposit to pay network candidate fee.

### Example


```python
import openapi_client
from openapi_client.models.storage_node_address import StorageNodeAddress
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    storage_node_address = openapi_client.StorageNodeAddress() # StorageNodeAddress |  (optional)

    try:
        api_instance.top_up_storage_node(storage_node_address=storage_node_address)
    except Exception as e:
        print("Exception when calling DefaultApi->top_up_storage_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_node_address** | [**StorageNodeAddress**](StorageNodeAddress.md)|  | [optional] 

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

# **v1_apply_sn_action**
> v1_apply_sn_action(x_morph_session_token, x_morph_action, storage_node_address=storage_node_address)



Apply one of the actions on the Storage Node. See available actions in the parameters.

### Example


```python
import openapi_client
from openapi_client.models.storage_node_address import StorageNodeAddress
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    x_morph_action = 'grant-access' # str | An action to apply to the storage node. The only available action for now is \"grant-access\", which grants access for a storage node to become a network candidate.
    storage_node_address = openapi_client.StorageNodeAddress() # StorageNodeAddress |  (optional)

    try:
        api_instance.v1_apply_sn_action(x_morph_session_token, x_morph_action, storage_node_address=storage_node_address)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_apply_sn_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 
 **x_morph_action** | **str**| An action to apply to the storage node. The only available action for now is \&quot;grant-access\&quot;, which grants access for a storage node to become a network candidate. | 
 **storage_node_address** | [**StorageNodeAddress**](StorageNodeAddress.md)|  | [optional] 

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
**200** | Action successfully performed. |  -  |
**400** | Address is empty. |  -  |
**403** | Insufficient rights. |  -  |
**500** | Unable to perform requested action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_bucket**
> v1_create_bucket(x_morph_session_token, create_bucket_request=create_bucket_request)



Create a new bucket.

### Example


```python
import openapi_client
from openapi_client.models.create_bucket_request import CreateBucketRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    create_bucket_request = openapi_client.CreateBucketRequest() # CreateBucketRequest | Parameters of the new bucket in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_create_bucket(x_morph_session_token, create_bucket_request=create_bucket_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 
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
**409** | Bucket already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_object**
> v1_create_object(bucket, x_morph_session_token, name, data, lifetime=lifetime)



Create a new object in the bucket.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    name = 'name_example' # str | Object name.
    data = None # bytearray | 
    lifetime = 56 # int | Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. (optional)

    try:
        api_instance.v1_create_object(bucket, x_morph_session_token, name, data, lifetime=lifetime)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Session token. | 
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

# **v1_delete_bucket**
> v1_delete_bucket(bucket, x_morph_session_token)



Delete bucket from the system.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_instance.v1_delete_bucket(bucket, x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Session token. | 

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
**404** | Bucket not found (not created or already removed). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_object**
> v1_delete_object(bucket, object, x_morph_session_token)



Delete object from the bucket.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'object_example' # str | Object name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_instance.v1_delete_object(bucket, object, x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name. | 
 **x_morph_session_token** | **str**| Session token. | 

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

# **v1_delete_user**
> v1_delete_user(user, x_morph_session_token)



Delete a user.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_instance.v1_delete_user(user, x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Session token. | 

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
**200** | User successfully deleted. |  -  |
**400** | Passed user name is invalid. |  -  |
**403** | Insufficient rights to execute request. |  -  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_download_object**
> bytearray v1_download_object(bucket, object, x_morph_session_token=x_morph_session_token)



Download the object data.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'object_example' # str | Object name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token. (optional)

    try:
        api_response = api_instance.v1_download_object(bucket, object, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_download_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_download_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name. | 
 **x_morph_session_token** | **str**| Session token. | [optional] 

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

# **v1_get_bucket**
> GetBucketResponse v1_get_bucket(bucket)



Get information about the bucket by name.

### Example


```python
import openapi_client
from openapi_client.models.get_bucket_response import GetBucketResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.

    try:
        api_response = api_instance.v1_get_bucket(bucket)
        print("The response of DefaultApi->v1_get_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_bucket: %s\n" % e)
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

# **v1_get_default_storage_quota**
> GetDefaultStorageQuotaResponse v1_get_default_storage_quota()



Get default storage quota for a new user.

### Example


```python
import openapi_client
from openapi_client.models.get_default_storage_quota_response import GetDefaultStorageQuotaResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_get_default_storage_quota()
        print("The response of DefaultApi->v1_get_default_storage_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_default_storage_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDefaultStorageQuotaResponse**](GetDefaultStorageQuotaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_metrics**
> GetMetricsResponse v1_get_metrics(x_morph_session_token)



Scrape system metrics.

### Example


```python
import openapi_client
from openapi_client.models.get_metrics_response import GetMetricsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_response = api_instance.v1_get_metrics(x_morph_session_token)
        print("The response of DefaultApi->v1_get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 

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
**403** | Insufficient rights to execute request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user**
> V1GetUserResponse v1_get_user(user)



Get user meta.

### Example


```python
import openapi_client
from openapi_client.models.v1_get_user_response import V1GetUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.

    try:
        api_response = api_instance.v1_get_user(user)
        print("The response of DefaultApi->v1_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 

### Return type

[**V1GetUserResponse**](V1GetUserResponse.md)

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

# **v1_get_user_list**
> GetUserListResponse v1_get_user_list(x_morph_session_token)



Get user list.

### Example


```python
import openapi_client
from openapi_client.models.get_user_list_response import GetUserListResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_response = api_instance.v1_get_user_list(x_morph_session_token)
        print("The response of DefaultApi->v1_get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 

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
**403** | Insufficient rights to execute request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_initial_registration**
> v1_initial_registration(v1_initial_registration_request=v1_initial_registration_request)



Register the first administrator account in the system.

### Example


```python
import openapi_client
from openapi_client.models.v1_initial_registration_request import V1InitialRegistrationRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    v1_initial_registration_request = openapi_client.V1InitialRegistrationRequest() # V1InitialRegistrationRequest |  (optional)

    try:
        api_instance.v1_initial_registration(v1_initial_registration_request=v1_initial_registration_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_initial_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_initial_registration_request** | [**V1InitialRegistrationRequest**](V1InitialRegistrationRequest.md)|  | [optional] 

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
**201** | Registration completed. |  -  |
**400** | Passed data is invalid. |  -  |
**403** | Already registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_buckets**
> ListBucketsResponse v1_list_buckets(x_morph_session_token)



List all user's buckets.

### Example


```python
import openapi_client
from openapi_client.models.list_buckets_response import ListBucketsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_response = api_instance.v1_list_buckets(x_morph_session_token)
        print("The response of DefaultApi->v1_list_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 

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
**400** | Session token is omitted or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_objects**
> ListObjectsResponse v1_list_objects(bucket, x_morph_session_token)



List all objects in the bucket with brief metadata.

### Example


```python
import openapi_client
from openapi_client.models.list_objects_response import ListObjectsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_response = api_instance.v1_list_objects(bucket, x_morph_session_token)
        print("The response of DefaultApi->v1_list_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Session token. | 

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

# **v1_login**
> V1LoginResponse v1_login(v1_login_request=v1_login_request)



Login via username and password.

### Example


```python
import openapi_client
from openapi_client.models.v1_login_request import V1LoginRequest
from openapi_client.models.v1_login_response import V1LoginResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    v1_login_request = openapi_client.V1LoginRequest() # V1LoginRequest |  (optional)

    try:
        api_response = api_instance.v1_login(v1_login_request=v1_login_request)
        print("The response of DefaultApi->v1_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_login_request** | [**V1LoginRequest**](V1LoginRequest.md)|  | [optional] 

### Return type

[**V1LoginResponse**](V1LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |
**400** | Passed data is invalid. |  -  |
**403** | User not found or wrong password. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_object_metadata**
> ObjectMetadataResponse v1_object_metadata(bucket, object, x_morph_session_token)



Get the object metadata.

### Example


```python
import openapi_client
from openapi_client.models.object_metadata_response import ObjectMetadataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'object_example' # str | Object name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_response = api_instance.v1_object_metadata(bucket, object, x_morph_session_token)
        print("The response of DefaultApi->v1_object_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_object_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name. | 
 **x_morph_session_token** | **str**| Session token. | 

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

# **v1_register_user**
> v1_register_user(x_morph_session_token, user, v1_register_user_request=v1_register_user_request)



Register new user.

### Example


```python
import openapi_client
from openapi_client.models.v1_register_user_request import V1RegisterUserRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    user = 'mike, admin or any users name.' # str | User name.
    v1_register_user_request = openapi_client.V1RegisterUserRequest() # V1RegisterUserRequest |  (optional)

    try:
        api_instance.v1_register_user(x_morph_session_token, user, v1_register_user_request=v1_register_user_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 
 **user** | **str**| User name. | 
 **v1_register_user_request** | [**V1RegisterUserRequest**](V1RegisterUserRequest.md)|  | [optional] 

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
**400** | Passed account data is invalid. |  -  |
**403** | Insufficient rights to execute request. |  -  |
**409** | User with this name already registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_s3_get_access_token**
> S3GetAccessTokenResponse v1_s3_get_access_token(x_morph_session_token)



Generate s3 access tokens.

### Example


```python
import openapi_client
from openapi_client.models.s3_get_access_token_response import S3GetAccessTokenResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.

    try:
        api_response = api_instance.v1_s3_get_access_token(x_morph_session_token)
        print("The response of DefaultApi->v1_s3_get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_get_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 

### Return type

[**S3GetAccessTokenResponse**](S3GetAccessTokenResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_default_storage_quota**
> v1_set_default_storage_quota(x_morph_session_token, set_default_storage_quota_request=set_default_storage_quota_request)



Set default storage quota for a new user.

### Example


```python
import openapi_client
from openapi_client.models.set_default_storage_quota_request import SetDefaultStorageQuotaRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    set_default_storage_quota_request = openapi_client.SetDefaultStorageQuotaRequest() # SetDefaultStorageQuotaRequest |  (optional)

    try:
        api_instance.v1_set_default_storage_quota(x_morph_session_token, set_default_storage_quota_request=set_default_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_default_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 
 **set_default_storage_quota_request** | [**SetDefaultStorageQuotaRequest**](SetDefaultStorageQuotaRequest.md)|  | [optional] 

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
**200** | Quota changed. |  -  |
**400** | Passed data is invalid. |  -  |
**403** | Insufficient rights to execute request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_eacl**
> v1_set_eacl(bucket, x_morph_session_token, set_eacl_request=set_eacl_request)



Set EACL to the bucket.

### Example


```python
import openapi_client
from openapi_client.models.set_eacl_request import SetEaclRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    set_eacl_request = openapi_client.SetEaclRequest() # SetEaclRequest | Parameters of the new EACL in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_set_eacl(bucket, x_morph_session_token, set_eacl_request=set_eacl_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_eacl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Session token. | 
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
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_user_storage_quota**
> v1_set_user_storage_quota(x_morph_session_token, user, user_change_storage_quota_request=user_change_storage_quota_request)



Change user storage quota.

### Example


```python
import openapi_client
from openapi_client.models.user_change_storage_quota_request import UserChangeStorageQuotaRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    user = 'mike, admin or any users name.' # str | User name.
    user_change_storage_quota_request = openapi_client.UserChangeStorageQuotaRequest() # UserChangeStorageQuotaRequest |  (optional)

    try:
        api_instance.v1_set_user_storage_quota(x_morph_session_token, user, user_change_storage_quota_request=user_change_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_user_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 
 **user** | **str**| User name. | 
 **user_change_storage_quota_request** | [**UserChangeStorageQuotaRequest**](UserChangeStorageQuotaRequest.md)|  | [optional] 

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
**201** | User quota successfully changed. |  -  |
**400** | Passed data is invalid. |  -  |
**403** | Insufficient rights to execute request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user**
> v1_update_user(x_morph_session_token, user, v1_update_user_request=v1_update_user_request)



Update existing user.

### Example


```python
import openapi_client
from openapi_client.models.v1_update_user_request import V1UpdateUserRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Session token.
    user = 'mike, admin or any users name.' # str | User name.
    v1_update_user_request = openapi_client.V1UpdateUserRequest() # V1UpdateUserRequest |  (optional)

    try:
        api_instance.v1_update_user(x_morph_session_token, user, v1_update_user_request=v1_update_user_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Session token. | 
 **user** | **str**| User name. | 
 **v1_update_user_request** | [**V1UpdateUserRequest**](V1UpdateUserRequest.md)|  | [optional] 

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
**201** | User successfully updated. |  -  |
**400** | Passed account data is invalid. |  -  |
**403** | Insufficient rights to execute request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

