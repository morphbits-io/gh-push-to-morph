# CreateBucketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Bucket name. | 
**placement_policy_name** | **str** | Placement policy name. | 
**basic_acl** | [**BasicACL**](BasicACL.md) |  | 
**lock_hours** | **int** | Optional parameter to set the period in hours during which the bucket cannot be deleted from the time of its creation. This period can be extended, but there is no way to make it expire earlier. | [optional] 

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


