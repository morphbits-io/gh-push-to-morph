# CreateBearerTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **str** | The value can be set in minutes, hours or as a date. Note that the actual token lifetime will be converted into epochs, which may cause a slight variation from the specified value. | [optional] [default to '30 days.']
**create_bucket** | **bool** | When set to true, this token grants permission to create buckets. Note that this option enables &#x60;setBucketEacl&#x60; as well. | [optional] [default to True]
**delete_bucket** | **bool** | When set to true, this token grants permission to delete buckets. | [optional] [default to True]
**set_bucket_eacl** | **bool** | When set to true, this token grants permission to set buckets EACLs. | [optional] [default to True]
**bucket_name** | **str** | When set to a non-empty value, this restricts the token to function exclusively within this bucket. Note, if you set this option, you cannot create a bucket, even if &#x60;createBucket&#x60; is set to true. | [optional] 
**token_name** | **str** | User defined token name. It may contain \&quot;a-z\&quot;, \&quot;A-Z\&quot;, \&quot;0-9\&quot;, \&quot;.\&quot;, \&quot;-\&quot;, \&quot; \&quot;. | 
**read_content** | **bool** | Flag allowing to read objects with this token. | [optional] [default to True]
**read_headers** | **bool** | Flag allowing to read headers objects with this token. | [optional] [default to True]
**create** | **bool** | Flag allowing to create objects with this token. | [optional] [default to True]
**delete** | **bool** | Flag allowing to delete objects with this token. | [optional] [default to True]
**register_user** | **bool** | When set to true, this token grants permission to register a new user. This option is available to admins only. | [optional] [default to False]
**update_user** | **bool** | When set to true, this token grants permission to update an existing user. This option is available to admins only. | [optional] [default to False]
**delete_user** | **bool** | When set to true, this token grants permission to delete an existing user. This option is available to admins only. | [optional] [default to False]
**list_user** | **bool** | When set to true, this token grants permission to list users. This option is available to admins only. | [optional] [default to False]
**set_user_quota** | **bool** | When set to true, this token grants permission to set user storage quota. This option is available to admins only. | [optional] [default to False]
**set_default_storage_quota** | **bool** | When set to true, this token grants permission to set default storage quota. This option is available to admins only. | [optional] [default to False]
**get_user_policies** | **bool** | When set to true, this token grants permission to get user storage policies. | [optional] [default to False]
**create_user_policy** | **bool** | When set to true, this token grants permission to create user storage policy. | [optional] [default to False]
**update_user_policy** | **bool** | When set to true, this token grants permission to update user storage policy. | [optional] [default to False]
**get_user_policy** | **bool** | When set to true, this token grants permission to get user storage policy. | [optional] [default to False]
**delete_user_policy** | **bool** | When set to true, this token grants permission to delete user storage policy. | [optional] [default to False]
**create_system_policy** | **bool** | When set to true, this token grants permission to create system storage policy. This option is available to admins only. | [optional] [default to False]
**update_system_policy** | **bool** | When set to true, this token grants permission to update system storage policy. This option is available to admins only. | [optional] [default to False]
**delete_system_policy** | **bool** | When set to true, this token grants permission to delete system storage policy. This option is available to admins only. | [optional] [default to False]
**s3_get_tokens** | **bool** | When set to true, this token grants permission to get S3 access tokens. | [optional] [default to False]
**s3_create_token** | **bool** | When set to true, this token grants permission to create S3 access token. | [optional] [default to False]
**s3_token_details** | **bool** | When set to true, this token grants permission to get S3 access token details. | [optional] [default to False]
**s3_revoke_token** | **bool** | When set to true, this token grants permission to revoke S3 access token. | [optional] [default to False]
**get_bearer_tokens** | **bool** | When set to true, this token grants permission to get Bearer tokens. | [optional] [default to False]
**create_bearer_token** | **bool** | When set to true, this token grants permission to create Bearer token. | [optional] [default to False]
**bearer_token_details** | **bool** | When set to true, this token grants permission to get Bearer token details. | [optional] [default to False]
**revoke_bearer_token** | **bool** | When set to true, this token grants permission to revoke Bearer token. | [optional] [default to False]
**create_o_auth_provider** | **bool** | When set to true, this token grants permission to create OAuth providers. | [optional] [default to False]
**update_o_auth_provider** | **bool** | When set to true, this token grants permission to update OAuth providers. | [optional] [default to False]
**delete_o_auth_provider** | **bool** | When set to true, this token grants permission to delete OAuth providers. | [optional] [default to False]
**upload_license** | **bool** | When set to true, this token grants permission to upload license. This option is available to admins only. | [optional] [default to False]
**get_license** | **bool** | When set to true, this token grants permission to get license metadata. This option is available to admins only. | [optional] [default to False]
**get_ir_public_keys** | **bool** | When set to true, this token grants permission to get IR public keys. This option is available to admins only. | [optional] [default to False]
**get_user_metrics** | **bool** | When set to true, this token grants permission to get user metrics. This option is available to admins only. | [optional] [default to False]
**create_saml_provider** | **bool** | When set to true, this token grants permission to create SAML providers. | [optional] [default to False]
**update_saml_provider** | **bool** | When set to true, this token grants permission to update SAML providers. | [optional] [default to False]
**delete_saml_provider** | **bool** | When set to true, this token grants permission to delete SAML providers. | [optional] [default to False]
**list_bucket_transfers** | **bool** | When set to true, this token grants permission to list user bucket transfers. | [optional] [default to False]
**create_namespace** | **bool** | When set to true, this token grants permission to create namespace. This option is available to admins only. | [optional] [default to False]
**get_namespace** | **bool** | When set to true, this token grants permission to get namespace. This option is available to admins only. | [optional] [default to False]
**list_namespaces** | **bool** | When set to true, this token grants permission to list namespaces. This option is available to admins only. | [optional] [default to False]
**delete_namespace** | **bool** | When set to true, this token grants permission to delete namespace. This option is available to admins only. | [optional] [default to False]

## Example

```python
from openapi_client.models.create_bearer_token_request import CreateBearerTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBearerTokenRequest from a JSON string
create_bearer_token_request_instance = CreateBearerTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBearerTokenRequest.to_json())

# convert the object into a dict
create_bearer_token_request_dict = create_bearer_token_request_instance.to_dict()
# create an instance of CreateBearerTokenRequest from a dict
create_bearer_token_request_from_dict = CreateBearerTokenRequest.from_dict(create_bearer_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


