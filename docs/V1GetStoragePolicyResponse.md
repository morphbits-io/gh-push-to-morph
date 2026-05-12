# V1GetStoragePolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 
**consistency** | [**MetadataConsistency**](MetadataConsistency.md) |  | [optional] 
**default** | **bool** | The flag indicates if the policy is the default. | [optional] 

## Example

```python
from openapi_client.models.v1_get_storage_policy_response import V1GetStoragePolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GetStoragePolicyResponse from a JSON string
v1_get_storage_policy_response_instance = V1GetStoragePolicyResponse.from_json(json)
# print the JSON string representation of the object
print(V1GetStoragePolicyResponse.to_json())

# convert the object into a dict
v1_get_storage_policy_response_dict = v1_get_storage_policy_response_instance.to_dict()
# create an instance of V1GetStoragePolicyResponse from a dict
v1_get_storage_policy_response_from_dict = V1GetStoragePolicyResponse.from_dict(v1_get_storage_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


