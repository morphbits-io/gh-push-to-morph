# ObjectMetadataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **datetime** | Creation date in RFC 3339 format. | 
**size** | **int** | Data size. | 
**file_name** | **str** | Name of the associated file. | 
**content_type** | **str** | Media type from https://www.iana.org/assignments/media-types/media-types.xhtml | [default to 'application/octet-stream']

## Example

```python
from openapi_client.models.object_metadata_response import ObjectMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMetadataResponse from a JSON string
object_metadata_response_instance = ObjectMetadataResponse.from_json(json)
# print the JSON string representation of the object
print ObjectMetadataResponse.to_json()

# convert the object into a dict
object_metadata_response_dict = object_metadata_response_instance.to_dict()
# create an instance of ObjectMetadataResponse from a dict
object_metadata_response_form_dict = object_metadata_response.from_dict(object_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


