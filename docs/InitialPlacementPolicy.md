# InitialPlacementPolicy

Controls how objects are placed initially before the full policy is applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replica_limits** | **List[int]** | Sets replica counts for each REP and EC rule. If used with maxReplicas sets the maximum number of replicas for each rule. | [optional] 
**max_replicas** | **int** | Sets max number of object replicas and EC partitions. Zero value means following &#x60;replicaLimits&#x60; with no additional constraint for overall replica count. | [optional] 
**prefer_local** | **bool** | Indicates preference for local (as per node processing the request) storage placement. | [optional] 

## Example

```python
from openapi_client.models.initial_placement_policy import InitialPlacementPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of InitialPlacementPolicy from a JSON string
initial_placement_policy_instance = InitialPlacementPolicy.from_json(json)
# print the JSON string representation of the object
print(InitialPlacementPolicy.to_json())

# convert the object into a dict
initial_placement_policy_dict = initial_placement_policy_instance.to_dict()
# create an instance of InitialPlacementPolicy from a dict
initial_placement_policy_from_dict = InitialPlacementPolicy.from_dict(initial_placement_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


