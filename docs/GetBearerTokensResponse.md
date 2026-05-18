# GetBearerTokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**List[BearerTokenInfo]**](BearerTokenInfo.md) | Bearer tokens list. | 

## Example

```python
from openapi_client.models.get_bearer_tokens_response import GetBearerTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBearerTokensResponse from a JSON string
get_bearer_tokens_response_instance = GetBearerTokensResponse.from_json(json)
# print the JSON string representation of the object
print(GetBearerTokensResponse.to_json())

# convert the object into a dict
get_bearer_tokens_response_dict = get_bearer_tokens_response_instance.to_dict()
# create an instance of GetBearerTokensResponse from a dict
get_bearer_tokens_response_from_dict = GetBearerTokensResponse.from_dict(get_bearer_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


