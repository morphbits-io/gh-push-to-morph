# PlacementPolicy

Set of rules to select a subset of nodes from `NetworkMap` able to store container's objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | [**List[Replica]**](Replica.md) | Rules to set number of object replicas and place each one into a named bucket. MUST NOT be empty. | 
**container_backup_factor** | **int** | Container backup factor controls how deep NeoFS will search for nodes alternatives to include into container&#39;s nodes subset. | 
**selectors** | [**List[Selector]**](Selector.md) | Set of Selectors to form the container&#39;s nodes subset. | 
**filters** | [**List[PlacementFilter]**](PlacementFilter.md) | List of named filters to reference in selectors. | 

## Example

```python
from openapi_client.models.placement_policy import PlacementPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementPolicy from a JSON string
placement_policy_instance = PlacementPolicy.from_json(json)
# print the JSON string representation of the object
print(PlacementPolicy.to_json())

# convert the object into a dict
placement_policy_dict = placement_policy_instance.to_dict()
# create an instance of PlacementPolicy from a dict
placement_policy_from_dict = PlacementPolicy.from_dict(placement_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


