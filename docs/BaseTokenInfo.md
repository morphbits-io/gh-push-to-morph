# BaseTokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Token ID. | 
**name** | **str** | User-defined token name. | 

## Example

```python
from openapi_client.models.base_token_info import BaseTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTokenInfo from a JSON string
base_token_info_instance = BaseTokenInfo.from_json(json)
# print the JSON string representation of the object
print(BaseTokenInfo.to_json())

# convert the object into a dict
base_token_info_dict = base_token_info_instance.to_dict()
# create an instance of BaseTokenInfo from a dict
base_token_info_from_dict = BaseTokenInfo.from_dict(base_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


