# V1LoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Account login. | 
**password** | **str** | Account password. | 

## Example

```python
from openapi_client.models.v1_login_request import V1LoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1LoginRequest from a JSON string
v1_login_request_instance = V1LoginRequest.from_json(json)
# print the JSON string representation of the object
print(V1LoginRequest.to_json())

# convert the object into a dict
v1_login_request_dict = v1_login_request_instance.to_dict()
# create an instance of V1LoginRequest from a dict
v1_login_request_from_dict = V1LoginRequest.from_dict(v1_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


