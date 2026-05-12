# GetStorageQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**soft_quota** | **int** | Default storage soft quota for users in bytes. | 
**hard_quota** | **int** | Default storage hard quota for users in bytes. | 

## Example

```python
from openapi_client.models.get_storage_quota_response import GetStorageQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStorageQuotaResponse from a JSON string
get_storage_quota_response_instance = GetStorageQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(GetStorageQuotaResponse.to_json())

# convert the object into a dict
get_storage_quota_response_dict = get_storage_quota_response_instance.to_dict()
# create an instance of GetStorageQuotaResponse from a dict
get_storage_quota_response_from_dict = GetStorageQuotaResponse.from_dict(get_storage_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


