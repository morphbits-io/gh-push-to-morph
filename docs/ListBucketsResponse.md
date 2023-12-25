# ListBucketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | **List[str]** | Bucket names. | 
**used_space** | **int** | Used space by user in bytes. | 

## Example

```python
from openapi_client.models.list_buckets_response import ListBucketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBucketsResponse from a JSON string
list_buckets_response_instance = ListBucketsResponse.from_json(json)
# print the JSON string representation of the object
print ListBucketsResponse.to_json()

# convert the object into a dict
list_buckets_response_dict = list_buckets_response_instance.to_dict()
# create an instance of ListBucketsResponse from a dict
list_buckets_response_form_dict = list_buckets_response.from_dict(list_buckets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


