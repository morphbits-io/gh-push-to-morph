# openapi_client.DefaultApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_apply_bucket_transfer_action**](DefaultApi.md#v1_apply_bucket_transfer_action) | **POST** /v1/users/{user}/pending-transfers/{id} | 
[**v1_apply_sn_action**](DefaultApi.md#v1_apply_sn_action) | **POST** /v1/cluster/storage-node | 
[**v1_cluster_create_o_auth_provider**](DefaultApi.md#v1_cluster_create_o_auth_provider) | **POST** /v1/cluster/oauth | 
[**v1_cluster_create_saml_provider**](DefaultApi.md#v1_cluster_create_saml_provider) | **POST** /v1/cluster/saml | 
[**v1_cluster_delete_o_auth_provider**](DefaultApi.md#v1_cluster_delete_o_auth_provider) | **DELETE** /v1/cluster/oauth/{providerID} | 
[**v1_cluster_delete_saml_provider**](DefaultApi.md#v1_cluster_delete_saml_provider) | **DELETE** /v1/cluster/saml/{providerID} | 
[**v1_cluster_get_o_auth_provider**](DefaultApi.md#v1_cluster_get_o_auth_provider) | **GET** /v1/cluster/oauth/{providerID} | 
[**v1_cluster_get_o_auth_providers**](DefaultApi.md#v1_cluster_get_o_auth_providers) | **GET** /v1/cluster/oauth | 
[**v1_cluster_get_saml_provider**](DefaultApi.md#v1_cluster_get_saml_provider) | **GET** /v1/cluster/saml/{providerID} | 
[**v1_cluster_list_saml_providers**](DefaultApi.md#v1_cluster_list_saml_providers) | **GET** /v1/cluster/saml | 
[**v1_cluster_update_o_auth_provider**](DefaultApi.md#v1_cluster_update_o_auth_provider) | **PUT** /v1/cluster/oauth/{providerID} | 
[**v1_cluster_update_saml_provider**](DefaultApi.md#v1_cluster_update_saml_provider) | **PUT** /v1/cluster/saml/{providerID} | 
[**v1_create_bearer_token**](DefaultApi.md#v1_create_bearer_token) | **POST** /v1/users/{user}/tokens | 
[**v1_create_bucket**](DefaultApi.md#v1_create_bucket) | **POST** /v1/buckets | 
[**v1_create_bucket_transfer**](DefaultApi.md#v1_create_bucket_transfer) | **POST** /v1/buckets/{bucket}/transfer | 
[**v1_create_namespace**](DefaultApi.md#v1_create_namespace) | **POST** /v1/cluster/namespaces | 
[**v1_create_object**](DefaultApi.md#v1_create_object) | **POST** /v1/buckets/{bucket}/objects | 
[**v1_create_system_storage_policy**](DefaultApi.md#v1_create_system_storage_policy) | **POST** /v1/cluster/storage-policies | 
[**v1_create_user_storage_policy**](DefaultApi.md#v1_create_user_storage_policy) | **POST** /v1/users/{user}/storage-policies | 
[**v1_delete_bucket**](DefaultApi.md#v1_delete_bucket) | **DELETE** /v1/buckets/{bucket} | 
[**v1_delete_namespace**](DefaultApi.md#v1_delete_namespace) | **DELETE** /v1/cluster/namespaces/{namespace} | 
[**v1_delete_object**](DefaultApi.md#v1_delete_object) | **DELETE** /v1/buckets/{bucket}/objects/{object} | 
[**v1_delete_system_storage_policy**](DefaultApi.md#v1_delete_system_storage_policy) | **DELETE** /v1/cluster/storage-policies/{policyName} | 
[**v1_delete_user**](DefaultApi.md#v1_delete_user) | **DELETE** /v1/users/{user} | 
[**v1_delete_user_storage_policy**](DefaultApi.md#v1_delete_user_storage_policy) | **DELETE** /v1/users/{user}/storage-policies/{policyName} | 
[**v1_download_object**](DefaultApi.md#v1_download_object) | **GET** /v1/buckets/{bucket}/objects/{object} | 
[**v1_get_bearer_token_details**](DefaultApi.md#v1_get_bearer_token_details) | **GET** /v1/users/{user}/tokens/{token} | 
[**v1_get_bearer_tokens**](DefaultApi.md#v1_get_bearer_tokens) | **GET** /v1/users/{user}/tokens | 
[**v1_get_bucket**](DefaultApi.md#v1_get_bucket) | **GET** /v1/buckets/{bucket} | 
[**v1_get_bucket_quota**](DefaultApi.md#v1_get_bucket_quota) | **GET** /v1/buckets/{bucket}/quota | 
[**v1_get_bucket_timelock**](DefaultApi.md#v1_get_bucket_timelock) | **GET** /v1/buckets/{bucket}/timelock | 
[**v1_get_default_storage_quota**](DefaultApi.md#v1_get_default_storage_quota) | **GET** /v1/cluster/default-quota | 
[**v1_get_eacl**](DefaultApi.md#v1_get_eacl) | **GET** /v1/buckets/{bucket}/eacl | 
[**v1_get_ir_public_keys**](DefaultApi.md#v1_get_ir_public_keys) | **GET** /v1/cluster/ir-keys | 
[**v1_get_license**](DefaultApi.md#v1_get_license) | **GET** /v1/cluster/license | 
[**v1_get_metrics**](DefaultApi.md#v1_get_metrics) | **GET** /v1/cluster/metrics | 
[**v1_get_namespace**](DefaultApi.md#v1_get_namespace) | **GET** /v1/cluster/namespaces/{namespace} | 
[**v1_get_system_storage_policies**](DefaultApi.md#v1_get_system_storage_policies) | **GET** /v1/cluster/storage-policies | 
[**v1_get_system_storage_policy**](DefaultApi.md#v1_get_system_storage_policy) | **GET** /v1/cluster/storage-policies/{policyName} | 
[**v1_get_user**](DefaultApi.md#v1_get_user) | **GET** /v1/users/{user} | 
[**v1_get_user_list**](DefaultApi.md#v1_get_user_list) | **GET** /v1/users | 
[**v1_get_user_metrics**](DefaultApi.md#v1_get_user_metrics) | **GET** /v1/users/{user}/metrics | 
[**v1_get_user_storage_policies**](DefaultApi.md#v1_get_user_storage_policies) | **GET** /v1/users/{user}/storage-policies | 
[**v1_get_user_storage_policy**](DefaultApi.md#v1_get_user_storage_policy) | **GET** /v1/users/{user}/storage-policies/{policyName} | 
[**v1_head_object**](DefaultApi.md#v1_head_object) | **HEAD** /v1/buckets/{bucket}/objects/{object} | 
[**v1_list_bucket_transfers**](DefaultApi.md#v1_list_bucket_transfers) | **GET** /v1/users/{user}/pending-transfers | 
[**v1_list_buckets**](DefaultApi.md#v1_list_buckets) | **GET** /v1/buckets | 
[**v1_list_namespaces**](DefaultApi.md#v1_list_namespaces) | **GET** /v1/cluster/namespaces | 
[**v1_list_objects**](DefaultApi.md#v1_list_objects) | **GET** /v1/buckets/{bucket}/objects | 
[**v1_login**](DefaultApi.md#v1_login) | **POST** /v1/login | 
[**v1_o_auth_callback**](DefaultApi.md#v1_o_auth_callback) | **GET** /v1/oauth/callback | 
[**v1_o_auth_login**](DefaultApi.md#v1_o_auth_login) | **GET** /v1/oauth/{providerID}/login | 
[**v1_register_user**](DefaultApi.md#v1_register_user) | **POST** /v1/users/{user} | 
[**v1_revoke_bearer_token**](DefaultApi.md#v1_revoke_bearer_token) | **DELETE** /v1/users/{user}/tokens/{token} | 
[**v1_s3_create_access_token**](DefaultApi.md#v1_s3_create_access_token) | **POST** /v1/users/{user}/s3-tokens | 
[**v1_s3_get_access_tokens**](DefaultApi.md#v1_s3_get_access_tokens) | **GET** /v1/users/{user}/s3-tokens | 
[**v1_s3_get_token_details**](DefaultApi.md#v1_s3_get_token_details) | **GET** /v1/users/{user}/s3-tokens/{token} | 
[**v1_s3_revoke_token**](DefaultApi.md#v1_s3_revoke_token) | **DELETE** /v1/users/{user}/s3-tokens/{token} | 
[**v1_saml_acs**](DefaultApi.md#v1_saml_acs) | **POST** /v1/saml/{providerID}/acs | 
[**v1_saml_login**](DefaultApi.md#v1_saml_login) | **GET** /v1/saml/{providerID}/login | 
[**v1_saml_metadata**](DefaultApi.md#v1_saml_metadata) | **GET** /v1/saml/{providerID}/metadata | 
[**v1_search_objects**](DefaultApi.md#v1_search_objects) | **POST** /v1/buckets/{bucket}/objects/search | 
[**v1_set_bucket_quota**](DefaultApi.md#v1_set_bucket_quota) | **PUT** /v1/buckets/{bucket}/quota | 
[**v1_set_bucket_timelock**](DefaultApi.md#v1_set_bucket_timelock) | **PUT** /v1/buckets/{bucket}/timelock | 
[**v1_set_default_storage_quota**](DefaultApi.md#v1_set_default_storage_quota) | **POST** /v1/cluster/default-quota | 
[**v1_set_eacl**](DefaultApi.md#v1_set_eacl) | **PUT** /v1/buckets/{bucket}/eacl | 
[**v1_set_user_storage_quota**](DefaultApi.md#v1_set_user_storage_quota) | **POST** /v1/users/{user}/quota | 
[**v1_update_system_storage_policy**](DefaultApi.md#v1_update_system_storage_policy) | **PUT** /v1/cluster/storage-policies/{policyName} | 
[**v1_update_user**](DefaultApi.md#v1_update_user) | **PUT** /v1/users/{user} | 
[**v1_update_user_storage_policy**](DefaultApi.md#v1_update_user_storage_policy) | **PUT** /v1/users/{user}/storage-policies/{policyName} | 
[**v1_upload_license**](DefaultApi.md#v1_upload_license) | **POST** /v1/cluster/license | 


# **v1_apply_bucket_transfer_action**
> v1_apply_bucket_transfer_action(user, id, x_morph_transfer_action, x_morph_namespace=x_morph_namespace)

Apply some action to a pending bucket transfer request by ID.

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
    id = '2b5b6d2c-44b5-4b92-8a1f-3b8a03d69c2a' # str | Bucket transfer ID.
    x_morph_transfer_action = 'accept' # str | An action to apply to a bucket transfer. The only available action for now is \"accept\", which accepts the pending bucket transfer.
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_instance.v1_apply_bucket_transfer_action(user, id, x_morph_transfer_action, x_morph_namespace=x_morph_namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_apply_bucket_transfer_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **id** | **str**| Bucket transfer ID. | 
 **x_morph_transfer_action** | **str**| An action to apply to a bucket transfer. The only available action for now is \&quot;accept\&quot;, which accepts the pending bucket transfer. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
**204** | Action applied. |  -  |
**400** | Transfer reference is missing or invalid, or transaction is malformed. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to apply the action. |  * WWW-Authenticate -  <br>  |
**404** | Transfer not found. |  -  |
**409** | Action has already been applied or has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_apply_sn_action**
> v1_apply_sn_action(x_morph_action, storage_node_address=storage_node_address)

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
    storage_node_address = openapi_client.StorageNodeAddress() # StorageNodeAddress |  (optional)

    try:
        api_instance.v1_apply_sn_action(x_morph_action, storage_node_address=storage_node_address)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_apply_sn_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_action** | **str**| An action to apply to the storage node. The only available action for now is \&quot;grant-access\&quot;, which grants access for a storage node to become a network candidate. | 
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
**204** | Action successfully performed. |  -  |
**400** | Address is empty. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights. |  * WWW-Authenticate -  <br>  |
**500** | Unable to perform requested action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_create_o_auth_provider**
> v1_cluster_create_o_auth_provider(v1_cluster_create_o_auth_provider_request=v1_cluster_create_o_auth_provider_request)

Create a new provider.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_create_o_auth_provider_request import V1ClusterCreateOAuthProviderRequest
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
    v1_cluster_create_o_auth_provider_request = openapi_client.V1ClusterCreateOAuthProviderRequest() # V1ClusterCreateOAuthProviderRequest |  (optional)

    try:
        api_instance.v1_cluster_create_o_auth_provider(v1_cluster_create_o_auth_provider_request=v1_cluster_create_o_auth_provider_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_create_o_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_cluster_create_o_auth_provider_request** | [**V1ClusterCreateOAuthProviderRequest**](V1ClusterCreateOAuthProviderRequest.md)|  | [optional] 

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
**201** | OAuth provider created. |  * Location - URL of the created OAuth provider resource. <br>  |
**400** | Request is malformed or has invalid provider type. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_create_saml_provider**
> v1_cluster_create_saml_provider(v1_cluster_create_saml_provider_request=v1_cluster_create_saml_provider_request)

Create a new provider.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_create_saml_provider_request import V1ClusterCreateSAMLProviderRequest
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
    v1_cluster_create_saml_provider_request = openapi_client.V1ClusterCreateSAMLProviderRequest() # V1ClusterCreateSAMLProviderRequest |  (optional)

    try:
        api_instance.v1_cluster_create_saml_provider(v1_cluster_create_saml_provider_request=v1_cluster_create_saml_provider_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_create_saml_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_cluster_create_saml_provider_request** | [**V1ClusterCreateSAMLProviderRequest**](V1ClusterCreateSAMLProviderRequest.md)|  | [optional] 

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
**201** | Provider created. |  * Location - URL of the created SAML provider resource. <br>  |
**400** | Request is malformed. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | Provider with the same id already registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_delete_o_auth_provider**
> v1_cluster_delete_o_auth_provider(provider_id=provider_id)

Delete OAuth provider.

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
    provider_id = 'provider_id_example' # str | OAuth provider id. (optional)

    try:
        api_instance.v1_cluster_delete_o_auth_provider(provider_id=provider_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_delete_o_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| OAuth provider id. | [optional] 

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
**204** | OAuth provider deleted. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | OAuth provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_delete_saml_provider**
> v1_cluster_delete_saml_provider(provider_id=provider_id)

Delete provider.

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
    provider_id = 'provider_id_example' # str | SAML provider id. (optional)

    try:
        api_instance.v1_cluster_delete_saml_provider(provider_id=provider_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_delete_saml_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| SAML provider id. | [optional] 

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
**204** | Provider deleted. |  -  |
**400** | Request is malformed. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_get_o_auth_provider**
> V1ClusterCreateOAuthProviderRequest v1_cluster_get_o_auth_provider(provider_id=provider_id)

Get OAuth provider.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_create_o_auth_provider_request import V1ClusterCreateOAuthProviderRequest
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
    provider_id = 'provider_id_example' # str | OAuth provider id. (optional)

    try:
        api_response = api_instance.v1_cluster_get_o_auth_provider(provider_id=provider_id)
        print("The response of DefaultApi->v1_cluster_get_o_auth_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_get_o_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| OAuth provider id. | [optional] 

### Return type

[**V1ClusterCreateOAuthProviderRequest**](V1ClusterCreateOAuthProviderRequest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | OAuth provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_get_o_auth_providers**
> V1ClusterGetOAuthProvidersResponse v1_cluster_get_o_auth_providers()

List all OAuth providers.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_get_o_auth_providers_response import V1ClusterGetOAuthProvidersResponse
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
        api_response = api_instance.v1_cluster_get_o_auth_providers()
        print("The response of DefaultApi->v1_cluster_get_o_auth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_get_o_auth_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ClusterGetOAuthProvidersResponse**](V1ClusterGetOAuthProvidersResponse.md)

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

# **v1_cluster_get_saml_provider**
> V1ClusterSAMLProviderInfo v1_cluster_get_saml_provider(provider_id=provider_id)

Get provider.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_saml_provider_info import V1ClusterSAMLProviderInfo
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
    provider_id = 'provider_id_example' # str | SAML provider id. (optional)

    try:
        api_response = api_instance.v1_cluster_get_saml_provider(provider_id=provider_id)
        print("The response of DefaultApi->v1_cluster_get_saml_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_get_saml_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| SAML provider id. | [optional] 

### Return type

[**V1ClusterSAMLProviderInfo**](V1ClusterSAMLProviderInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |
**400** | Request has invalid provider id length. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_list_saml_providers**
> V1ClusterListSAMLProvidersResponse v1_cluster_list_saml_providers()

List all providers.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_list_saml_providers_response import V1ClusterListSAMLProvidersResponse
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
        api_response = api_instance.v1_cluster_list_saml_providers()
        print("The response of DefaultApi->v1_cluster_list_saml_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_list_saml_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ClusterListSAMLProvidersResponse**](V1ClusterListSAMLProvidersResponse.md)

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

# **v1_cluster_update_o_auth_provider**
> v1_cluster_update_o_auth_provider(provider_id=provider_id, v1_cluster_create_o_auth_provider_request=v1_cluster_create_o_auth_provider_request)

Update an existing provider.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_create_o_auth_provider_request import V1ClusterCreateOAuthProviderRequest
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
    provider_id = 'provider_id_example' # str | OAuth provider id. (optional)
    v1_cluster_create_o_auth_provider_request = openapi_client.V1ClusterCreateOAuthProviderRequest() # V1ClusterCreateOAuthProviderRequest |  (optional)

    try:
        api_instance.v1_cluster_update_o_auth_provider(provider_id=provider_id, v1_cluster_create_o_auth_provider_request=v1_cluster_create_o_auth_provider_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_update_o_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| OAuth provider id. | [optional] 
 **v1_cluster_create_o_auth_provider_request** | [**V1ClusterCreateOAuthProviderRequest**](V1ClusterCreateOAuthProviderRequest.md)|  | [optional] 

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
**204** | OAuth provider updated. |  -  |
**400** | Request is malformed or has invalid provider type. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_update_saml_provider**
> v1_cluster_update_saml_provider(provider_id=provider_id, v1_cluster_saml_provider_info=v1_cluster_saml_provider_info)

Update an existing provider.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_cluster_saml_provider_info import V1ClusterSAMLProviderInfo
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
    provider_id = 'provider_id_example' # str | SAML provider id. (optional)
    v1_cluster_saml_provider_info = openapi_client.V1ClusterSAMLProviderInfo() # V1ClusterSAMLProviderInfo |  (optional)

    try:
        api_instance.v1_cluster_update_saml_provider(provider_id=provider_id, v1_cluster_saml_provider_info=v1_cluster_saml_provider_info)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_cluster_update_saml_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| SAML provider id. | [optional] 
 **v1_cluster_saml_provider_info** | [**V1ClusterSAMLProviderInfo**](V1ClusterSAMLProviderInfo.md)|  | [optional] 

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
**204** | Provider updated. |  -  |
**400** | Request is malformed. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_bearer_token**
> CreateBearerTokenResponse v1_create_bearer_token(user, create_bearer_token_request=create_bearer_token_request)

Generate Bearer token.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_bearer_token_request import CreateBearerTokenRequest
from openapi_client.models.create_bearer_token_response import CreateBearerTokenResponse
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
    create_bearer_token_request = openapi_client.CreateBearerTokenRequest() # CreateBearerTokenRequest |  (optional)

    try:
        api_response = api_instance.v1_create_bearer_token(user, create_bearer_token_request=create_bearer_token_request)
        print("The response of DefaultApi->v1_create_bearer_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_bearer_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **create_bearer_token_request** | [**CreateBearerTokenRequest**](CreateBearerTokenRequest.md)|  | [optional] 

### Return type

[**CreateBearerTokenResponse**](CreateBearerTokenResponse.md)

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

# **v1_create_bucket**
> v1_create_bucket(create_bucket_request=create_bucket_request)

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
    create_bucket_request = openapi_client.CreateBucketRequest() # CreateBucketRequest | Parameters of the new bucket in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_create_bucket(create_bucket_request=create_bucket_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Bucket successfully created. |  * Location - URL of the created bucket. <br>  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | Bucket already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_bucket_transfer**
> CreateBucketTransferResponse v1_create_bucket_transfer(bucket, x_morph_namespace=x_morph_namespace, create_bucket_transfer_request=create_bucket_transfer_request)

Create a new bucket transfer request addressed to a recipient. The recipient must accept it later. Both sender and recipient must belong to the same namespace.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_bucket_transfer_request import CreateBucketTransferRequest
from openapi_client.models.create_bucket_transfer_response import CreateBucketTransferResponse
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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    create_bucket_transfer_request = openapi_client.CreateBucketTransferRequest() # CreateBucketTransferRequest |  (optional)

    try:
        api_response = api_instance.v1_create_bucket_transfer(bucket, x_morph_namespace=x_morph_namespace, create_bucket_transfer_request=create_bucket_transfer_request)
        print("The response of DefaultApi->v1_create_bucket_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_bucket_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
 **create_bucket_transfer_request** | [**CreateBucketTransferRequest**](CreateBucketTransferRequest.md)|  | [optional] 

### Return type

[**CreateBucketTransferResponse**](CreateBucketTransferResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer request successfully created. |  -  |
**400** | At least one parameter is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to create transfer for this bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket or user not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_namespace**
> v1_create_namespace(create_namespace_request=create_namespace_request)

Create a new namespace.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_namespace_request import CreateNamespaceRequest
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
    create_namespace_request = openapi_client.CreateNamespaceRequest() # CreateNamespaceRequest | Parameters of the new namespace in JSON. (optional)

    try:
        api_instance.v1_create_namespace(create_namespace_request=create_namespace_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_namespace_request** | [**CreateNamespaceRequest**](CreateNamespaceRequest.md)| Parameters of the new namespace in JSON. | [optional] 

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
**201** | Namespace successfully created. |  * Location - URL of the created namespace. <br>  |
**400** | At least one namespace parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | Namespace already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_object**
> CreateObjectResponse v1_create_object(bucket, x_morph_path=x_morph_path, x_morph_lifetime=x_morph_lifetime, x_attributes=x_attributes, body=body)

Uploads a new object into the specified bucket. The request body is the raw object bytes.
Object path (name) should be provided via the X-Morph-Path header (Base64-encoded) or 
inside X-Attributes (not empty "FilePath" parameter). If omitted or empty, the request 
is rejected as "Missing object path."
Optional expiration  can be set via X-Morph-Lifetime or inside X-Attributes. If Content-Type 
is not provided in X-Attributes, it is detected from the first 512 bytes of the payload 
([http.DetectContentType](https://pkg.go.dev/net/http#DetectContentType)).
Priority rules:
  1) X-Morph-Path overrides "FilePath" in X-Attributes.
  2) X-Morph-Lifetime overrides "ExpHours" in X-Attributes.
  3) X-Attributes.Content-Type overrides auto-detection (but must be a valid MIME type,
    checked by [mime.ParseMediaType](https://pkg.go.dev/mime#ParseMediaType)).


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
    x_morph_path = 'my-object, cat.png' # str | Object name. It can be a file path or object name, which suits your situation better. The object name encoded in base64. (optional)
    x_morph_lifetime = 24 # int | Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. (optional)
    x_attributes = '{\"FilePath\":\"readme.txt\"}' # str | JSON object with user attributes. The following keys are specially handled: - \"FilePath\": object path (used only if X-Morph-Path is absent). - \"ExpHours\": expiration in hours (used only if X-Morph-Lifetime is absent). - \"Content-Type\": MIME type for the object (validated; overrides auto-detection). - \"Timestamp\": object creation time in RFC 3339 (e.g. \"2022-11-21T07:12:42.68680647Z\")    or HTTP (\"Mon, 21 Nov 2022 07:12:42 GMT\") date format. This value is returned in object   GET/HEAD responses as the \"Last-Modified\" header.  Storage of attributes: - The special keys above are consumed and not stored as custom attributes. - Keys beginning with \"__\" are reserved and must not be used (will result in 400). - Pairs with an empty key or value are ignored.  - All other keys are forwarded as user attributes.  Invalid JSON: - If the header value is not valid JSON of the form map[string]string - 400.  Body requirements when using x-attributes: - Send the raw object bytes as the request body (content-type application/octet-stream is acceptable). - Payload must be non-empty.  (optional)
    body = None # object |  (optional)

    try:
        api_response = api_instance.v1_create_object(bucket, x_morph_path=x_morph_path, x_morph_lifetime=x_morph_lifetime, x_attributes=x_attributes, body=body)
        print("The response of DefaultApi->v1_create_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **x_morph_path** | **str**| Object name. It can be a file path or object name, which suits your situation better. The object name encoded in base64. | [optional] 
 **x_morph_lifetime** | **int**| Object lifetime, in hours. The actual object lifetime will be calculated according network epoch duration. Zero means no expiration. | [optional] 
 **x_attributes** | **str**| JSON object with user attributes. The following keys are specially handled: - \&quot;FilePath\&quot;: object path (used only if X-Morph-Path is absent). - \&quot;ExpHours\&quot;: expiration in hours (used only if X-Morph-Lifetime is absent). - \&quot;Content-Type\&quot;: MIME type for the object (validated; overrides auto-detection). - \&quot;Timestamp\&quot;: object creation time in RFC 3339 (e.g. \&quot;2022-11-21T07:12:42.68680647Z\&quot;)    or HTTP (\&quot;Mon, 21 Nov 2022 07:12:42 GMT\&quot;) date format. This value is returned in object   GET/HEAD responses as the \&quot;Last-Modified\&quot; header.  Storage of attributes: - The special keys above are consumed and not stored as custom attributes. - Keys beginning with \&quot;__\&quot; are reserved and must not be used (will result in 400). - Pairs with an empty key or value are ignored.  - All other keys are forwarded as user attributes.  Invalid JSON: - If the header value is not valid JSON of the form map[string]string - 400.  Body requirements when using x-attributes: - Send the raw object bytes as the request body (content-type application/octet-stream is acceptable). - Payload must be non-empty.  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**CreateObjectResponse**](CreateObjectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Object successfully created. |  * Location - URL of the created object. <br>  |
**400** | At least one object parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**409** | Object already exists. |  -  |
**507** | User doesn&#39;t have enough space. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_system_storage_policy**
> v1_create_system_storage_policy(v1_create_system_storage_policy_request=v1_create_system_storage_policy_request)

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
    v1_create_system_storage_policy_request = openapi_client.V1CreateSystemStoragePolicyRequest() # V1CreateSystemStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_create_system_storage_policy(v1_create_system_storage_policy_request=v1_create_system_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Storage policy created. |  * Location - URL of the created system storage policy. <br>  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | Storage policy with this name already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_user_storage_policy**
> v1_create_user_storage_policy(user, x_morph_namespace=x_morph_namespace, v1_create_user_storage_policy_request=v1_create_user_storage_policy_request)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    v1_create_user_storage_policy_request = openapi_client.V1CreateUserStoragePolicyRequest() # V1CreateUserStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_create_user_storage_policy(user, x_morph_namespace=x_morph_namespace, v1_create_user_storage_policy_request=v1_create_user_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_create_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
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
**201** | Storage policy created. |  * Location - URL of the created user storage policy. <br>  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_bucket**
> v1_delete_bucket(bucket)

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

    try:
        api_instance.v1_delete_bucket(bucket)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 

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
**409** | Bucket locked. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_namespace**
> v1_delete_namespace(namespace)

Delete namespace from the system.

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
    namespace = 'namespace_example' # str | Namespace name.

    try:
        api_instance.v1_delete_namespace(namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace name. | 

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
**204** | Namespace successfully removed. |  -  |
**400** | Session token is omitted or invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Namespace not found (not created or already removed). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_object**
> v1_delete_object(bucket, object)

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

    try:
        api_instance.v1_delete_object(bucket, object)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name or object id. | 

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
> v1_delete_system_storage_policy(policy_name)

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

    try:
        api_instance.v1_delete_system_storage_policy(policy_name)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Storage policy name. | 

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
> v1_delete_user(user, x_morph_namespace=x_morph_namespace)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_instance.v1_delete_user(user, x_morph_namespace=x_morph_namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
**409** | User removal is not allowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_user_storage_policy**
> v1_delete_user_storage_policy(user, policy_name, x_morph_namespace=x_morph_namespace)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_instance.v1_delete_user_storage_policy(user, policy_name, x_morph_namespace=x_morph_namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_delete_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
> bytes v1_download_object(bucket, object, range=range)

Download the object data. No authentication required for public objects.

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
    range = 'bytes=500-999' # str | Request a specific range of bytes from the object. Supports a single range only. (optional)

    try:
        api_response = api_instance.v1_download_object(bucket, object, range=range)
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
 **range** | **str**| Request a specific range of bytes from the object. Supports a single range only. | [optional] 

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Object-Id -  <br>  * X-Attributes -  <br>  * Accept-Ranges -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Last-Modified -  <br>  |
**206** | Partial Content - Successfully retrieved a partial object based on the Range header. |  * X-Object-Id -  <br>  * X-Attributes -  <br>  * Accept-Ranges -  <br>  * Content-Length -  <br>  * Content-Range - Indicates the range of bytes being returned in the response. <br>  * Content-Type -  <br>  * Last-Modified -  <br>  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket or object not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_bearer_token_details**
> GetBearerTokenDetailsResponse v1_get_bearer_token_details(user, token)

Get Bearer token details.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_bearer_token_details_response import GetBearerTokenDetailsResponse
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
    token = 'token_example' # str | Token id.

    try:
        api_response = api_instance.v1_get_bearer_token_details(user, token)
        print("The response of DefaultApi->v1_get_bearer_token_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_bearer_token_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **token** | **str**| Token id. | 

### Return type

[**GetBearerTokenDetailsResponse**](GetBearerTokenDetailsResponse.md)

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

# **v1_get_bearer_tokens**
> GetBearerTokensResponse v1_get_bearer_tokens(user, type=type)

Get Bearer tokens.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_bearer_tokens_response import GetBearerTokensResponse
from openapi_client.models.token_type import TokenType
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
    type = openapi_client.TokenType() # TokenType | Optional filter by token type. If omitted, returns all token types. (optional)

    try:
        api_response = api_instance.v1_get_bearer_tokens(user, type=type)
        print("The response of DefaultApi->v1_get_bearer_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_bearer_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **type** | [**TokenType**](.md)| Optional filter by token type. If omitted, returns all token types. | [optional] 

### Return type

[**GetBearerTokensResponse**](GetBearerTokensResponse.md)

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

# **v1_get_bucket**
> GetBucketResponse v1_get_bucket(bucket)

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

# **v1_get_bucket_quota**
> GetStorageQuotaResponse v1_get_bucket_quota(bucket)

Get bucket quota.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_storage_quota_response import GetStorageQuotaResponse
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

    try:
        api_response = api_instance.v1_get_bucket_quota(bucket)
        print("The response of DefaultApi->v1_get_bucket_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_bucket_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 

### Return type

[**GetStorageQuotaResponse**](GetStorageQuotaResponse.md)

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

# **v1_get_bucket_timelock**
> GetTimelockResponse v1_get_bucket_timelock(bucket)

Get bucket lock time.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_timelock_response import GetTimelockResponse
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

    try:
        api_response = api_instance.v1_get_bucket_timelock(bucket)
        print("The response of DefaultApi->v1_get_bucket_timelock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_bucket_timelock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 

### Return type

[**GetTimelockResponse**](GetTimelockResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | At least one parameter is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_default_storage_quota**
> GetStorageQuotaResponse v1_get_default_storage_quota()

Get default storage quota for a new user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_storage_quota_response import GetStorageQuotaResponse
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

[**GetStorageQuotaResponse**](GetStorageQuotaResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_eacl**
> GetEaclResponse v1_get_eacl(bucket)

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

    try:
        api_response = api_instance.v1_get_eacl(bucket)
        print("The response of DefaultApi->v1_get_eacl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_eacl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 

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

# **v1_get_ir_public_keys**
> List[str] v1_get_ir_public_keys()

Get Inner Ring public keys.

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

    try:
        api_response = api_instance.v1_get_ir_public_keys()
        print("The response of DefaultApi->v1_get_ir_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_ir_public_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_license**
> LicenseResponse v1_get_license()

Get brief license metadata.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.license_response import LicenseResponse
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
        api_response = api_instance.v1_get_license()
        print("The response of DefaultApi->v1_get_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_license: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicenseResponse**](LicenseResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | License not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_metrics**
> GetMetricsResponse v1_get_metrics()

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

    try:
        api_response = api_instance.v1_get_metrics()
        print("The response of DefaultApi->v1_get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **v1_get_namespace**
> GetNamespaceResponse v1_get_namespace(namespace)

Get information about the namespace by name.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_namespace_response import GetNamespaceResponse
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
    namespace = 'namespace_example' # str | Namespace name.

    try:
        api_response = api_instance.v1_get_namespace(namespace)
        print("The response of DefaultApi->v1_get_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace name. | 

### Return type

[**GetNamespaceResponse**](GetNamespaceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Namespace reference is missing or invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to get namespace info. |  * WWW-Authenticate -  <br>  |
**404** | Namespace not found. |  -  |

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
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_system_storage_policy**
> V1GetStoragePolicyResponse v1_get_system_storage_policy(policy_name)

Get system storage policy by name.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_get_storage_policy_response import V1GetStoragePolicyResponse
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

[**V1GetStoragePolicyResponse**](V1GetStoragePolicyResponse.md)

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
**404** | Policy not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user**
> V1GetUserResponse v1_get_user(user, x_morph_namespace=x_morph_namespace)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_get_user(user, x_morph_namespace=x_morph_namespace)
        print("The response of DefaultApi->v1_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user_list**
> GetUserListResponse v1_get_user_list(x_morph_namespace=x_morph_namespace)

Get user list. Here, authentication is not required if there are no registered users.

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_get_user_list(x_morph_namespace=x_morph_namespace)
        print("The response of DefaultApi->v1_get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
**400** | Bearer token required because system contains users. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user_metrics**
> GetUserMetricsResponse v1_get_user_metrics(user, x_morph_namespace=x_morph_namespace)

Get user metrics.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_user_metrics_response import GetUserMetricsResponse
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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_get_user_metrics(user, x_morph_namespace=x_morph_namespace)
        print("The response of DefaultApi->v1_get_user_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

### Return type

[**GetUserMetricsResponse**](GetUserMetricsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_user_storage_policies**
> V1GetUserStoragePoliciesResponse v1_get_user_storage_policies(user, x_morph_namespace=x_morph_namespace)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_get_user_storage_policies(user, x_morph_namespace=x_morph_namespace)
        print("The response of DefaultApi->v1_get_user_storage_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_get_user_storage_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
> V1GetStoragePolicyResponse v1_get_user_storage_policy(user, policy_name, x_morph_namespace=x_morph_namespace)

Get storage policy by name.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_get_storage_policy_response import V1GetStoragePolicyResponse
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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_get_user_storage_policy(user, policy_name, x_morph_namespace=x_morph_namespace)
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
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

### Return type

[**V1GetStoragePolicyResponse**](V1GetStoragePolicyResponse.md)

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

# **v1_head_object**
> v1_head_object(bucket, object)

Get the object metadata. No authentication required for public objects.

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

    try:
        api_instance.v1_head_object(bucket, object)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_head_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **object** | **str**| Object name or object id. | 

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
**200** | OK |  * X-Object-Id -  <br>  * X-Attributes -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Last-Modified -  <br>  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to make this action in the bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket or object not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_bucket_transfers**
> ListBucketTransfersResponse v1_list_bucket_transfers(user, x_morph_namespace=x_morph_namespace)

List pending bucket transfer requests addressed to the authenticated user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.list_bucket_transfers_response import ListBucketTransfersResponse
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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_list_bucket_transfers(user, x_morph_namespace=x_morph_namespace)
        print("The response of DefaultApi->v1_list_bucket_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_bucket_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

### Return type

[**ListBucketTransfersResponse**](ListBucketTransfersResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | At least one parameter is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to list bucket transfers. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_buckets**
> ListBucketsResponse v1_list_buckets(user, cursor=cursor, max_items=max_items, prefix=prefix, x_morph_namespace=x_morph_namespace)

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
    cursor = 'cursor_example' # str | ID to start the next batch from. It returns the first elements batch if empty value passed. You should take `cursor` value from previous response to be able to list items. (optional)
    max_items = 100 # int | Limits the number of buckets in the response. Any value outside the range [1,100] will be overridden to the default of 100 buckets. (optional) (default to 100)
    prefix = 'prefix_example' # str | Prefix of the object's path (name) to filter for. (optional)
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)

    try:
        api_response = api_instance.v1_list_buckets(user, cursor=cursor, max_items=max_items, prefix=prefix, x_morph_namespace=x_morph_namespace)
        print("The response of DefaultApi->v1_list_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **cursor** | **str**| ID to start the next batch from. It returns the first elements batch if empty value passed. You should take &#x60;cursor&#x60; value from previous response to be able to list items. | [optional] 
 **max_items** | **int**| Limits the number of buckets in the response. Any value outside the range [1,100] will be overridden to the default of 100 buckets. | [optional] [default to 100]
 **prefix** | **str**| Prefix of the object&#39;s path (name) to filter for. | [optional] 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 

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
**404** | Requested user is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_namespaces**
> ListNamespacesResponse v1_list_namespaces()

List all namespaces.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.list_namespaces_response import ListNamespacesResponse
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
        api_response = api_instance.v1_list_namespaces()
        print("The response of DefaultApi->v1_list_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_namespaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListNamespacesResponse**](ListNamespacesResponse.md)

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
> ListObjectsResponse v1_list_objects(bucket, cursor=cursor, max_items=max_items, prefix=prefix)

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
    cursor = 'cursor_example' # str | ID to start the next batch from. It returns the first elements batch if empty value passed. You should take `cursor` value from previous response to be able to list items. (optional)
    max_items = 100 # int | Limits amount of objects in response. (optional) (default to 100)
    prefix = 'prefix_example' # str | Prefix of the object's path (name) to filter for. (optional)

    try:
        api_response = api_instance.v1_list_objects(bucket, cursor=cursor, max_items=max_items, prefix=prefix)
        print("The response of DefaultApi->v1_list_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_list_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **cursor** | **str**| ID to start the next batch from. It returns the first elements batch if empty value passed. You should take &#x60;cursor&#x60; value from previous response to be able to list items. | [optional] 
 **max_items** | **int**| Limits amount of objects in response. | [optional] [default to 100]
 **prefix** | **str**| Prefix of the object&#39;s path (name) to filter for. | [optional] 

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
> V1LoginResponse v1_login(x_morph_namespace=x_morph_namespace, v1_login_request=v1_login_request)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    v1_login_request = openapi_client.V1LoginRequest() # V1LoginRequest |  (optional)

    try:
        api_response = api_instance.v1_login(x_morph_namespace=x_morph_namespace, v1_login_request=v1_login_request)
        print("The response of DefaultApi->v1_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
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

# **v1_o_auth_callback**
> v1_o_auth_callback(state=state, code=code, device_id=device_id)

OAuth provider callback.

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
    state = 'state_example' # str | State to identify request. (optional)
    code = 'code_example' # str | Code to identify request. (optional)
    device_id = 'device_id_example' # str | Unique device ID received from OAuth provider. (optional)

    try:
        api_instance.v1_o_auth_callback(state=state, code=code, device_id=device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_o_auth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| State to identify request. | [optional] 
 **code** | **str**| Code to identify request. | [optional] 
 **device_id** | **str**| Unique device ID received from OAuth provider. | [optional] 

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
**307** | Successfully authorized. |  -  |
**400** | Invalid response from OAuth provider or wrong provider configuration. |  -  |
**403** | OAuth provider auth failed. |  -  |
**404** | OAuth provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_o_auth_login**
> v1_o_auth_login(provider_id=provider_id)

Login using OAuth provider.

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
    provider_id = 'provider_id_example' # str | OAuth provider id. (optional)

    try:
        api_instance.v1_o_auth_login(provider_id=provider_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_o_auth_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| OAuth provider id. | [optional] 

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
**307** | Redirect to auth provider resource. |  -  |
**404** | OAuth provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_register_user**
> v1_register_user(user, x_morph_namespace=x_morph_namespace, v1_update_user_request=v1_update_user_request)

Register a new user. This method should also be used to register the first admin. In the case of the first admin, authentication is not required.

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    v1_update_user_request = openapi_client.V1UpdateUserRequest() # V1UpdateUserRequest |  (optional)

    try:
        api_instance.v1_register_user(user, x_morph_namespace=x_morph_namespace, v1_update_user_request=v1_update_user_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
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
**201** | User successfully registered. |  * Location - URL of the created user. <br>  |
**400** | Passed account data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**409** | User with this name already registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_revoke_bearer_token**
> v1_revoke_bearer_token(user, token)

Revoke Bearer token.

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
    token = 'token_example' # str | Token id.

    try:
        api_instance.v1_revoke_bearer_token(user, token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_revoke_bearer_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **token** | **str**| Token id. | 

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

# **v1_s3_create_access_token**
> S3CreateAccessTokenResponse v1_s3_create_access_token(user, s3_create_access_token_request=s3_create_access_token_request)

Generate s3 access tokens.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.s3_create_access_token_request import S3CreateAccessTokenRequest
from openapi_client.models.s3_create_access_token_response import S3CreateAccessTokenResponse
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
    s3_create_access_token_request = openapi_client.S3CreateAccessTokenRequest() # S3CreateAccessTokenRequest |  (optional)

    try:
        api_response = api_instance.v1_s3_create_access_token(user, s3_create_access_token_request=s3_create_access_token_request)
        print("The response of DefaultApi->v1_s3_create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **s3_create_access_token_request** | [**S3CreateAccessTokenRequest**](S3CreateAccessTokenRequest.md)|  | [optional] 

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
> S3GetAccessTokensResponse v1_s3_get_access_tokens(user)

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

    try:
        api_response = api_instance.v1_s3_get_access_tokens(user)
        print("The response of DefaultApi->v1_s3_get_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_get_access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 

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
> S3GetAccessTokenDetailsResponse v1_s3_get_token_details(user, token)

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
    token = 'token_example' # str | Token id.

    try:
        api_response = api_instance.v1_s3_get_token_details(user, token)
        print("The response of DefaultApi->v1_s3_get_token_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_get_token_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **token** | **str**| Token id. | 

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
> v1_s3_revoke_token(user, token)

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
    token = 'token_example' # str | Token id.

    try:
        api_instance.v1_s3_revoke_token(user, token)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_s3_revoke_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **token** | **str**| Token id. | 

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

# **v1_saml_acs**
> v1_saml_acs(provider_id=provider_id)

ACS route for IDP provider. It is called by IDP.

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
    provider_id = 'provider_id_example' # str | SAML provider id. (optional)

    try:
        api_instance.v1_saml_acs(provider_id=provider_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_saml_acs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| SAML provider id. | [optional] 

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
**302** | Access granted. |  -  |
**404** | Provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_saml_login**
> v1_saml_login(provider_id=provider_id)

Login using SAML provider.

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
    provider_id = 'provider_id_example' # str | SAML provider id. (optional)

    try:
        api_instance.v1_saml_login(provider_id=provider_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_saml_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| SAML provider id. | [optional] 

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
**307** | Redirect to saml provider resource. |  -  |
**404** | Provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_saml_metadata**
> v1_saml_metadata(provider_id=provider_id)

Get SP metadata.

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
    provider_id = 'provider_id_example' # str | SAML provider id. (optional)

    try:
        api_instance.v1_saml_metadata(provider_id=provider_id)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_saml_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| SAML provider id. | [optional] 

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
**200** | OK. |  -  |
**404** | Provider not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_search_objects**
> SearchObjectsResponse v1_search_objects(bucket, search_objects_request, cursor=cursor, max_items=max_items)

Search for objects in the bucket using structured filters. Returns a list of objects with requested attributes.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.search_objects_request import SearchObjectsRequest
from openapi_client.models.search_objects_response import SearchObjectsResponse
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
    search_objects_request = openapi_client.SearchObjectsRequest() # SearchObjectsRequest | 
    cursor = 'cursor_example' # str | ID to start the next batch from. It returns the first elements batch if empty value passed. You should take `cursor` value from previous response to be able to list items. (optional)
    max_items = 100 # int | Limits amount of objects in response. (optional) (default to 100)

    try:
        api_response = api_instance.v1_search_objects(bucket, search_objects_request, cursor=cursor, max_items=max_items)
        print("The response of DefaultApi->v1_search_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_search_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **search_objects_request** | [**SearchObjectsRequest**](SearchObjectsRequest.md)|  | 
 **cursor** | **str**| ID to start the next batch from. It returns the first elements batch if empty value passed. You should take &#x60;cursor&#x60; value from previous response to be able to list items. | [optional] 
 **max_items** | **int**| Limits amount of objects in response. | [optional] [default to 100]

### Return type

[**SearchObjectsResponse**](SearchObjectsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filtered object list. |  -  |
**400** | At least one parameter is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | User is not authorized to search in this bucket. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_bucket_quota**
> v1_set_bucket_quota(bucket, set_storage_quota_request=set_storage_quota_request)

Set bucket quota.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.set_storage_quota_request import SetStorageQuotaRequest
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
    set_storage_quota_request = openapi_client.SetStorageQuotaRequest() # SetStorageQuotaRequest | Parameters of the new quota in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_set_bucket_quota(bucket, set_storage_quota_request=set_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_bucket_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **set_storage_quota_request** | [**SetStorageQuotaRequest**](SetStorageQuotaRequest.md)| Parameters of the new quota in JSON. Required only for payload generation request. | [optional] 

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
**204** | Quota successfully put. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_bucket_timelock**
> v1_set_bucket_timelock(bucket, set_timelock_request=set_timelock_request)

Set bucket lock time.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.set_timelock_request import SetTimelockRequest
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
    set_timelock_request = openapi_client.SetTimelockRequest() # SetTimelockRequest |  (optional)

    try:
        api_instance.v1_set_bucket_timelock(bucket, set_timelock_request=set_timelock_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_bucket_timelock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
 **set_timelock_request** | [**SetTimelockRequest**](SetTimelockRequest.md)|  | [optional] 

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
**204** | Lock time successfully put. |  -  |
**400** | At least one parameter is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_default_storage_quota**
> v1_set_default_storage_quota(set_storage_quota_request=set_storage_quota_request)

Set default storage quota for a new user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.set_storage_quota_request import SetStorageQuotaRequest
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
    set_storage_quota_request = openapi_client.SetStorageQuotaRequest() # SetStorageQuotaRequest |  (optional)

    try:
        api_instance.v1_set_default_storage_quota(set_storage_quota_request=set_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_default_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_storage_quota_request** | [**SetStorageQuotaRequest**](SetStorageQuotaRequest.md)|  | [optional] 

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
**204** | Quota changed. |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_eacl**
> v1_set_eacl(bucket, set_eacl_request=set_eacl_request)

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
    set_eacl_request = openapi_client.SetEaclRequest() # SetEaclRequest | Parameters of the new EACL in JSON. Required only for payload generation request. (optional)

    try:
        api_instance.v1_set_eacl(bucket, set_eacl_request=set_eacl_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_eacl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket name. | 
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
**204** | EACL successfully put. |  -  |
**400** | At least one bucket parameter is invalid (e.g. required parameter is missing). |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | Bucket not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_user_storage_quota**
> v1_set_user_storage_quota(user, x_morph_namespace=x_morph_namespace, set_storage_quota_request=set_storage_quota_request)

Change user storage quota.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.set_storage_quota_request import SetStorageQuotaRequest
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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    set_storage_quota_request = openapi_client.SetStorageQuotaRequest() # SetStorageQuotaRequest |  (optional)

    try:
        api_instance.v1_set_user_storage_quota(user, x_morph_namespace=x_morph_namespace, set_storage_quota_request=set_storage_quota_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_set_user_storage_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
 **set_storage_quota_request** | [**SetStorageQuotaRequest**](SetStorageQuotaRequest.md)|  | [optional] 

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
**204** | User quota successfully changed. |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_system_storage_policy**
> v1_update_system_storage_policy(policy_name, v1_update_storage_policy_request=v1_update_storage_policy_request)

Update system storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_update_storage_policy_request import V1UpdateStoragePolicyRequest
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
    v1_update_storage_policy_request = openapi_client.V1UpdateStoragePolicyRequest() # V1UpdateStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_update_system_storage_policy(policy_name, v1_update_storage_policy_request=v1_update_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_system_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Storage policy name. | 
 **v1_update_storage_policy_request** | [**V1UpdateStoragePolicyRequest**](V1UpdateStoragePolicyRequest.md)|  | [optional] 

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
**204** | Storage policy updated. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user**
> v1_update_user(user, x_morph_namespace=x_morph_namespace, v1_update_user_request=v1_update_user_request)

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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    v1_update_user_request = openapi_client.V1UpdateUserRequest() # V1UpdateUserRequest |  (optional)

    try:
        api_instance.v1_update_user(user, x_morph_namespace=x_morph_namespace, v1_update_user_request=v1_update_user_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
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
**204** | User successfully updated. |  -  |
**400** | Passed account data is invalid. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**404** | User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user_storage_policy**
> v1_update_user_storage_policy(user, policy_name, x_morph_namespace=x_morph_namespace, v1_update_storage_policy_request=v1_update_storage_policy_request)

Update storage policy.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.v1_update_storage_policy_request import V1UpdateStoragePolicyRequest
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
    x_morph_namespace = 'team-a' # str | Namespace of the target user or auth provider. If omitted, the default namespace \"\" is used. For backward compatibility, existing clients may omit this header. (optional)
    v1_update_storage_policy_request = openapi_client.V1UpdateStoragePolicyRequest() # V1UpdateStoragePolicyRequest |  (optional)

    try:
        api_instance.v1_update_user_storage_policy(user, policy_name, x_morph_namespace=x_morph_namespace, v1_update_storage_policy_request=v1_update_storage_policy_request)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_update_user_storage_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User name. | 
 **policy_name** | **str**| Storage policy name. | 
 **x_morph_namespace** | **str**| Namespace of the target user or auth provider. If omitted, the default namespace \&quot;\&quot; is used. For backward compatibility, existing clients may omit this header. | [optional] 
 **v1_update_storage_policy_request** | [**V1UpdateStoragePolicyRequest**](V1UpdateStoragePolicyRequest.md)|  | [optional] 

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
**204** | Storage policy updated. |  -  |
**401** | Token is missing or incorrect. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upload_license**
> v1_upload_license(body=body)

Upload license.

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
    body = None # object |  (optional)

    try:
        api_instance.v1_upload_license(body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_upload_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | License successfully uploaded. |  -  |
**400** | Passed data is invalid. |  -  |
**401** | Authentication token is invalid, missing or expired. |  * WWW-Authenticate -  <br>  |
**403** | Insufficient rights to execute request. |  * WWW-Authenticate -  <br>  |
**413** | License too large. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

