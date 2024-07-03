# SetDefaultStorageQuotaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quota** | **int** | Default storage quota for users in bytes. | 

## Example

```python
from openapi_client.models.set_default_storage_quota_request import SetDefaultStorageQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultStorageQuotaRequest from a JSON string
set_default_storage_quota_request_instance = SetDefaultStorageQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(SetDefaultStorageQuotaRequest.to_json())

# convert the object into a dict
set_default_storage_quota_request_dict = set_default_storage_quota_request_instance.to_dict()
# create an instance of SetDefaultStorageQuotaRequest from a dict
set_default_storage_quota_request_from_dict = SetDefaultStorageQuotaRequest.from_dict(set_default_storage_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


