# RecordFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_type** | [**List[HeaderType]**](HeaderType.md) | Define if Object or Request header will be used. | 
**match_type** | [**List[MatchType]**](MatchType.md) | Match operation type. | 
**key** | **str** | Name of the Header to use. | 
**value** | **str** | Expected Header Value or pattern to match. | 

## Example

```python
from openapi_client.models.record_filter import RecordFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RecordFilter from a JSON string
record_filter_instance = RecordFilter.from_json(json)
# print the JSON string representation of the object
print RecordFilter.to_json()

# convert the object into a dict
record_filter_dict = record_filter_instance.to_dict()
# create an instance of RecordFilter from a dict
record_filter_form_dict = record_filter.from_dict(record_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


