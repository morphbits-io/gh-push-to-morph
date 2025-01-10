# V1GetSystemStoragePoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[NamedStoragePolicy]**](NamedStoragePolicy.md) | Storage policy list. | 

## Example

```python
from openapi_client.models.v1_get_system_storage_policies_response import V1GetSystemStoragePoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GetSystemStoragePoliciesResponse from a JSON string
v1_get_system_storage_policies_response_instance = V1GetSystemStoragePoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(V1GetSystemStoragePoliciesResponse.to_json())

# convert the object into a dict
v1_get_system_storage_policies_response_dict = v1_get_system_storage_policies_response_instance.to_dict()
# create an instance of V1GetSystemStoragePoliciesResponse from a dict
v1_get_system_storage_policies_response_from_dict = V1GetSystemStoragePoliciesResponse.from_dict(v1_get_system_storage_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


