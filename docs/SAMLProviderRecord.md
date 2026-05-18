# SAMLProviderRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | **str** |  | 

## Example

```python
from openapi_client.models.saml_provider_record import SAMLProviderRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLProviderRecord from a JSON string
saml_provider_record_instance = SAMLProviderRecord.from_json(json)
# print the JSON string representation of the object
print(SAMLProviderRecord.to_json())

# convert the object into a dict
saml_provider_record_dict = saml_provider_record_instance.to_dict()
# create an instance of SAMLProviderRecord from a dict
saml_provider_record_from_dict = SAMLProviderRecord.from_dict(saml_provider_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


