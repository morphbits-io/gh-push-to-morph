# LicenseResponse

License metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_limit** | **int** | Limit of node count. | 
**capacity** | **int** | Capacity in GB. | 
**valid_from** | **datetime** | License valid-from date in RFC 3339 format. | 
**valid_until** | **datetime** | License valid-until date in RFC 3339 format. | 

## Example

```python
from openapi_client.models.license_response import LicenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseResponse from a JSON string
license_response_instance = LicenseResponse.from_json(json)
# print the JSON string representation of the object
print(LicenseResponse.to_json())

# convert the object into a dict
license_response_dict = license_response_instance.to_dict()
# create an instance of LicenseResponse from a dict
license_response_from_dict = LicenseResponse.from_dict(license_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


