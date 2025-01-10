# CreateBucketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Bucket name. | 
**basic_acl** | [**BasicACL**](BasicACL.md) |  | 
**placement_policy** | [**StoragePolicy**](StoragePolicy.md) |  | 

## Example

```python
from openapi_client.models.create_bucket_request import CreateBucketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBucketRequest from a JSON string
create_bucket_request_instance = CreateBucketRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBucketRequest.to_json())

# convert the object into a dict
create_bucket_request_dict = create_bucket_request_instance.to_dict()
# create an instance of CreateBucketRequest from a dict
create_bucket_request_from_dict = CreateBucketRequest.from_dict(create_bucket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


