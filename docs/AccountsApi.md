# gocardless_bankaccountdata.AccountsApi

All URIs are relative to *https://bankaccountdata.gocardless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_account_balances**](AccountsApi.md#retrieve_account_balances) | **GET** /api/v2/accounts/{id}/balances/ | 
[**retrieve_account_details**](AccountsApi.md#retrieve_account_details) | **GET** /api/v2/accounts/{id}/details/ | 
[**retrieve_account_metadata**](AccountsApi.md#retrieve_account_metadata) | **GET** /api/v2/accounts/{id}/ | 
[**retrieve_account_transactions**](AccountsApi.md#retrieve_account_transactions) | **GET** /api/v2/accounts/{id}/transactions/ | 

# **retrieve_account_balances**
> GocardlessBankaccountdataAccountBalance retrieve_account_balances(id)



Access account balances.  Balances will be returned in Berlin Group PSD2 format.

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AccountsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_account_balances(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GocardlessBankaccountdataAccountBalance**](GocardlessBankaccountdataAccountBalance.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account_details**
> GocardlessBankaccountdataAccountDetail retrieve_account_details(id)



Access account details.  Account details will be returned in Berlin Group PSD2 format.

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AccountsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_account_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GocardlessBankaccountdataAccountDetail**](GocardlessBankaccountdataAccountDetail.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account_metadata**
> GocardlessBankaccountdataAccount retrieve_account_metadata(id)



Access account metadata.  Information about the account record, such as the processing status and IBAN.  Account status is recalculated based on the error count in the latest req.

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AccountsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_account_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GocardlessBankaccountdataAccount**](GocardlessBankaccountdataAccount.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account_transactions**
> GocardlessBankaccountdataAccountTransactions retrieve_account_transactions(id, date_from=date_from, date_to=date_to)



Access account transactions.  Transactions will be returned in Berlin Group PSD2 format.

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AccountsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 
date_from = '2013-10-20' # date |  (optional)
date_to = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.retrieve_account_transactions(id, date_from=date_from, date_to=date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 

### Return type

[**GocardlessBankaccountdataAccountTransactions**](GocardlessBankaccountdataAccountTransactions.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

