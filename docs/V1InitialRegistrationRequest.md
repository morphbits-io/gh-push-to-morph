# V1InitialRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Account login. | 
**password** | **str** | Account password. | 

## Example

```python
from openapi_client.models.v1_initial_registration_request import V1InitialRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1InitialRegistrationRequest from a JSON string
v1_initial_registration_request_instance = V1InitialRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(V1InitialRegistrationRequest.to_json())

# convert the object into a dict
v1_initial_registration_request_dict = v1_initial_registration_request_instance.to_dict()
# create an instance of V1InitialRegistrationRequest from a dict
v1_initial_registration_request_from_dict = V1InitialRegistrationRequest.from_dict(v1_initial_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


