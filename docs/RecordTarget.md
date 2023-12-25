# RecordTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**List[Role]**](Role.md) | Target subject&#39;s role class. | 
**keys** | **List[str]** | List of public keys to identify target subject. | 

## Example

```python
from openapi_client.models.record_target import RecordTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RecordTarget from a JSON string
record_target_instance = RecordTarget.from_json(json)
# print the JSON string representation of the object
print RecordTarget.to_json()

# convert the object into a dict
record_target_dict = record_target_instance.to_dict()
# create an instance of RecordTarget from a dict
record_target_form_dict = record_target.from_dict(record_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


