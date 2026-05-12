# GetTimelockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_until** | **datetime** | Date until which the bucket cannot be deleted, in RFC 3339 format. Returned in UTC (with “Z”). If empty or set to a time in the past, the bucket is not locked for deletion. | 

## Example

```python
from openapi_client.models.get_timelock_response import GetTimelockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimelockResponse from a JSON string
get_timelock_response_instance = GetTimelockResponse.from_json(json)
# print the JSON string representation of the object
print(GetTimelockResponse.to_json())

# convert the object into a dict
get_timelock_response_dict = get_timelock_response_instance.to_dict()
# create an instance of GetTimelockResponse from a dict
get_timelock_response_from_dict = GetTimelockResponse.from_dict(get_timelock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


