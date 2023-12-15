# ACLGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_content** | **bool** | Flag allows to read object payload. Requires ReadHeaders flag. | 
**read_headers** | **bool** | Flag allows to read headers without object payload. | 
**create** | **bool** | Flag allows to create new objects. | 
**delete** | **bool** | Flag allow to delete objects. Requires Create and ReadHeaders flags. | 

## Example

```python
from openapi_client.models.acl_group import ACLGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ACLGroup from a JSON string
acl_group_instance = ACLGroup.from_json(json)
# print the JSON string representation of the object
print ACLGroup.to_json()

# convert the object into a dict
acl_group_dict = acl_group_instance.to_dict()
# create an instance of ACLGroup from a dict
acl_group_form_dict = acl_group.from_dict(acl_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


