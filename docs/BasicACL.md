# BasicACL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final** | **bool** | Flag denying Extended ACL. | 
**sticky** | **bool** | Flag denying different owners of the request and the object. | 
**owner** | [**ACLGroup**](ACLGroup.md) |  | 
**others** | [**ACLGroup**](ACLGroup.md) |  | 

## Example

```python
from openapi_client.models.basic_acl import BasicACL

# TODO update the JSON string below
json = "{}"
# create an instance of BasicACL from a JSON string
basic_acl_instance = BasicACL.from_json(json)
# print the JSON string representation of the object
print(BasicACL.to_json())

# convert the object into a dict
basic_acl_dict = basic_acl_instance.to_dict()
# create an instance of BasicACL from a dict
basic_acl_from_dict = BasicACL.from_dict(basic_acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


