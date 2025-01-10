# S3TokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Token ID. | 
**name** | **str** | User-defined token name | 

## Example

```python
from openapi_client.models.s3_token_info import S3TokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of S3TokenInfo from a JSON string
s3_token_info_instance = S3TokenInfo.from_json(json)
# print the JSON string representation of the object
print(S3TokenInfo.to_json())

# convert the object into a dict
s3_token_info_dict = s3_token_info_instance.to_dict()
# create an instance of S3TokenInfo from a dict
s3_token_info_from_dict = S3TokenInfo.from_dict(s3_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


