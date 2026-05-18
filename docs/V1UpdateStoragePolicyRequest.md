# V1UpdateStoragePolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 
**consistency** | [**MetadataConsistency**](MetadataConsistency.md) |  | [optional] 
**default** | **bool** | The flag indicates if the policy is the default. | [optional] 

## Example

```python
from openapi_client.models.v1_update_storage_policy_request import V1UpdateStoragePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateStoragePolicyRequest from a JSON string
v1_update_storage_policy_request_instance = V1UpdateStoragePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(V1UpdateStoragePolicyRequest.to_json())

# convert the object into a dict
v1_update_storage_policy_request_dict = v1_update_storage_policy_request_instance.to_dict()
# create an instance of V1UpdateStoragePolicyRequest from a dict
v1_update_storage_policy_request_from_dict = V1UpdateStoragePolicyRequest.from_dict(v1_update_storage_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


