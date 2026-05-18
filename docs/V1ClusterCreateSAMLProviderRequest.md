# V1ClusterCreateSAMLProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for login button. | 
**entity_id** | **str** | Service Provider entity id. | 
**idp_metadata** | **str** | Identity provider (idp) metadata encoded in base64. | 
**root_url** | **str** | It is a root URL for the service provider | 
**domains** | **List[str]** | Whitelisted domains. Users from these domains allowed to login. | [optional] 

## Example

```python
from openapi_client.models.v1_cluster_create_saml_provider_request import V1ClusterCreateSAMLProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterCreateSAMLProviderRequest from a JSON string
v1_cluster_create_saml_provider_request_instance = V1ClusterCreateSAMLProviderRequest.from_json(json)
# print the JSON string representation of the object
print(V1ClusterCreateSAMLProviderRequest.to_json())

# convert the object into a dict
v1_cluster_create_saml_provider_request_dict = v1_cluster_create_saml_provider_request_instance.to_dict()
# create an instance of V1ClusterCreateSAMLProviderRequest from a dict
v1_cluster_create_saml_provider_request_from_dict = V1ClusterCreateSAMLProviderRequest.from_dict(v1_cluster_create_saml_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


