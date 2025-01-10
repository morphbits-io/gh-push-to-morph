# CreateObjectResponse

Object successfully created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | **str** | Created object id. | 

## Example

```python
from openapi_client.models.create_object_response import CreateObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectResponse from a JSON string
create_object_response_instance = CreateObjectResponse.from_json(json)
# print the JSON string representation of the object
print(CreateObjectResponse.to_json())

# convert the object into a dict
create_object_response_dict = create_object_response_instance.to_dict()
# create an instance of CreateObjectResponse from a dict
create_object_response_from_dict = CreateObjectResponse.from_dict(create_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


