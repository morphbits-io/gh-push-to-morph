# GetBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **datetime** | Bucket creation date in RFC 3339 format. | 
**name** | **str** | Bucket name. | 
**basic_acl** | [**BasicACL**](BasicACL.md) |  | 
**e_acl** | [**EACL**](EACL.md) |  | 
**placement_policy** | [**StoragePolicy**](StoragePolicy.md) |  | 
**owner** | **str** | User that owns this bucket. | 
**used_space** | **int** | Bucket used space in bytes. | 

## Example

```python
from openapi_client.models.get_bucket_response import GetBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBucketResponse from a JSON string
get_bucket_response_instance = GetBucketResponse.from_json(json)
# print the JSON string representation of the object
print(GetBucketResponse.to_json())

# convert the object into a dict
get_bucket_response_dict = get_bucket_response_instance.to_dict()
# create an instance of GetBucketResponse from a dict
get_bucket_response_from_dict = GetBucketResponse.from_dict(get_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


