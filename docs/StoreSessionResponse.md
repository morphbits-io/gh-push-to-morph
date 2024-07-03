# StoreSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The access token for the user. It should be used to interact with object operations. | 

## Example

```python
from openapi_client.models.store_session_response import StoreSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreSessionResponse from a JSON string
store_session_response_instance = StoreSessionResponse.from_json(json)
# print the JSON string representation of the object
print(StoreSessionResponse.to_json())

# convert the object into a dict
store_session_response_dict = store_session_response_instance.to_dict()
# create an instance of StoreSessionResponse from a dict
store_session_response_from_dict = StoreSessionResponse.from_dict(store_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


