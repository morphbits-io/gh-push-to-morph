# V1S3CreateAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **str** | The value can be set in minutes, hours or as a date. Note that the actual token lifetime will be converted into epochs, which may cause a slight variation from the specified value. | [optional] [default to '30 days.']
**create_bucket** | **bool** | When set to true, this token grants permission to create buckets. Note that this option enables &#x60;setBucketEacl&#x60; as well. | [optional] [default to True]
**delete_bucket** | **bool** | When set to true, this token grants permission to delete buckets. | [optional] [default to True]
**set_bucket_eacl** | **bool** | When set to true, this token grants permission to set buckets EACLs. | [optional] [default to True]
**read_content** | **bool** | Flag allowing to read objects with this token. | [optional] [default to True]
**read_headers** | **bool** | Flag allowing to read headers objects with this token. | [optional] [default to True]
**create** | **bool** | Flag allowing to create objects with this token. | [optional] [default to True]
**delete** | **bool** | Flag allowing to delete objects with this token. | [optional] [default to True]
**container_name** | **str** | When set to a non-empty value, this restricts the token to function exclusively within this bucket. | [optional] 
**token_name** | **str** | User defined token name. It may contain \&quot;a-z\&quot;, \&quot;A-Z\&quot;, \&quot;0-9\&quot;, \&quot;.\&quot;, \&quot;-\&quot;, \&quot; \&quot;. | 

## Example

```python
from openapi_client.models.v1_s3_create_access_token_request import V1S3CreateAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1S3CreateAccessTokenRequest from a JSON string
v1_s3_create_access_token_request_instance = V1S3CreateAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(V1S3CreateAccessTokenRequest.to_json())

# convert the object into a dict
v1_s3_create_access_token_request_dict = v1_s3_create_access_token_request_instance.to_dict()
# create an instance of V1S3CreateAccessTokenRequest from a dict
v1_s3_create_access_token_request_from_dict = V1S3CreateAccessTokenRequest.from_dict(v1_s3_create_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


