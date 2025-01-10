# V1CreateUserStoragePolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 
**name** | **str** | Policy name. Max policyName length must be less or equal 42. | 

## Example

```python
from openapi_client.models.v1_create_user_storage_policy_request import V1CreateUserStoragePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateUserStoragePolicyRequest from a JSON string
v1_create_user_storage_policy_request_instance = V1CreateUserStoragePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateUserStoragePolicyRequest.to_json())

# convert the object into a dict
v1_create_user_storage_policy_request_dict = v1_create_user_storage_policy_request_instance.to_dict()
# create an instance of V1CreateUserStoragePolicyRequest from a dict
v1_create_user_storage_policy_request_from_dict = V1CreateUserStoragePolicyRequest.from_dict(v1_create_user_storage_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


