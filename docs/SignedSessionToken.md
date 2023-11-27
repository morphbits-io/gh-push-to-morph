# SignedSessionToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | This payload should be signed by client. | 
**verb** | [**SessionVerb**](SessionVerb.md) |  | 
**signature** | **str** | Signature for the payload. | 

## Example

```python
from openapi_client.models.signed_session_token import SignedSessionToken

# TODO update the JSON string below
json = "{}"
# create an instance of SignedSessionToken from a JSON string
signed_session_token_instance = SignedSessionToken.from_json(json)
# print the JSON string representation of the object
print SignedSessionToken.to_json()

# convert the object into a dict
signed_session_token_dict = signed_session_token_instance.to_dict()
# create an instance of SignedSessionToken from a dict
signed_session_token_form_dict = signed_session_token.from_dict(signed_session_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


