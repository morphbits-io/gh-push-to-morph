# UserManagementDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_key** | **str** | Superkey wallet file. It should be passed to the request only in case of admin removing. | [optional] 

## Example

```python
from openapi_client.models.user_management_delete_request import UserManagementDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserManagementDeleteRequest from a JSON string
user_management_delete_request_instance = UserManagementDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(UserManagementDeleteRequest.to_json())

# convert the object into a dict
user_management_delete_request_dict = user_management_delete_request_instance.to_dict()
# create an instance of UserManagementDeleteRequest from a dict
user_management_delete_request_from_dict = UserManagementDeleteRequest.from_dict(user_management_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


