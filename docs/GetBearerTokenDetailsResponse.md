# GetBearerTokenDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**DetailedBearerTokenInfo**](DetailedBearerTokenInfo.md) |  | 

## Example

```python
from openapi_client.models.get_bearer_token_details_response import GetBearerTokenDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBearerTokenDetailsResponse from a JSON string
get_bearer_token_details_response_instance = GetBearerTokenDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetBearerTokenDetailsResponse.to_json())

# convert the object into a dict
get_bearer_token_details_response_dict = get_bearer_token_details_response_instance.to_dict()
# create an instance of GetBearerTokenDetailsResponse from a dict
get_bearer_token_details_response_from_dict = GetBearerTokenDetailsResponse.from_dict(get_bearer_token_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


