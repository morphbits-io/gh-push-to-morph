# V1GetUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_limit** | **int** | User&#39;s storage limit for all it&#39;s buckets in bytes. Zero value means unlimited. | 
**role** | [**UserRole**](UserRole.md) |  | 

## Example

```python
from openapi_client.models.v1_get_user_response import V1GetUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GetUserResponse from a JSON string
v1_get_user_response_instance = V1GetUserResponse.from_json(json)
# print the JSON string representation of the object
print(V1GetUserResponse.to_json())

# convert the object into a dict
v1_get_user_response_dict = v1_get_user_response_instance.to_dict()
# create an instance of V1GetUserResponse from a dict
v1_get_user_response_from_dict = V1GetUserResponse.from_dict(v1_get_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


