# gocardless_bankaccountdata.AgreementsApi

All URIs are relative to *https://bankaccountdata.gocardless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_eua**](AgreementsApi.md#accept_eua) | **PUT** /api/v2/agreements/enduser/{id}/accept/ | 
[**create_eua**](AgreementsApi.md#create_eua) | **POST** /api/v2/agreements/enduser/ | 
[**delete_eua_by_id**](AgreementsApi.md#delete_eua_by_id) | **DELETE** /api/v2/agreements/enduser/{id}/ | 
[**retrieve_all_euas_for_an_end_user**](AgreementsApi.md#retrieve_all_euas_for_an_end_user) | **GET** /api/v2/agreements/enduser/ | 
[**retrieve_eua_by_id**](AgreementsApi.md#retrieve_eua_by_id) | **GET** /api/v2/agreements/enduser/{id}/ | 

# **accept_eua**
> GocardlessBankaccountdataEndUserAgreement accept_eua(body, id)



Accept an end-user agreement via the API

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AgreementsApi(gocardless_bankaccountdata.ApiClient(configuration))
body = gocardless_bankaccountdata.GocardlessBankaccountdataEnduserAcceptanceDetailsRequest() # GocardlessBankaccountdataEnduserAcceptanceDetailsRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_response = api_instance.accept_eua(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->accept_eua: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GocardlessBankaccountdataEnduserAcceptanceDetailsRequest**](GocardlessBankaccountdataEnduserAcceptanceDetailsRequest.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

[**GocardlessBankaccountdataEndUserAgreement**](GocardlessBankaccountdataEndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_eua**
> GocardlessBankaccountdataEndUserAgreement create_eua(body)



API endpoints related to end-user agreements.

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AgreementsApi(gocardless_bankaccountdata.ApiClient(configuration))
body = gocardless_bankaccountdata.GocardlessBankaccountdataEndUserAgreementRequest() # GocardlessBankaccountdataEndUserAgreementRequest | 

try:
    api_response = api_instance.create_eua(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->create_eua: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GocardlessBankaccountdataEndUserAgreementRequest**](GocardlessBankaccountdataEndUserAgreementRequest.md)|  | 

### Return type

[**GocardlessBankaccountdataEndUserAgreement**](GocardlessBankaccountdataEndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_eua_by_id**
> delete_eua_by_id(id)



Delete an end user agreement

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AgreementsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_instance.delete_eua_by_id(id)
except ApiException as e:
    print("Exception when calling AgreementsApi->delete_eua_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_euas_for_an_end_user**
> GocardlessBankaccountdataPaginatedEndUserAgreementList retrieve_all_euas_for_an_end_user(limit=limit, offset=offset)



Overwrite pagination to map CONN consent data with end user agreements.  Args:     request (HttpRequest): Request  Returns:     HttpResponse: Response

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AgreementsApi(gocardless_bankaccountdata.ApiClient(configuration))
limit = 100 # int | Number of results to return per page. (optional) (default to 100)
offset = 0 # int | The initial zero-based index from which to return the results. (optional) (default to 0)

try:
    api_response = api_instance.retrieve_all_euas_for_an_end_user(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->retrieve_all_euas_for_an_end_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **int**| The initial zero-based index from which to return the results. | [optional] [default to 0]

### Return type

[**GocardlessBankaccountdataPaginatedEndUserAgreementList**](GocardlessBankaccountdataPaginatedEndUserAgreementList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_eua_by_id**
> GocardlessBankaccountdataEndUserAgreement retrieve_eua_by_id(id)



Retrieve end user agreement by ID

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AgreementsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_response = api_instance.retrieve_eua_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->retrieve_eua_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

[**GocardlessBankaccountdataEndUserAgreement**](GocardlessBankaccountdataEndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

