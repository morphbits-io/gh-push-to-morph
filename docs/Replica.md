# Replica


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | How many object replicas to put. | 
**selector** | **str** | Named selector bucket to put replicas. | 

## Example

```python
from openapi_client.models.replica import Replica

# TODO update the JSON string below
json = "{}"
# create an instance of Replica from a JSON string
replica_instance = Replica.from_json(json)
# print the JSON string representation of the object
print Replica.to_json()

# convert the object into a dict
replica_dict = replica_instance.to_dict()
# create an instance of Replica from a dict
replica_form_dict = replica.from_dict(replica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


