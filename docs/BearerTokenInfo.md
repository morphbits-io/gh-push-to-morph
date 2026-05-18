# BearerTokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Token ID. | 
**name** | **str** | User-defined token name. | 
**type** | [**TokenType**](TokenType.md) | Token type. | [optional] 

## Example

```python
from openapi_client.models.bearer_token_info import BearerTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BearerTokenInfo from a JSON string
bearer_token_info_instance = BearerTokenInfo.from_json(json)
# print the JSON string representation of the object
print(BearerTokenInfo.to_json())

# convert the object into a dict
bearer_token_info_dict = bearer_token_info_instance.to_dict()
# create an instance of BearerTokenInfo from a dict
bearer_token_info_from_dict = BearerTokenInfo.from_dict(bearer_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


