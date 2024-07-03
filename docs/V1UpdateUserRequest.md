# V1UpdateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserRole**](UserRole.md) |  | 
**password** | **str** | User&#39;s new password. | 

## Example

```python
from openapi_client.models.v1_update_user_request import V1UpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateUserRequest from a JSON string
v1_update_user_request_instance = V1UpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print(V1UpdateUserRequest.to_json())

# convert the object into a dict
v1_update_user_request_dict = v1_update_user_request_instance.to_dict()
# create an instance of V1UpdateUserRequest from a dict
v1_update_user_request_from_dict = V1UpdateUserRequest.from_dict(v1_update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


