# V1GetUserStoragePoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[NamedStoragePolicy]**](NamedStoragePolicy.md) | Storage policy list. | 

## Example

```python
from openapi_client.models.v1_get_user_storage_policies_response import V1GetUserStoragePoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GetUserStoragePoliciesResponse from a JSON string
v1_get_user_storage_policies_response_instance = V1GetUserStoragePoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(V1GetUserStoragePoliciesResponse.to_json())

# convert the object into a dict
v1_get_user_storage_policies_response_dict = v1_get_user_storage_policies_response_instance.to_dict()
# create an instance of V1GetUserStoragePoliciesResponse from a dict
v1_get_user_storage_policies_response_from_dict = V1GetUserStoragePoliciesResponse.from_dict(v1_get_user_storage_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


