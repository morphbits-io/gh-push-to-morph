# GetUserListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) | Users list. | 

## Example

```python
from openapi_client.models.get_user_list_response import GetUserListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserListResponse from a JSON string
get_user_list_response_instance = GetUserListResponse.from_json(json)
# print the JSON string representation of the object
print GetUserListResponse.to_json()

# convert the object into a dict
get_user_list_response_dict = get_user_list_response_instance.to_dict()
# create an instance of GetUserListResponse from a dict
get_user_list_response_form_dict = get_user_list_response.from_dict(get_user_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


