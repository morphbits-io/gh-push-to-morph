# StoragePolicy

Set of rules to select a subset of nodes from `NetworkMap` able to store bucket's objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | [**List[Replica]**](Replica.md) | Rules to set number of object replicas and place each one into a named bucket. MUST NOT be empty. | 
**placement_factor** | **int** | Bucket placement factor defines the maximum number of storage nodes (replicas×factor) that will store bucket data. | 
**selectors** | [**List[Selector]**](Selector.md) | Set of Selectors to form the bucket&#39;s nodes subset. | 
**filters** | [**List[PlacementFilter]**](PlacementFilter.md) | List of named filters to reference in selectors. | 

## Example

```python
from openapi_client.models.storage_policy import StoragePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePolicy from a JSON string
storage_policy_instance = StoragePolicy.from_json(json)
# print the JSON string representation of the object
print(StoragePolicy.to_json())

# convert the object into a dict
storage_policy_dict = storage_policy_instance.to_dict()
# create an instance of StoragePolicy from a dict
storage_policy_from_dict = StoragePolicy.from_dict(storage_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


