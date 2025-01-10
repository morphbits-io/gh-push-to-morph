# V1UpdateUserStoragePolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 

## Example

```python
from openapi_client.models.v1_update_user_storage_policy_request import V1UpdateUserStoragePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateUserStoragePolicyRequest from a JSON string
v1_update_user_storage_policy_request_instance = V1UpdateUserStoragePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(V1UpdateUserStoragePolicyRequest.to_json())

# convert the object into a dict
v1_update_user_storage_policy_request_dict = v1_update_user_storage_policy_request_instance.to_dict()
# create an instance of V1UpdateUserStoragePolicyRequest from a dict
v1_update_user_storage_policy_request_from_dict = V1UpdateUserStoragePolicyRequest.from_dict(v1_update_user_storage_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


