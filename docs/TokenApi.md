# gocardless_bankaccountdata.TokenApi

All URIs are relative to *https://bankaccountdata.gocardless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_a_new_access_token**](TokenApi.md#get_a_new_access_token) | **POST** /api/v2/token/refresh/ | 
[**obtain_new_accessrefresh_token_pair**](TokenApi.md#obtain_new_accessrefresh_token_pair) | **POST** /api/v2/token/new/ | 

# **get_a_new_access_token**
> GocardlessBankaccountdataSpectacularJWTRefresh get_a_new_access_token(body)



Refresh access token

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.TokenApi(gocardless_bankaccountdata.ApiClient(configuration))
body = gocardless_bankaccountdata.GocardlessBankaccountdataJWTRefreshRequest() # GocardlessBankaccountdataJWTRefreshRequest | 

try:
    api_response = api_instance.get_a_new_access_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_a_new_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GocardlessBankaccountdataJWTRefreshRequest**](GocardlessBankaccountdataJWTRefreshRequest.md)|  | 

### Return type

[**GocardlessBankaccountdataSpectacularJWTRefresh**](GocardlessBankaccountdataSpectacularJWTRefresh.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obtain_new_accessrefresh_token_pair**
> GocardlessBankaccountdataSpectacularJWTObtain obtain_new_accessrefresh_token_pair(body)



Obtain JWT pair

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.TokenApi(gocardless_bankaccountdata.ApiClient(configuration))
body = gocardless_bankaccountdata.GocardlessBankaccountdataJWTObtainPairRequest() # GocardlessBankaccountdataJWTObtainPairRequest | 

try:
    api_response = api_instance.obtain_new_accessrefresh_token_pair(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->obtain_new_accessrefresh_token_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GocardlessBankaccountdataJWTObtainPairRequest**](GocardlessBankaccountdataJWTObtainPairRequest.md)|  | 

### Return type

[**GocardlessBankaccountdataSpectacularJWTObtain**](GocardlessBankaccountdataSpectacularJWTObtain.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

