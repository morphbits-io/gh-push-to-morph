# SearchObjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[SearchObjects]**](SearchObjects.md) |  | 
**cursor** | **str** | Value to start the next batch from. Omitted if the result fits in a single batch or it&#39;s the last pack. | [optional] 
**incomplete** | **bool** | Present if true and omitted if false. It indicates an incomplete success. The search was performed, but not all nodes returned results, so some items may be missing. | [optional] 

## Example

```python
from openapi_client.models.search_objects_response import SearchObjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchObjectsResponse from a JSON string
search_objects_response_instance = SearchObjectsResponse.from_json(json)
# print the JSON string representation of the object
print(SearchObjectsResponse.to_json())

# convert the object into a dict
search_objects_response_dict = search_objects_response_instance.to_dict()
# create an instance of SearchObjectsResponse from a dict
search_objects_response_from_dict = SearchObjectsResponse.from_dict(search_objects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


