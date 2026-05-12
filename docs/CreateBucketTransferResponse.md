# CreateBucketTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer** | [**BucketTransfer**](BucketTransfer.md) |  | 

## Example

```python
from openapi_client.models.create_bucket_transfer_response import CreateBucketTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBucketTransferResponse from a JSON string
create_bucket_transfer_response_instance = CreateBucketTransferResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBucketTransferResponse.to_json())

# convert the object into a dict
create_bucket_transfer_response_dict = create_bucket_transfer_response_instance.to_dict()
# create an instance of CreateBucketTransferResponse from a dict
create_bucket_transfer_response_from_dict = CreateBucketTransferResponse.from_dict(create_bucket_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


