# V1ClusterGetOAuthProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[OAuthProviderRecord]**](OAuthProviderRecord.md) |  | 

## Example

```python
from openapi_client.models.v1_cluster_get_o_auth_providers_response import V1ClusterGetOAuthProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterGetOAuthProvidersResponse from a JSON string
v1_cluster_get_o_auth_providers_response_instance = V1ClusterGetOAuthProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(V1ClusterGetOAuthProvidersResponse.to_json())

# convert the object into a dict
v1_cluster_get_o_auth_providers_response_dict = v1_cluster_get_o_auth_providers_response_instance.to_dict()
# create an instance of V1ClusterGetOAuthProvidersResponse from a dict
v1_cluster_get_o_auth_providers_response_from_dict = V1ClusterGetOAuthProvidersResponse.from_dict(v1_cluster_get_o_auth_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


