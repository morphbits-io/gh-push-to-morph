# V1GetUserStoragePolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 

## Example

```python
from openapi_client.models.v1_get_user_storage_policy_response import V1GetUserStoragePolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GetUserStoragePolicyResponse from a JSON string
v1_get_user_storage_policy_response_instance = V1GetUserStoragePolicyResponse.from_json(json)
# print the JSON string representation of the object
print(V1GetUserStoragePolicyResponse.to_json())

# convert the object into a dict
v1_get_user_storage_policy_response_dict = v1_get_user_storage_policy_response_instance.to_dict()
# create an instance of V1GetUserStoragePolicyResponse from a dict
v1_get_user_storage_policy_response_from_dict = V1GetUserStoragePolicyResponse.from_dict(v1_get_user_storage_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


