# openapi_client.DefaultApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_apply_sn_action**](DefaultApi.md#v1_apply_sn_action) | **POST** /v1/cluster/storage-node | 
[**v1_create_bucket**](DefaultApi.md#v1_create_bucket) | **POST** /v1/buckets | 
[**v1_create_object**](DefaultApi.md#v1_create_object) | **POST** /v1/buckets/{bucket}/objects | 
[**v1_create_system_storage_policy**](DefaultApi.md#v1_create_system_storage_policy) | **POST** /v1/cluster/storage-policies | 
[**v1_create_user_storage_policy**](DefaultApi.md#v1_create_user_storage_policy) | **POST** /v1/users/{user}/storage-policies | 
[**v1_delete_bucket**](DefaultApi.md#v1_delete_bucket) | **DELETE** /v1/buckets/{bucket} | 
[**v1_delete_object**](DefaultApi.md#v1_delete_object) | **DELETE** /v1/buckets/{bucket}/objects/{object} | 
[**v1_delete_system_storage_policy**](DefaultApi.md#v1_delete_system_storage_policy) | **DELETE** /v1/cluster/storage-policies/{policyName} | 
[**v1_delete_user**](DefaultApi.md#v1_delete_user) | **DELETE** /v1/users/{user} | 
[**v1_delete_user_storage_policy**](DefaultApi.md#v1_delete_user_storage_policy) | **DELETE** /v1/users/{user}/storage-policies/{policyName} | 
[**v1_download_object**](DefaultApi.md#v1_download_object) | **GET** /v1/buckets/{bucket}/objects/{object} | 
[**v1_get_bucket**](DefaultApi.md#v1_get_bucket) | **GET** /v1/buckets/{bucket} | 
[**v1_get_default_storage_quota**](DefaultApi.md#v1_get_default_storage_quota) | **GET** /v1/cluster/default-quota | 
[**v1_get_eacl**](DefaultApi.md#v1_get_eacl) | **GET** /v1/buckets/{bucket}/eacl | 
[**v1_get_metrics**](DefaultApi.md#v1_get_metrics) | **GET** /v1/cluster/metrics | 
[**v1_get_system_storage_policies**](DefaultApi.md#v1_get_system_storage_policies) | **GET** /v1/cluster/storage-policies | 
[**v1_get_system_storage_policy**](DefaultApi.md#v1_get_system_storage_policy) | **GET** /v1/cluster/storage-policies/{policyName} | 
[**v1_get_user**](DefaultApi.md#v1_get_user) | **GET** /v1/users/{user} | 
[**v1_get_user_list**](DefaultApi.md#v1_get_user_list) | **GET** /v1/users | 
[**v1_get_user_storage_policies**](DefaultApi.md#v1_get_user_storage_policies) | **GET** /v1/users/{user}/storage-policies | 
[**v1_get_user_storage_policy**](DefaultApi.md#v1_get_user_storage_policy) | **GET** /v1/users/{user}/storage-policies/{policyName} | 
[**v1_list_buckets**](DefaultApi.md#v1_list_buckets) | **GET** /v1/buckets | 
[**v1_list_objects**](DefaultApi.md#v1_list_objects) | **GET** /v1/buckets/{bucket}/objects | 
[**v1_login**](DefaultApi.md#v1_login) | **POST** /v1/login | 
[**v1_object_metadata**](DefaultApi.md#v1_object_metadata) | **GET** /v1/buckets/{bucket}/objects/{object}/metadata | 
[**v1_register_user**](DefaultApi.md#v1_register_user) | **POST** /v1/users/{user} | 
[**v1_s3_create_access_token**](DefaultApi.md#v1_s3_create_access_token) | **POST** /v1/users/{user}/s3-tokens | 
[**v1_s3_get_access_tokens**](DefaultApi.md#v1_s3_get_access_tokens) | **GET** /v1/users/{user}/s3-tokens | 
[**v1_s3_get_token_details**](DefaultApi.md#v1_s3_get_token_details) | **GET** /v1/users/{user}/s3-tokens/{token} | 
[**v1_s3_revoke_token**](DefaultApi.md#v1_s3_revoke_token) | **DELETE** /v1/users/{user}/s3-tokens/{token} | 
[**v1_set_default_storage_quota**](DefaultApi.md#v1_set_default_storage_quota) | **POST** /v1/cluster/default-quota | 
[**v1_set_eacl**](DefaultApi.md#v1_set_eacl) | **PUT** /v1/buckets/{bucket}/eacl | 
[**v1_set_eacl_deprecated**](DefaultApi.md#v1_set_eacl_deprecated) | **POST** /v1/buckets/{bucket}/eacl | 
[**v1_set_user_storage_quota**](DefaultApi.md#v1_set_user_storage_quota) | **POST** /v1/users/{user}/quota | 
[**v1_update_system_storage_policy**](DefaultApi.md#v1_update_system_storage_policy) | **PUT** /v1/cluster/storage-policies/{policyName} | 
[**v1_update_user**](DefaultApi.md#v1_update_user) | **PUT** /v1/users/{user} | 
[**v1_update_user_storage_policy**](DefaultApi.md#v1_update_user_storage_policy) | **PUT** /v1/users/{user}/storage-policies/{policyName} | 


# **v1_apply_sn_action**
> v1_apply_sn_action(x_morph_action, x_morph_session_token=x_morph_session_token, storage_node_address=storage_node_address)



Apply one of the actions on the Storage Node. See available actions in the parameters.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_action = 'grant-access' # str | An action to apply to the storage node. The only available action for now is \"grant-access\", which grants access for a storage node to become a network candidate.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    storage_node_address = openapi_client.StorageNodeAddress() # StorageNodeAddress |  (optional)

    try:
        api_instance.v1_apply_sn_action(x_morph_action, x_morph_session_token=x_morph_session_token, storage_node_address=storage_node_address)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_apply_sn_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_action** | **str**| An action to apply to the storage node. The only available action for now is \&quot;grant-access\&quot;, which grants access for a storage node to become a network candidate. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **storage_node_address** | [**StorageNodeAddress**](StorageNodeAddress.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action successfully performed. |  -  |
**400** | Address is empty. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights. |  * WWW-Authenticate -  <br>  |
**500** | Unable to perform requested action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_bucket**
> v1_create_bucket(x_morph_session_token=x_morph_session_token, create_bucket_request=create_bucket_request)



Create a new bucket.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    create_bucket_request = openapi_client.CreateBucketRequest() # CreateBucketRequest | Parameters of the new bucket in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_create_bucket(x_morph_session_token=x_morph_session_token, create_bucket_request=create_bucket_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **create_bucket_request** | [**CreateBucketRequest**](CreateBucketRequest.md)| Parameters of the new bucket in JSON. Required only for payload generation request. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bucket successfully created. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | Bucket already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_object**
> CreateObjectResponse v1_create_object(bucket, name, data, x_morph_session_token=x_morph_session_token, lifetime=lifetime)



Create a new object in the bucket.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_object_response import CreateObjectResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    name = 'name_example' # str | Object name.
    data = None # bytearray | 
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    lifetime = 56 # int | Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. (optional)

    try:
        api_response = api_instance.v1_create_object(bucket, name, data, x_morph_session_token=x_morph_session_token, lifetime=lifetime)
        print("The response of DefaultApi->v1_create_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **name** | **str**| Object name. | 
 **data** | **bytearray**|  | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **lifetime** | **int**| Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. | [optional] 

### Return type

[**CreateObjectResponse**](CreateObjectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Object successfully created. |  -  |
**400** | At least one object parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**409** | Object already exists. |  -  |
**507** | User doesn&#39;t have enough space. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_system_storage_policy**
> v1_create_system_storage_policy(x_morph_session_token=x_morph_session_token, v1_create_system_storage_policy_request=v1_create_system_storage_policy_request)



Create storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_create_system_storage_policy_request import V1CreateSystemStoragePolicyRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_create_system_storage_policy_request = openapi_client.V1CreateSystemStoragePolicyRequest() # V1CreateSystemStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_create_system_storage_policy(x_morph_session_token=x_morph_session_token, v1_create_system_storage_policy_request=v1_create_system_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_create_system_storage_policy_request** | [**V1CreateSystemStoragePolicyRequest**](V1CreateSystemStoragePolicyRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Storage policy created. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_user_storage_policy**
> v1_create_user_storage_policy(user, x_morph_session_token=x_morph_session_token, v1_create_user_storage_policy_request=v1_create_user_storage_policy_request)



Create storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_create_user_storage_policy_request import V1CreateUserStoragePolicyRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_create_user_storage_policy_request = openapi_client.V1CreateUserStoragePolicyRequest() # V1CreateUserStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_create_user_storage_policy(user, x_morph_session_token=x_morph_session_token, v1_create_user_storage_policy_request=v1_create_user_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_create_user_storage_policy_request** | [**V1CreateUserStoragePolicyRequest**](V1CreateUserStoragePolicyRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Storage policy created. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_bucket**
> v1_delete_bucket(bucket, x_morph_session_token=x_morph_session_token)



Delete bucket from the system.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_instance.v1_delete_bucket(bucket, x_morph_session_token=x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Bucket successfully removed. |  -  |
**400** | Session token is omitted or invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found (not created or already removed). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_object**
> v1_delete_object(bucket, object, x_morph_session_token=x_morph_session_token)



Delete object from the bucket.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'file.txt' # str | Object name or object id.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_instance.v1_delete_object(bucket, object, x_morph_session_token=x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name or object id. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Object successfully removed. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket or object not found (not created or already removed). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_system_storage_policy**
> v1_delete_system_storage_policy(policy_name, x_morph_session_token=x_morph_session_token)



Delete system storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    policy_name = 'policy1, policy2, superPolicy.' # str | Storage policy name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_instance.v1_delete_system_storage_policy(policy_name, x_morph_session_token=x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Storage policy deleted. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Policy not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_user**
> v1_delete_user(user, x_morph_session_token=x_morph_session_token)



Delete a user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_instance.v1_delete_user(user, x_morph_session_token=x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User successfully deleted. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_user_storage_policy**
> v1_delete_user_storage_policy(user, policy_name, x_morph_session_token=x_morph_session_token)



Delete storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    policy_name = 'policy1, policy2, superPolicy.' # str | Storage policy name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_instance.v1_delete_user_storage_policy(user, policy_name, x_morph_session_token=x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Storage policy deleted. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Storage policy not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_download_object**
> bytearray v1_download_object(bucket, object, x_morph_session_token=x_morph_session_token)



Download the object data.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'file.txt' # str | Object name or object id.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

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
 **object** | **str**| Object name or object id. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket or object not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_bucket**
> GetBucketResponse v1_get_bucket(bucket, x_morph_session_token=x_morph_session_token)



Get information about the bucket by name.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_get_bucket(bucket, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_get_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**GetBucketResponse**](GetBucketResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bucket reference is missing or invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to get bucket info. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_default_storage_quota**
> GetDefaultStorageQuotaResponse v1_get_default_storage_quota()



Get default storage quota for a new user.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_eacl**
> GetEaclResponse v1_get_eacl(bucket, x_morph_session_token=x_morph_session_token)



Get bucket EACL.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_eacl_response import GetEaclResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_get_eacl(bucket, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_get_eacl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_eacl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**GetEaclResponse**](GetEaclResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_metrics**
> GetMetricsResponse v1_get_metrics(x_morph_session_token=x_morph_session_token)



Scrape system metrics.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_get_metrics(x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**GetMetricsResponse**](GetMetricsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_system_storage_policies**
> V1GetSystemStoragePoliciesResponse v1_get_system_storage_policies()



Get system storage policies.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_get_system_storage_policies_response import V1GetSystemStoragePoliciesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_get_system_storage_policies()
        print("The response of DefaultApi->v1_get_system_storage_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_system_storage_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1GetSystemStoragePoliciesResponse**](V1GetSystemStoragePoliciesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage policies found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_system_storage_policy**
> V1GetSystemStoragePolicyResponse v1_get_system_storage_policy(policy_name)



Get system storage policy by name.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_get_system_storage_policy_response import V1GetSystemStoragePolicyResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    policy_name = 'policy1, policy2, superPolicy.' # str | Storage policy name.

    try:
        api_response = api_instance.v1_get_system_storage_policy(policy_name)
        print("The response of DefaultApi->v1_get_system_storage_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Storage policy name. | 

### Return type

[**V1GetSystemStoragePolicyResponse**](V1GetSystemStoragePolicyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage policy found. |  -  |
**404** | Policy not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user**
> V1GetUserResponse v1_get_user(user)



Get user meta.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User found. |  -  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user_list**
> GetUserListResponse v1_get_user_list(x_morph_session_token=x_morph_session_token)



Get user list.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_get_user_list(x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**GetUserListResponse**](GetUserListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full list of users in system. |  -  |
**400** | Session token required because system contains users. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user_storage_policies**
> V1GetUserStoragePoliciesResponse v1_get_user_storage_policies(user, x_morph_session_token=x_morph_session_token)



Get user storage policies.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_get_user_storage_policies_response import V1GetUserStoragePoliciesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_get_user_storage_policies(user, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_get_user_storage_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_storage_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**V1GetUserStoragePoliciesResponse**](V1GetUserStoragePoliciesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage policies found. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user_storage_policy**
> V1GetUserStoragePolicyResponse v1_get_user_storage_policy(user, policy_name, x_morph_session_token=x_morph_session_token)



Get storage policy by name.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_get_user_storage_policy_response import V1GetUserStoragePolicyResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    policy_name = 'policy1, policy2, superPolicy.' # str | Storage policy name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_get_user_storage_policy(user, policy_name, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_get_user_storage_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**V1GetUserStoragePolicyResponse**](V1GetUserStoragePolicyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage policy found. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Policy not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_buckets**
> ListBucketsResponse v1_list_buckets(user, x_morph_session_token=x_morph_session_token, cursor=cursor, max_items=max_items)



List all user's buckets. Default items amount in response is 100.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'user_example' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    cursor = 'cursor_example' # str | ID to start the next batch from. It returns the first elements batch if empty value passed. You should take `cursor` value from previous response to be able to list items. (optional)
    max_items = 100 # int | Limits amount of items in response. (optional) (default to 100)

    try:
        api_response = api_instance.v1_list_buckets(user, x_morph_session_token=x_morph_session_token, cursor=cursor, max_items=max_items)
        print("The response of DefaultApi->v1_list_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **cursor** | **str**| ID to start the next batch from. It returns the first elements batch if empty value passed. You should take &#x60;cursor&#x60; value from previous response to be able to list items. | [optional] 
 **max_items** | **int**| Limits amount of items in response. | [optional] [default to 100]

### Return type

[**ListBucketsResponse**](ListBucketsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Session token is omitted or invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_objects**
> ListObjectsResponse v1_list_objects(bucket, x_morph_session_token=x_morph_session_token)



List all objects in the bucket with brief metadata.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_list_objects(bucket, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_list_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**ListObjectsResponse**](ListObjectsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_login**
> V1LoginResponse v1_login(v1_login_request=v1_login_request)



Login via username and password.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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

[BearerAuth](../README.md#BearerAuth)

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
> ObjectMetadataResponse v1_object_metadata(bucket, object, x_morph_session_token=x_morph_session_token)



Get the object metadata.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    object = 'file.txt' # str | Object name or object id.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_object_metadata(bucket, object, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_object_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_object_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name or object id. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**ObjectMetadataResponse**](ObjectMetadataResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket or object not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_register_user**
> v1_register_user(user, x_morph_session_token=x_morph_session_token, v1_register_user_request=v1_register_user_request)



Register new user. This method should be used to register the first admin as well. In case of the first admin session token is not required.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_register_user_request = openapi_client.V1RegisterUserRequest() # V1RegisterUserRequest |  (optional)

    try:
        api_instance.v1_register_user(user, x_morph_session_token=x_morph_session_token, v1_register_user_request=v1_register_user_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_register_user_request** | [**V1RegisterUserRequest**](V1RegisterUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User successfully registered. |  -  |
**400** | Passed account data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | User with this name already registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_s3_create_access_token**
> S3CreateAccessTokenResponse v1_s3_create_access_token(user, x_morph_session_token=x_morph_session_token, v1_s3_create_access_token_request=v1_s3_create_access_token_request)



Generate s3 access tokens.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.s3_create_access_token_response import S3CreateAccessTokenResponse
from openapi_client.models.v1_s3_create_access_token_request import V1S3CreateAccessTokenRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_s3_create_access_token_request = openapi_client.V1S3CreateAccessTokenRequest() # V1S3CreateAccessTokenRequest |  (optional)

    try:
        api_response = api_instance.v1_s3_create_access_token(user, x_morph_session_token=x_morph_session_token, v1_s3_create_access_token_request=v1_s3_create_access_token_request)
        print("The response of DefaultApi->v1_s3_create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_s3_create_access_token_request** | [**V1S3CreateAccessTokenRequest**](V1S3CreateAccessTokenRequest.md)|  | [optional] 

### Return type

[**S3CreateAccessTokenResponse**](S3CreateAccessTokenResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_s3_get_access_tokens**
> S3GetAccessTokensResponse v1_s3_get_access_tokens(user, x_morph_session_token=x_morph_session_token)



Get user s3 access tokens.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.s3_get_access_tokens_response import S3GetAccessTokensResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_s3_get_access_tokens(user, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_s3_get_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_get_access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**S3GetAccessTokensResponse**](S3GetAccessTokensResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_s3_get_token_details**
> S3GetAccessTokenDetailsResponse v1_s3_get_token_details(user, token, x_morph_session_token=x_morph_session_token)



Get s3 token details.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.s3_get_access_token_details_response import S3GetAccessTokenDetailsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    token = 'token_example' # str | S3 token id.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_response = api_instance.v1_s3_get_token_details(user, token, x_morph_session_token=x_morph_session_token)
        print("The response of DefaultApi->v1_s3_get_token_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_get_token_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **token** | **str**| S3 token id. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

[**S3GetAccessTokenDetailsResponse**](S3GetAccessTokenDetailsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Token not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_s3_revoke_token**
> v1_s3_revoke_token(user, token, x_morph_session_token=x_morph_session_token)



Revoke s3 token.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    token = 'token_example' # str | S3 token id.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)

    try:
        api_instance.v1_s3_revoke_token(user, token, x_morph_session_token=x_morph_session_token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_revoke_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **token** | **str**| S3 token id. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The token has been revoked. |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Token not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_default_storage_quota**
> v1_set_default_storage_quota(x_morph_session_token=x_morph_session_token, set_default_storage_quota_request=set_default_storage_quota_request)



Set default storage quota for a new user.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    set_default_storage_quota_request = openapi_client.SetDefaultStorageQuotaRequest() # SetDefaultStorageQuotaRequest |  (optional)

    try:
        api_instance.v1_set_default_storage_quota(x_morph_session_token=x_morph_session_token, set_default_storage_quota_request=set_default_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_default_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **set_default_storage_quota_request** | [**SetDefaultStorageQuotaRequest**](SetDefaultStorageQuotaRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quota changed. |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_eacl**
> v1_set_eacl(bucket, x_morph_session_token=x_morph_session_token, set_eacl_request=set_eacl_request)



Set EACL to the bucket.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    set_eacl_request = openapi_client.SetEaclRequest() # SetEaclRequest | Parameters of the new EACL in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_set_eacl(bucket, x_morph_session_token=x_morph_session_token, set_eacl_request=set_eacl_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_eacl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **set_eacl_request** | [**SetEaclRequest**](SetEaclRequest.md)| Parameters of the new EACL in JSON. Required only for payload generation request. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EACL successfully put. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_eacl_deprecated**
> v1_set_eacl_deprecated(bucket, x_morph_session_token=x_morph_session_token, set_eacl_request=set_eacl_request)



Set EACL to the bucket. This operation is deprecated. Use PUT request instead.\"

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Bucket name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    set_eacl_request = openapi_client.SetEaclRequest() # SetEaclRequest | Parameters of the new EACL in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_set_eacl_deprecated(bucket, x_morph_session_token=x_morph_session_token, set_eacl_request=set_eacl_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_eacl_deprecated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **set_eacl_request** | [**SetEaclRequest**](SetEaclRequest.md)| Parameters of the new EACL in JSON. Required only for payload generation request. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EACL successfully put. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_user_storage_quota**
> v1_set_user_storage_quota(user, x_morph_session_token=x_morph_session_token, user_change_storage_quota_request=user_change_storage_quota_request)



Change user storage quota.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    user_change_storage_quota_request = openapi_client.UserChangeStorageQuotaRequest() # UserChangeStorageQuotaRequest |  (optional)

    try:
        api_instance.v1_set_user_storage_quota(user, x_morph_session_token=x_morph_session_token, user_change_storage_quota_request=user_change_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_user_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **user_change_storage_quota_request** | [**UserChangeStorageQuotaRequest**](UserChangeStorageQuotaRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User quota successfully changed. |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_system_storage_policy**
> v1_update_system_storage_policy(policy_name, x_morph_session_token=x_morph_session_token, v1_update_system_storage_policy_request=v1_update_system_storage_policy_request)



Update system storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_update_system_storage_policy_request import V1UpdateSystemStoragePolicyRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    policy_name = 'policy1, policy2, superPolicy.' # str | Storage policy name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_update_system_storage_policy_request = openapi_client.V1UpdateSystemStoragePolicyRequest() # V1UpdateSystemStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_update_system_storage_policy(policy_name, x_morph_session_token=x_morph_session_token, v1_update_system_storage_policy_request=v1_update_system_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_update_system_storage_policy_request** | [**V1UpdateSystemStoragePolicyRequest**](V1UpdateSystemStoragePolicyRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage policy updated. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user**
> v1_update_user(user, x_morph_session_token=x_morph_session_token, v1_update_user_request=v1_update_user_request)



Update existing user.

### Example

* Bearer Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_update_user_request = openapi_client.V1UpdateUserRequest() # V1UpdateUserRequest |  (optional)

    try:
        api_instance.v1_update_user(user, x_morph_session_token=x_morph_session_token, v1_update_user_request=v1_update_user_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_update_user_request** | [**V1UpdateUserRequest**](V1UpdateUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully updated. |  -  |
**400** | Passed account data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user_storage_policy**
> v1_update_user_storage_policy(user, policy_name, x_morph_session_token=x_morph_session_token, v1_update_user_storage_policy_request=v1_update_user_storage_policy_request)



Update storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_update_user_storage_policy_request import V1UpdateUserStoragePolicyRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = 'mike, admin or any users name.' # str | User name.
    policy_name = 'policy1, policy2, superPolicy.' # str | Storage policy name.
    x_morph_session_token = 'x_morph_session_token_example' # str | Optional session token. (optional)
    v1_update_user_storage_policy_request = openapi_client.V1UpdateUserStoragePolicyRequest() # V1UpdateUserStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_update_user_storage_policy(user, policy_name, x_morph_session_token=x_morph_session_token, v1_update_user_storage_policy_request=v1_update_user_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_session_token** | **str**| Optional session token. | [optional] 
 **v1_update_user_storage_policy_request** | [**V1UpdateUserStoragePolicyRequest**](V1UpdateUserStoragePolicyRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage policy updated. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

