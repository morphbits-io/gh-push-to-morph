# S3GetAccessTokenDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**S3DetailedTokenInfo**](S3DetailedTokenInfo.md) |  | 

## Example

```python
from openapi_client.models.s3_get_access_token_details_response import S3GetAccessTokenDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of S3GetAccessTokenDetailsResponse from a JSON string
s3_get_access_token_details_response_instance = S3GetAccessTokenDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(S3GetAccessTokenDetailsResponse.to_json())

# convert the object into a dict
s3_get_access_token_details_response_dict = s3_get_access_token_details_response_instance.to_dict()
# create an instance of S3GetAccessTokenDetailsResponse from a dict
s3_get_access_token_details_response_from_dict = S3GetAccessTokenDetailsResponse.from_dict(s3_get_access_token_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


