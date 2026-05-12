# ECRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **str** | Name of the corresponding selector to put EC data. | [optional] 
**data_parts** | **int** | Number of data parts. The dataParts value of sum of dataParts+parityParts can&#39;t be greater 64. | 
**parity_parts** | **int** | Number of parity pats. The parityParts value of sum of dataParts+parityParts can&#39;t be greater 64. | 

## Example

```python
from openapi_client.models.ec_rule import ECRule

# TODO update the JSON string below
json = "{}"
# create an instance of ECRule from a JSON string
ec_rule_instance = ECRule.from_json(json)
# print the JSON string representation of the object
print(ECRule.to_json())

# convert the object into a dict
ec_rule_dict = ec_rule_instance.to_dict()
# create an instance of ECRule from a dict
ec_rule_from_dict = ECRule.from_dict(ec_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


