# UserManagementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | User wallet file. | 
**role** | [**UserRole**](UserRole.md) |  | 
**super_key** | **str** | Superkey wallet file. | [optional] 

## Example

```python
from openapi_client.models.user_management_request import UserManagementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserManagementRequest from a JSON string
user_management_request_instance = UserManagementRequest.from_json(json)
# print the JSON string representation of the object
print(UserManagementRequest.to_json())

# convert the object into a dict
user_management_request_dict = user_management_request_instance.to_dict()
# create an instance of UserManagementRequest from a dict
user_management_request_from_dict = UserManagementRequest.from_dict(user_management_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


