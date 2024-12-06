# gocardless_bankaccountdata.RequisitionsApi

All URIs are relative to *https://bankaccountdata.gocardless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_requisition**](RequisitionsApi.md#create_requisition) | **POST** /api/v2/requisitions/ | 
[**delete_requisition_by_id**](RequisitionsApi.md#delete_requisition_by_id) | **DELETE** /api/v2/requisitions/{id}/ | 
[**requisition_by_id**](RequisitionsApi.md#requisition_by_id) | **GET** /api/v2/requisitions/{id}/ | 
[**retrieve_all_requisitions**](RequisitionsApi.md#retrieve_all_requisitions) | **GET** /api/v2/requisitions/ | 

# **create_requisition**
> GocardlessBankaccountdataSpectacularRequisition create_requisition(body)



Create a new requisition

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.RequisitionsApi(gocardless_bankaccountdata.ApiClient(configuration))
body = gocardless_bankaccountdata.GocardlessBankaccountdataRequisitionRequest() # GocardlessBankaccountdataRequisitionRequest | 

try:
    api_response = api_instance.create_requisition(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequisitionsApi->create_requisition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GocardlessBankaccountdataRequisitionRequest**](GocardlessBankaccountdataRequisitionRequest.md)|  | 

### Return type

[**GocardlessBankaccountdataSpectacularRequisition**](GocardlessBankaccountdataSpectacularRequisition.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_requisition_by_id**
> delete_requisition_by_id(id)



Delete requisition and its end user agreement

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.RequisitionsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this requisition.

try:
    api_instance.delete_requisition_by_id(id)
except ApiException as e:
    print("Exception when calling RequisitionsApi->delete_requisition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this requisition. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requisition_by_id**
> GocardlessBankaccountdataRequisition requisition_by_id(id)



Retrieve a requisition by ID

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.RequisitionsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this requisition.

try:
    api_response = api_instance.requisition_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequisitionsApi->requisition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this requisition. | 

### Return type

[**GocardlessBankaccountdataRequisition**](GocardlessBankaccountdataRequisition.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_requisitions**
> GocardlessBankaccountdataPaginatedRequisitionList retrieve_all_requisitions(limit=limit, offset=offset)



Retrieve all requisitions belonging to the company

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.RequisitionsApi(gocardless_bankaccountdata.ApiClient(configuration))
limit = 100 # int | Number of results to return per page. (optional) (default to 100)
offset = 0 # int | The initial zero-based index from which to return the results. (optional) (default to 0)

try:
    api_response = api_instance.retrieve_all_requisitions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequisitionsApi->retrieve_all_requisitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **int**| The initial zero-based index from which to return the results. | [optional] [default to 0]

### Return type

[**GocardlessBankaccountdataPaginatedRequisitionList**](GocardlessBankaccountdataPaginatedRequisitionList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

