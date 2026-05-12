# SearchObjects

Requested object information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** |  | 
**attributes** | **Dict[str, object]** | Requested attributes. The first filter key will also be added as an additional attribute in the response, if that attribute wasn&#39;t explicitly requested. | 

## Example

```python
from openapi_client.models.search_objects import SearchObjects

# TODO update the JSON string below
json = "{}"
# create an instance of SearchObjects from a JSON string
search_objects_instance = SearchObjects.from_json(json)
# print the JSON string representation of the object
print(SearchObjects.to_json())

# convert the object into a dict
search_objects_dict = search_objects_instance.to_dict()
# create an instance of SearchObjects from a dict
search_objects_from_dict = SearchObjects.from_dict(search_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


