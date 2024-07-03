# UserChangeStorageQuotaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | New user storage quota size in bytes. | 

## Example

```python
from openapi_client.models.user_change_storage_quota_request import UserChangeStorageQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserChangeStorageQuotaRequest from a JSON string
user_change_storage_quota_request_instance = UserChangeStorageQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(UserChangeStorageQuotaRequest.to_json())

# convert the object into a dict
user_change_storage_quota_request_dict = user_change_storage_quota_request_instance.to_dict()
# create an instance of UserChangeStorageQuotaRequest from a dict
user_change_storage_quota_request_from_dict = UserChangeStorageQuotaRequest.from_dict(user_change_storage_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


