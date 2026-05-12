# ListBucketTransfersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfers** | [**List[BucketTransfer]**](BucketTransfer.md) |  | 

## Example

```python
from openapi_client.models.list_bucket_transfers_response import ListBucketTransfersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBucketTransfersResponse from a JSON string
list_bucket_transfers_response_instance = ListBucketTransfersResponse.from_json(json)
# print the JSON string representation of the object
print(ListBucketTransfersResponse.to_json())

# convert the object into a dict
list_bucket_transfers_response_dict = list_bucket_transfers_response_instance.to_dict()
# create an instance of ListBucketTransfersResponse from a dict
list_bucket_transfers_response_from_dict = ListBucketTransfersResponse.from_dict(list_bucket_transfers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


