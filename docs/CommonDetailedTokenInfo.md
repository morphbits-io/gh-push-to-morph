# CommonDetailedTokenInfo


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

## Example

```python
from openapi_client.models.common_detailed_token_info import CommonDetailedTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDetailedTokenInfo from a JSON string
common_detailed_token_info_instance = CommonDetailedTokenInfo.from_json(json)
# print the JSON string representation of the object
print(CommonDetailedTokenInfo.to_json())

# convert the object into a dict
common_detailed_token_info_dict = common_detailed_token_info_instance.to_dict()
# create an instance of CommonDetailedTokenInfo from a dict
common_detailed_token_info_from_dict = CommonDetailedTokenInfo.from_dict(common_detailed_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


