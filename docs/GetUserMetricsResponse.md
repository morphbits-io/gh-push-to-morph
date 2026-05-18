# GetUserMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_count** | **int** | Total number of buckets owned by the user. | 
**used_space** | **int** | Used space by user in bytes. | 

## Example

```python
from openapi_client.models.get_user_metrics_response import GetUserMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserMetricsResponse from a JSON string
get_user_metrics_response_instance = GetUserMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserMetricsResponse.to_json())

# convert the object into a dict
get_user_metrics_response_dict = get_user_metrics_response_instance.to_dict()
# create an instance of GetUserMetricsResponse from a dict
get_user_metrics_response_from_dict = GetUserMetricsResponse.from_dict(get_user_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


