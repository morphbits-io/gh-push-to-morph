# CommonCreateTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **str** | The value can be set in minutes, hours or as a date. Note that the actual token lifetime will be converted into epochs, which may cause a slight variation from the specified value. | [optional] [default to '30 days.']
**create_bucket** | **bool** | When set to true, this token grants permission to create buckets. Note that this option enables &#x60;setBucketEacl&#x60; as well. | [optional] [default to True]
**delete_bucket** | **bool** | When set to true, this token grants permission to delete buckets. | [optional] [default to True]
**set_bucket_eacl** | **bool** | When set to true, this token grants permission to set buckets EACLs. | [optional] [default to True]
**bucket_name** | **str** | When set to a non-empty value, this restricts the token to function exclusively within this bucket. Note, if you set this option, you cannot create a bucket, even if &#x60;createBucket&#x60; is set to true. | [optional] 
**token_name** | **str** | User defined token name. It may contain \&quot;a-z\&quot;, \&quot;A-Z\&quot;, \&quot;0-9\&quot;, \&quot;.\&quot;, \&quot;-\&quot;, \&quot; \&quot;. | 

## Example

```python
from openapi_client.models.common_create_token_request import CommonCreateTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCreateTokenRequest from a JSON string
common_create_token_request_instance = CommonCreateTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CommonCreateTokenRequest.to_json())

# convert the object into a dict
common_create_token_request_dict = common_create_token_request_instance.to_dict()
# create an instance of CommonCreateTokenRequest from a dict
common_create_token_request_from_dict = CommonCreateTokenRequest.from_dict(common_create_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


