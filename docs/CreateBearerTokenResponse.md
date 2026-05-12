# CreateBearerTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Bearer token. | 

## Example

```python
from openapi_client.models.create_bearer_token_response import CreateBearerTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBearerTokenResponse from a JSON string
create_bearer_token_response_instance = CreateBearerTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBearerTokenResponse.to_json())

# convert the object into a dict
create_bearer_token_response_dict = create_bearer_token_response_instance.to_dict()
# create an instance of CreateBearerTokenResponse from a dict
create_bearer_token_response_from_dict = CreateBearerTokenResponse.from_dict(create_bearer_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


