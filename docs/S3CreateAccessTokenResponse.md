# S3CreateAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | AWS access key ID. | 
**secret_access_key** | **str** | AWS secret access Key. | 

## Example

```python
from openapi_client.models.s3_create_access_token_response import S3CreateAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of S3CreateAccessTokenResponse from a JSON string
s3_create_access_token_response_instance = S3CreateAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(S3CreateAccessTokenResponse.to_json())

# convert the object into a dict
s3_create_access_token_response_dict = s3_create_access_token_response_instance.to_dict()
# create an instance of S3CreateAccessTokenResponse from a dict
s3_create_access_token_response_from_dict = S3CreateAccessTokenResponse.from_dict(s3_create_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


