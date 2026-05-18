# V1ClusterListSAMLProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[SAMLProviderRecord]**](SAMLProviderRecord.md) |  | 

## Example

```python
from openapi_client.models.v1_cluster_list_saml_providers_response import V1ClusterListSAMLProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterListSAMLProvidersResponse from a JSON string
v1_cluster_list_saml_providers_response_instance = V1ClusterListSAMLProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(V1ClusterListSAMLProvidersResponse.to_json())

# convert the object into a dict
v1_cluster_list_saml_providers_response_dict = v1_cluster_list_saml_providers_response_instance.to_dict()
# create an instance of V1ClusterListSAMLProvidersResponse from a dict
v1_cluster_list_saml_providers_response_from_dict = V1ClusterListSAMLProvidersResponse.from_dict(v1_cluster_list_saml_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


