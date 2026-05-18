# V1ClusterCreateOAuthProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for login button. | 
**type** | [**OAuthProviderType**](OAuthProviderType.md) |  | 
**client_id** | **str** | OAuth provider application client id. | 
**client_secret** | **str** | OAuth provider application client secret. | 
**user_info_url** | **str** | OAuth provider URL, to get user details. | 
**authorize_url** | **str** | OAuth provider URL, to authorize user. | 
**token_url** | **str** | OAuth provider URL, to exchange token. | 
**scope** | **List[str]** | OAuth provider scope required to get user&#39;s email. | 
**authorize_header_prefix** | **str** | OAuth provider Authorization header. It is used to get user&#39;s info from OAuth provider. | [default to 'OAuth']
**email_path** | **List[str]** | The path to extract email field from user info response. | 
**domains** | **List[str]** | Whitelisted domains. Users from these domains allowed to login. | 
**use_pkce** | **bool** | Tells to use PKCE feature with OAuth provider. The feature must be supported by provider. | [default to False]
**callback_url** | **str** | The OAuth provider redirects users to this URL after authorization. It must exactly match the one configured in your OAuth provider’s dashboard. | 

## Example

```python
from openapi_client.models.v1_cluster_create_o_auth_provider_request import V1ClusterCreateOAuthProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterCreateOAuthProviderRequest from a JSON string
v1_cluster_create_o_auth_provider_request_instance = V1ClusterCreateOAuthProviderRequest.from_json(json)
# print the JSON string representation of the object
print(V1ClusterCreateOAuthProviderRequest.to_json())

# convert the object into a dict
v1_cluster_create_o_auth_provider_request_dict = v1_cluster_create_o_auth_provider_request_instance.to_dict()
# create an instance of V1ClusterCreateOAuthProviderRequest from a dict
v1_cluster_create_o_auth_provider_request_from_dict = V1ClusterCreateOAuthProviderRequest.from_dict(v1_cluster_create_o_auth_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


