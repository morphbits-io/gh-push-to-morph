# GetNamespaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Namespace name. | 
**description** | **str** | Optional human-readable namespace description. Intended to explain the namespace purpose. Maximum 256 UTF-8 bytes. | [optional] 

## Example

```python
from openapi_client.models.get_namespace_response import GetNamespaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNamespaceResponse from a JSON string
get_namespace_response_instance = GetNamespaceResponse.from_json(json)
# print the JSON string representation of the object
print(GetNamespaceResponse.to_json())

# convert the object into a dict
get_namespace_response_dict = get_namespace_response_instance.to_dict()
# create an instance of GetNamespaceResponse from a dict
get_namespace_response_from_dict = GetNamespaceResponse.from_dict(get_namespace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


