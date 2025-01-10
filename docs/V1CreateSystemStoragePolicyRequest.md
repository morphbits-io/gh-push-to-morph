# V1CreateSystemStoragePolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 
**name** | **str** | Policy name. Max length must be less or equal 62. | 

## Example

```python
from openapi_client.models.v1_create_system_storage_policy_request import V1CreateSystemStoragePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateSystemStoragePolicyRequest from a JSON string
v1_create_system_storage_policy_request_instance = V1CreateSystemStoragePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateSystemStoragePolicyRequest.to_json())

# convert the object into a dict
v1_create_system_storage_policy_request_dict = v1_create_system_storage_policy_request_instance.to_dict()
# create an instance of V1CreateSystemStoragePolicyRequest from a dict
v1_create_system_storage_policy_request_from_dict = V1CreateSystemStoragePolicyRequest.from_dict(v1_create_system_storage_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


