# CreateNamespaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Namespace name must be 1 to 31 characters long, start with a lowercase letter, contain only lowercase letters, digits, and hyphens, and not end with a hyphen. | 
**description** | **str** | Optional human-readable namespace description. Intended to explain the namespace purpose. Maximum 256 UTF-8 bytes. | [optional] 

## Example

```python
from openapi_client.models.create_namespace_request import CreateNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNamespaceRequest from a JSON string
create_namespace_request_instance = CreateNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNamespaceRequest.to_json())

# convert the object into a dict
create_namespace_request_dict = create_namespace_request_instance.to_dict()
# create an instance of CreateNamespaceRequest from a dict
create_namespace_request_from_dict = CreateNamespaceRequest.from_dict(create_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


