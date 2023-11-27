# PlacementFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the filter or a reference to a named filter. &#39;*&#39; means application to the whole unfiltered NetworkMap. At top level it&#39;s used as a filter name. At lower levels it&#39;s considered to be a reference to another named filter. | 
**key** | **str** | Key to filter. | 
**op** | [**List[Operation]**](Operation.md) | Filtering operation. | 
**value** | **str** | Value to match. | 
**filters** | [**List[PlacementFilter]**](PlacementFilter.md) |  | 

## Example

```python
from openapi_client.models.placement_filter import PlacementFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementFilter from a JSON string
placement_filter_instance = PlacementFilter.from_json(json)
# print the JSON string representation of the object
print PlacementFilter.to_json()

# convert the object into a dict
placement_filter_dict = placement_filter_instance.to_dict()
# create an instance of PlacementFilter from a dict
placement_filter_form_dict = placement_filter.from_dict(placement_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


