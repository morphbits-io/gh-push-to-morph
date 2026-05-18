# OAuthProviderRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | **str** |  | 
**type** | [**OAuthProviderType**](OAuthProviderType.md) |  | 

## Example

```python
from openapi_client.models.o_auth_provider_record import OAuthProviderRecord

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProviderRecord from a JSON string
o_auth_provider_record_instance = OAuthProviderRecord.from_json(json)
# print the JSON string representation of the object
print(OAuthProviderRecord.to_json())

# convert the object into a dict
o_auth_provider_record_dict = o_auth_provider_record_instance.to_dict()
# create an instance of OAuthProviderRecord from a dict
o_auth_provider_record_from_dict = OAuthProviderRecord.from_dict(o_auth_provider_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


