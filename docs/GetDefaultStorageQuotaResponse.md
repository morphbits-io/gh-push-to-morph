# GetDefaultStorageQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quota** | **int** | Default storage quota for users in bytes. | 

## Example

```python
from openapi_client.models.get_default_storage_quota_response import GetDefaultStorageQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDefaultStorageQuotaResponse from a JSON string
get_default_storage_quota_response_instance = GetDefaultStorageQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(GetDefaultStorageQuotaResponse.to_json())

# convert the object into a dict
get_default_storage_quota_response_dict = get_default_storage_quota_response_instance.to_dict()
# create an instance of GetDefaultStorageQuotaResponse from a dict
get_default_storage_quota_response_from_dict = GetDefaultStorageQuotaResponse.from_dict(get_default_storage_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


