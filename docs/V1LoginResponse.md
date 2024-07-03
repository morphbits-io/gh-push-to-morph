# V1LoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Unified access token. | 
**role** | [**UserRole**](UserRole.md) |  | 

## Example

```python
from openapi_client.models.v1_login_response import V1LoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1LoginResponse from a JSON string
v1_login_response_instance = V1LoginResponse.from_json(json)
# print the JSON string representation of the object
print(V1LoginResponse.to_json())

# convert the object into a dict
v1_login_response_dict = v1_login_response_instance.to_dict()
# create an instance of V1LoginResponse from a dict
v1_login_response_from_dict = V1LoginResponse.from_dict(v1_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


