# EACLRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**List[OperationType]**](OperationType.md) | Request&#39;s operation type to match if the rule is applicable to a particular request | 
**action** | [**List[ActionType]**](ActionType.md) | Rule execution result action. | 
**filters** | [**List[RecordFilter]**](RecordFilter.md) | Filters for records. | 
**targets** | [**List[RecordTarget]**](RecordTarget.md) | Target to apply ACL rule. Can be a subject&#39;s role class or a list of public keys to match. | 

## Example

```python
from openapi_client.models.eacl_record import EACLRecord

# TODO update the JSON string below
json = "{}"
# create an instance of EACLRecord from a JSON string
eacl_record_instance = EACLRecord.from_json(json)
# print the JSON string representation of the object
print EACLRecord.to_json()

# convert the object into a dict
eacl_record_dict = eacl_record_instance.to_dict()
# create an instance of EACLRecord from a dict
eacl_record_form_dict = eacl_record.from_dict(eacl_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


