# SearchObjectsRequest

List of parameters for the search request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[SearchFilter]**](SearchFilter.md) | Optional list of up to 7 object filters. If it is not specified, all objects are  returned.  Special filter keys starting with \&quot;$Object:\&quot; can be used to filter by system attributes. The expected value formats are:    \&quot;$Object:payloadLength\&quot; – payload size in bytes, as a decimal uint64 string.    \&quot;$Object:ownerID\&quot;       – object creator identifier, as a user ID string.    \&quot;$Object:payloadHash\&quot;   – SHA-256 hash of the payload, as a standard Base64-encoded                              string (decoded length must be 32 bytes).    \&quot;$Object:creationEpoch\&quot; – object creation epoch, as a decimal uint64 string.    Other keys starting from \&quot;$Object:*\&quot; lead to a 400 error.  Other keys are treated as user-defined object attributes (for example \&quot;FilePath\&quot;).  | [optional] 
**attributes** | **List[str]** | Optional list of attributes to be returned for each object. It must contain up to 7  attributes.   Basic object metadata can be retrieved by requesting the attributes:  \&quot;FilePath\&quot;, \&quot;Content-Type\&quot;, \&quot;Timestamp\&quot; as the creation date, and \&quot;ExpHours\&quot; as the  object expiration time. You also may request reserved attributes:  \&quot;$Object:payloadLength\&quot;, \&quot;$Object:ownerID\&quot;, \&quot;$Object:payloadHash\&quot;, \&quot;$Object:creationEpoch\&quot;. However, any other values starting from \&quot;$Object:*\&quot; will result in a 400 error.  If this parameter is empty, no attributes will be returned, only object IDs.  | [optional] 

## Example

```python
from openapi_client.models.search_objects_request import SearchObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchObjectsRequest from a JSON string
search_objects_request_instance = SearchObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(SearchObjectsRequest.to_json())

# convert the object into a dict
search_objects_request_dict = search_objects_request_instance.to_dict()
# create an instance of SearchObjectsRequest from a dict
search_objects_request_from_dict = SearchObjectsRequest.from_dict(search_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


