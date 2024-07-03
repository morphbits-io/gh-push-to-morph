# V1RegisterUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserRole**](UserRole.md) |  | 
**password** | **str** | User&#39;s password. | 

## Example

```python
from openapi_client.models.v1_register_user_request import V1RegisterUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1RegisterUserRequest from a JSON string
v1_register_user_request_instance = V1RegisterUserRequest.from_json(json)
# print the JSON string representation of the object
print(V1RegisterUserRequest.to_json())

# convert the object into a dict
v1_register_user_request_dict = v1_register_user_request_instance.to_dict()
# create an instance of V1RegisterUserRequest from a dict
v1_register_user_request_from_dict = V1RegisterUserRequest.from_dict(v1_register_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


