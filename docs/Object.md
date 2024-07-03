# Object

Object descriptor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Object name. | 
**creation_date** | **datetime** | Creation date in RFC 3339 format. | 
**size** | **int** | Data size. | 
**content_type** | **str** | Media type from https://www.iana.org/assignments/media-types/media-types.xhtml | [default to 'application/octet-stream']
**lifetime** | **int** | Object lifetime in hours, since object creation time. Zero means no expiration. | [default to 0]

## Example

```python
from openapi_client.models.object import Object

# TODO update the JSON string below
json = "{}"
# create an instance of Object from a JSON string
object_instance = Object.from_json(json)
# print the JSON string representation of the object
print(Object.to_json())

# convert the object into a dict
object_dict = object_instance.to_dict()
# create an instance of Object from a dict
object_from_dict = Object.from_dict(object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


