# SetStorageQuotaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**soft_quota** | **int** | Default storage soft quota for users in bytes. Must be less than the hard quota. | 
**hard_quota** | **int** | Default storage hard quota for users in bytes. Must be greater than the soft quota. | 

## Example

```python
from openapi_client.models.set_storage_quota_request import SetStorageQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetStorageQuotaRequest from a JSON string
set_storage_quota_request_instance = SetStorageQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(SetStorageQuotaRequest.to_json())

# convert the object into a dict
set_storage_quota_request_dict = set_storage_quota_request_instance.to_dict()
# create an instance of SetStorageQuotaRequest from a dict
set_storage_quota_request_from_dict = SetStorageQuotaRequest.from_dict(set_storage_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


