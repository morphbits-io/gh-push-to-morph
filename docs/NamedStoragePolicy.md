# NamedStoragePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StoragePolicy**](StoragePolicy.md) |  | 
**name** | **str** | Policy name. Max combined length userName+policyName must be less or equal 62. | 

## Example

```python
from openapi_client.models.named_storage_policy import NamedStoragePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of NamedStoragePolicy from a JSON string
named_storage_policy_instance = NamedStoragePolicy.from_json(json)
# print the JSON string representation of the object
print(NamedStoragePolicy.to_json())

# convert the object into a dict
named_storage_policy_dict = named_storage_policy_instance.to_dict()
# create an instance of NamedStoragePolicy from a dict
named_storage_policy_from_dict = NamedStoragePolicy.from_dict(named_storage_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


