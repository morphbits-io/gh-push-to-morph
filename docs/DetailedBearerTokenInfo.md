# DetailedBearerTokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_bucket** | **bool** | When set to true, this token grants permission to create buckets. Note that this option enables &#x60;setBucketEacl&#x60; as well. | [default to True]
**delete_bucket** | **bool** | When set to true, this token grants permission to delete buckets. | [default to True]
**set_bucket_eacl** | **bool** | When set to true, this token grants permission to set buckets EACLs. | [default to True]
**expires_at** | **datetime** | Estimated time when token will expire in RFC 3339 format. | 
**created_at** | **datetime** | Time when token was issued in RFC 3339 format. | 
**name** | **str** | User-defined token name. | 
**bucket_name** | **str** | When set to non empty value, it restricts the token to function exclusively within this bucket. Note, if you set this option, you cannot create a bucket, even if &#x60;createBucket&#x60; is set to true. | 
**read_content** | **bool** | When set to true, this token grants permission to read objects. | 
**read_headers** | **bool** | When set to true, this token grants permission to read objects headers. | 
**create** | **bool** | When set to true, this token grants permission to create objects. | 
**delete** | **bool** | When set to true, this token grants permission to delete objects. | 
**register_user** | **bool** | When set to true, this token grants permission to register a new user. This option is available to admins only. | [default to False]
**update_user** | **bool** | When set to true, this token grants permission to update an existing user. This option is available to admins only. | [default to False]
**delete_user** | **bool** | When set to true, this token grants permission to delete an existing user. This option is available to admins only. | [default to False]
**list_user** | **bool** | When set to true, this token grants permission to list users. This option is available to admins only. | [default to False]
**set_user_quota** | **bool** | When set to true, this token grants permission to set user storage quota. This option is available to admins only. | [default to False]
**set_default_storage_quota** | **bool** | When set to true, this token grants permission to set default storage quota. This option is available to admins only. | [default to False]
**get_user_policies** | **bool** | When set to true, this token grants permission to get user storage policies. | [default to False]
**create_user_policy** | **bool** | When set to true, this token grants permission to create user storage policy. | [default to False]
**update_user_policy** | **bool** | When set to true, this token grants permission to update user storage policy. | [default to False]
**get_user_policy** | **bool** | When set to true, this token grants permission to get user storage policy. | [default to False]
**delete_user_policy** | **bool** | When set to true, this token grants permission to delete user storage policy. | [default to False]
**create_system_policy** | **bool** | When set to true, this token grants permission to create system storage policy. This option is available to admins only. | [default to False]
**update_system_policy** | **bool** | When set to true, this token grants permission to update system storage policy. This option is available to admins only. | [default to False]
**delete_system_policy** | **bool** | When set to true, this token grants permission to delete system storage policy. This option is available to admins only. | [default to False]
**s3_get_tokens** | **bool** | When set to true, this token grants permission to get S3 access tokens. | [default to False]
**s3_create_token** | **bool** | When set to true, this token grants permission to create S3 access token. | [default to False]
**s3_token_details** | **bool** | When set to true, this token grants permission to get S3 access token details. | [default to False]
**s3_revoke_token** | **bool** | When set to true, this token grants permission to revoke S3 access token. | [default to False]
**get_bearer_tokens** | **bool** | When set to true, this token grants permission to get Bearer tokens. | [default to False]
**create_bearer_token** | **bool** | When set to true, this token grants permission to create Bearer token. | [default to False]
**bearer_token_details** | **bool** | When set to true, this token grants permission to get Bearer token details. | [default to False]
**revoke_bearer_token** | **bool** | When set to true, this token grants permission to revoke Bearer token. | [default to False]
**create_o_auth_provider** | **bool** | When set to true, this token grants permission to create OAuth provider. | [default to False]
**update_o_auth_provider** | **bool** | When set to true, this token grants permission to update OAuth provider. | [default to False]
**delete_o_auth_provider** | **bool** | When set to true, this token grants permission to delete OAuth provider. | [default to False]
**upload_license** | **bool** | When set to true, this token grants permission to upload license. This option is available to admins only. | [default to False]
**get_license** | **bool** | When set to true, this token grants permission to get license metadata. This option is available to admins only. | [default to False]
**get_ir_public_keys** | **bool** | When set to true, this token grants permission to get IR public keys. This option is available to admins only. | [default to False]
**get_user_metrics** | **bool** | When set to true, this token grants permission to get user metrics. This option is available to admins only. | [default to False]
**create_saml_provider** | **bool** | When set to true, this token grants permission to create SAML provider. | [default to False]
**update_saml_provider** | **bool** | When set to true, this token grants permission to update SAML provider. | [default to False]
**delete_saml_provider** | **bool** | When set to true, this token grants permission to delete SAML provider. | [default to False]
**list_bucket_transfers** | **bool** | When set to true, this token grants permission to list user bucket transfers. | [default to False]
**create_namespace** | **bool** | When set to true, this token grants permission to create namespace. This option is available to admins only. | [default to False]
**get_namespace** | **bool** | When set to true, this token grants permission to get namespace. This option is available to admins only. | [default to False]
**list_namespaces** | **bool** | When set to true, this token grants permission to list namespaces. This option is available to admins only. | [default to False]
**delete_namespace** | **bool** | When set to true, this token grants permission to delete namespace. This option is available to admins only. | [default to False]

## Example

```python
from openapi_client.models.detailed_bearer_token_info import DetailedBearerTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedBearerTokenInfo from a JSON string
detailed_bearer_token_info_instance = DetailedBearerTokenInfo.from_json(json)
# print the JSON string representation of the object
print(DetailedBearerTokenInfo.to_json())

# convert the object into a dict
detailed_bearer_token_info_dict = detailed_bearer_token_info_instance.to_dict()
# create an instance of DetailedBearerTokenInfo from a dict
detailed_bearer_token_info_from_dict = DetailedBearerTokenInfo.from_dict(detailed_bearer_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


