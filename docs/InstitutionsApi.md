# gocardless_bankaccountdata.InstitutionsApi

All URIs are relative to *https://bankaccountdata.gocardless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_supported_institutions_in_a_given_country**](InstitutionsApi.md#retrieve_all_supported_institutions_in_a_given_country) | **GET** /api/v2/institutions/ | 
[**retrieve_institution**](InstitutionsApi.md#retrieve_institution) | **GET** /api/v2/institutions/{id}/ | 

# **retrieve_all_supported_institutions_in_a_given_country**
> list[GocardlessBankaccountdataIntegration] retrieve_all_supported_institutions_in_a_given_country(access_scopes_supported=access_scopes_supported, account_selection_supported=account_selection_supported, business_accounts_supported=business_accounts_supported, card_accounts_supported=card_accounts_supported, corporate_accounts_supported=corporate_accounts_supported, country=country, payment_submission_supported=payment_submission_supported, payments_enabled=payments_enabled, pending_transactions_supported=pending_transactions_supported, private_accounts_supported=private_accounts_supported, read_debtor_account_supported=read_debtor_account_supported, read_refund_account_supported=read_refund_account_supported, ssn_verification_supported=ssn_verification_supported)



List all available institutions

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.InstitutionsApi(gocardless_bankaccountdata.ApiClient(configuration))
access_scopes_supported = 'access_scopes_supported_example' # str | Boolean value, indicating if access scopes are supported (optional)
account_selection_supported = 'account_selection_supported_example' # str | Boolean value, indicating if account selection is supported (optional)
business_accounts_supported = 'business_accounts_supported_example' # str | Boolean value, indicating if business accounts are supported (optional)
card_accounts_supported = 'card_accounts_supported_example' # str | Boolean value, indicating if card accounts are supported (optional)
corporate_accounts_supported = 'corporate_accounts_supported_example' # str | Boolean value, indicating if corporate accounts are supported (optional)
country = 'country_example' # str | ISO 3166 two-character country code (optional)
payment_submission_supported = 'payment_submission_supported_example' # str | Boolean value, indicating if payment submission is supported (optional)
payments_enabled = 'payments_enabled_example' # str | Boolean value, indicating if payments are supported (optional)
pending_transactions_supported = 'pending_transactions_supported_example' # str | Boolean value, indicating if pending transactions are supported (optional)
private_accounts_supported = 'private_accounts_supported_example' # str | Boolean value, indicating if private accounts are supported (optional)
read_debtor_account_supported = 'read_debtor_account_supported_example' # str | Boolean value, indicating if debtor account can be read before submitting payment (optional)
read_refund_account_supported = 'read_refund_account_supported_example' # str | Boolean value, indicating if read refund account is supported (optional)
ssn_verification_supported = 'ssn_verification_supported_example' # str | Boolean value, indicating if ssn verification is supported (optional)

try:
    api_response = api_instance.retrieve_all_supported_institutions_in_a_given_country(access_scopes_supported=access_scopes_supported, account_selection_supported=account_selection_supported, business_accounts_supported=business_accounts_supported, card_accounts_supported=card_accounts_supported, corporate_accounts_supported=corporate_accounts_supported, country=country, payment_submission_supported=payment_submission_supported, payments_enabled=payments_enabled, pending_transactions_supported=pending_transactions_supported, private_accounts_supported=private_accounts_supported, read_debtor_account_supported=read_debtor_account_supported, read_refund_account_supported=read_refund_account_supported, ssn_verification_supported=ssn_verification_supported)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->retrieve_all_supported_institutions_in_a_given_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_scopes_supported** | **str**| Boolean value, indicating if access scopes are supported | [optional] 
 **account_selection_supported** | **str**| Boolean value, indicating if account selection is supported | [optional] 
 **business_accounts_supported** | **str**| Boolean value, indicating if business accounts are supported | [optional] 
 **card_accounts_supported** | **str**| Boolean value, indicating if card accounts are supported | [optional] 
 **corporate_accounts_supported** | **str**| Boolean value, indicating if corporate accounts are supported | [optional] 
 **country** | **str**| ISO 3166 two-character country code | [optional] 
 **payment_submission_supported** | **str**| Boolean value, indicating if payment submission is supported | [optional] 
 **payments_enabled** | **str**| Boolean value, indicating if payments are supported | [optional] 
 **pending_transactions_supported** | **str**| Boolean value, indicating if pending transactions are supported | [optional] 
 **private_accounts_supported** | **str**| Boolean value, indicating if private accounts are supported | [optional] 
 **read_debtor_account_supported** | **str**| Boolean value, indicating if debtor account can be read before submitting payment | [optional] 
 **read_refund_account_supported** | **str**| Boolean value, indicating if read refund account is supported | [optional] 
 **ssn_verification_supported** | **str**| Boolean value, indicating if ssn verification is supported | [optional] 

### Return type

[**list[GocardlessBankaccountdataIntegration]**](GocardlessBankaccountdataIntegration.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_institution**
> GocardlessBankaccountdataIntegrationRetrieve retrieve_institution(id)



Get details about a specific Institution and its supported features

### Example
```python
from __future__ import print_function
import time
import gocardless_bankaccountdata
from gocardless_bankaccountdata.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gocardless_bankaccountdata.InstitutionsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_institution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->retrieve_institution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GocardlessBankaccountdataIntegrationRetrieve**](GocardlessBankaccountdataIntegrationRetrieve.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

