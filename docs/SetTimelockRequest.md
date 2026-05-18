# SetTimelockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_until** | **datetime** | Date until which the bucket cannot be deleted, in RFC 3339 format. This period can be extended, but there is no way to make it expire earlier. | 

## Example

```python
from openapi_client.models.set_timelock_request import SetTimelockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTimelockRequest from a JSON string
set_timelock_request_instance = SetTimelockRequest.from_json(json)
# print the JSON string representation of the object
print(SetTimelockRequest.to_json())

# convert the object into a dict
set_timelock_request_dict = set_timelock_request_instance.to_dict()
# create an instance of SetTimelockRequest from a dict
set_timelock_request_from_dict = SetTimelockRequest.from_dict(set_timelock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


