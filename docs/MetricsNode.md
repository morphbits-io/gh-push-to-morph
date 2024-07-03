# MetricsNode

Node metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Network endpoint of the node server. | 
**uptime** | **int** | Time elapsed since node startup in seconds. | 
**drives** | [**List[MetricsDrive]**](MetricsDrive.md) | Listing of drives&#39; metrics. | 

## Example

```python
from openapi_client.models.metrics_node import MetricsNode

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsNode from a JSON string
metrics_node_instance = MetricsNode.from_json(json)
# print the JSON string representation of the object
print(MetricsNode.to_json())

# convert the object into a dict
metrics_node_dict = metrics_node_instance.to_dict()
# create an instance of MetricsNode from a dict
metrics_node_from_dict = MetricsNode.from_dict(metrics_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


