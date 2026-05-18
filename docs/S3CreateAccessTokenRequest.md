# S3CreateAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **str** | The value can be set in minutes, hours or as a date. Note that the actual token lifetime will be converted into epochs, which may cause a slight variation from the specified value. | [optional] [default to '30 days.']
**create_bucket** | **bool** | When set to true, this token grants permission to create buckets. Note that this option enables &#x60;setBucketEacl&#x60; as well. | [optional] [default to True]
**delete_bucket** | **bool** | When set to true, this token grants permission to delete buckets. | [optional] [default to True]
**set_bucket_eacl** | **bool** | When set to true, this token grants permission to set buckets EACLs. | [optional] [default to True]
**bucket_name** | **str** | When set to a non-empty value, this restricts the token to function exclusively within this bucket. Note, if you set this option, you cannot create a bucket, even if &#x60;createBucket&#x60; is set to true. | [optional] 
**token_name** | **str** | User defined token name. It may contain \&quot;a-z\&quot;, \&quot;A-Z\&quot;, \&quot;0-9\&quot;, \&quot;.\&quot;, \&quot;-\&quot;, \&quot; \&quot;. | 
**read** | **bool** | Flag allowing to read objects with this token. | [optional] [default to True]
**modify** | **bool** | Flag allowing to create and delete objects with this token. | [optional] [default to True]
**manage_settings** | **bool** | Flag allowing to manage S3 bucket cors, tags, notifications, policy, ownerships and locks with this token. | [optional] [default to True]

## Example

```python
from openapi_client.models.s3_create_access_token_request import S3CreateAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of S3CreateAccessTokenRequest from a JSON string
s3_create_access_token_request_instance = S3CreateAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(S3CreateAccessTokenRequest.to_json())

# convert the object into a dict
s3_create_access_token_request_dict = s3_create_access_token_request_instance.to_dict()
# create an instance of S3CreateAccessTokenRequest from a dict
s3_create_access_token_request_from_dict = S3CreateAccessTokenRequest.from_dict(s3_create_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


