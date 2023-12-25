# MetricsDrive

Drive metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_point** | **str** | Mount point of the physical drive. | 
**total_space** | **int** | Total disk space of the node in bytes. | 
**used_space** | **int** | Total disk space used on the node in bytes. | 
**avail_space** | **int** | Available disk space on the node in bytes. | 

## Example

```python
from openapi_client.models.metrics_drive import MetricsDrive

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsDrive from a JSON string
metrics_drive_instance = MetricsDrive.from_json(json)
# print the JSON string representation of the object
print MetricsDrive.to_json()

# convert the object into a dict
metrics_drive_dict = metrics_drive_instance.to_dict()
# create an instance of MetricsDrive from a dict
metrics_drive_form_dict = metrics_drive.from_dict(metrics_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


