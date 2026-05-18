# BucketTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transfer ID. | 
**bucket** | **str** | Bucket name. | 
**sender_login** | **str** | Sender user login. | 
**recipient_login** | **str** | Recipient user login. | 

## Example

```python
from openapi_client.models.bucket_transfer import BucketTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BucketTransfer from a JSON string
bucket_transfer_instance = BucketTransfer.from_json(json)
# print the JSON string representation of the object
print(BucketTransfer.to_json())

# convert the object into a dict
bucket_transfer_dict = bucket_transfer_instance.to_dict()
# create an instance of BucketTransfer from a dict
bucket_transfer_from_dict = BucketTransfer.from_dict(bucket_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


