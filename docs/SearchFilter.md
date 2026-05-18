# SearchFilter

Filter used to match object attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Name of the attribute to apply the filter to (for example, \&quot;FilePath\&quot;, \&quot;Content-Type\&quot;, or a user-defined attribute key). | 
**value** | **str** | Numeric filters (MatchNum*) decimal values within the supported 256-bit integer range [-(2^256 - 1), 2^256 - 1]. | 
**match** | [**SearchMatch**](SearchMatch.md) |  | 

## Example

```python
from openapi_client.models.search_filter import SearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilter from a JSON string
search_filter_instance = SearchFilter.from_json(json)
# print the JSON string representation of the object
print(SearchFilter.to_json())

# convert the object into a dict
search_filter_dict = search_filter_instance.to_dict()
# create an instance of SearchFilter from a dict
search_filter_from_dict = SearchFilter.from_dict(search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


