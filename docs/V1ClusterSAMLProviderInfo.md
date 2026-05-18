# V1ClusterSAMLProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for login button. | 
**entity_id** | **str** | Service Provider entity id. | 
**idp_metadata** | **str** | Identity provider (idp) metadata encoded in base64. | 
**root_url** | **str** | It is a root URL for the service provider | 
**metadata_path** | **str** | Metadata path. It is used to get Service Provider metadata. | 
**acs_path** | **str** | Assertion Consumer Service URL receives the SAML response. | 
**slo_path** | **str** | Logout path. | [optional] 
**domains** | **List[str]** | Whitelisted domains. Users from these domains allowed to login. | [optional] 

## Example

```python
from openapi_client.models.v1_cluster_saml_provider_info import V1ClusterSAMLProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterSAMLProviderInfo from a JSON string
v1_cluster_saml_provider_info_instance = V1ClusterSAMLProviderInfo.from_json(json)
# print the JSON string representation of the object
print(V1ClusterSAMLProviderInfo.to_json())

# convert the object into a dict
v1_cluster_saml_provider_info_dict = v1_cluster_saml_provider_info_instance.to_dict()
# create an instance of V1ClusterSAMLProviderInfo from a dict
v1_cluster_saml_provider_info_from_dict = V1ClusterSAMLProviderInfo.from_dict(v1_cluster_saml_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


