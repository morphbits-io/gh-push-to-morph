# CreateBucketTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_login** | **str** | Recipient user login. | 

## Example

```python
from openapi_client.models.create_bucket_transfer_request import CreateBucketTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBucketTransferRequest from a JSON string
create_bucket_transfer_request_instance = CreateBucketTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBucketTransferRequest.to_json())

# convert the object into a dict
create_bucket_transfer_request_dict = create_bucket_transfer_request_instance.to_dict()
# create an instance of CreateBucketTransferRequest from a dict
create_bucket_transfer_request_from_dict = CreateBucketTransferRequest.from_dict(create_bucket_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


