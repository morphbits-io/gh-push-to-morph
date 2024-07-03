# StorageNodeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Storage node address. | 

## Example

```python
from openapi_client.models.storage_node_address import StorageNodeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of StorageNodeAddress from a JSON string
storage_node_address_instance = StorageNodeAddress.from_json(json)
# print the JSON string representation of the object
print(StorageNodeAddress.to_json())

# convert the object into a dict
storage_node_address_dict = storage_node_address_instance.to_dict()
# create an instance of StorageNodeAddress from a dict
storage_node_address_from_dict = StorageNodeAddress.from_dict(storage_node_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


