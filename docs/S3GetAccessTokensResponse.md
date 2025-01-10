# S3GetAccessTokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**List[S3TokenInfo]**](S3TokenInfo.md) | Tokens list. | 

## Example

```python
from openapi_client.models.s3_get_access_tokens_response import S3GetAccessTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of S3GetAccessTokensResponse from a JSON string
s3_get_access_tokens_response_instance = S3GetAccessTokensResponse.from_json(json)
# print the JSON string representation of the object
print(S3GetAccessTokensResponse.to_json())

# convert the object into a dict
s3_get_access_tokens_response_dict = s3_get_access_tokens_response_instance.to_dict()
# create an instance of S3GetAccessTokensResponse from a dict
s3_get_access_tokens_response_from_dict = S3GetAccessTokensResponse.from_dict(s3_get_access_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


