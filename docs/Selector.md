# Selector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Selector name to reference in object placement section. | 
**count** | **int** | How many nodes to select from the bucket. | 
**attribute** | **str** | Bucket attribute to select from. | 
**filter** | **str** | Filter reference to select from. | 
**clause** | [**List[Clause]**](Clause.md) | Selector modifier showing how to form a bucket. | 

## Example

```python
from openapi_client.models.selector import Selector

# TODO update the JSON string below
json = "{}"
# create an instance of Selector from a JSON string
selector_instance = Selector.from_json(json)
# print the JSON string representation of the object
print Selector.to_json()

# convert the object into a dict
selector_dict = selector_instance.to_dict()
# create an instance of Selector from a dict
selector_form_dict = selector.from_dict(selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


