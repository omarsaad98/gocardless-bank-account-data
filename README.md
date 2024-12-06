# gocardless-bankaccountdata
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0 (v2)
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import gocardless_bankaccountdata 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gocardless_bankaccountdata
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AccountsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_account_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_details: %s\n" % e)


# create an instance of the API class
api_instance = gocardless_bankaccountdata.AccountsApi(gocardless_bankaccountdata.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_account_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_metadata: %s\n" % e)


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

## Documentation for API Endpoints

All URIs are relative to *https://bankaccountdata.gocardless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**retrieve_account_balances**](docs/AccountsApi.md#retrieve_account_balances) | **GET** /api/v2/accounts/{id}/balances/ | 
*AccountsApi* | [**retrieve_account_details**](docs/AccountsApi.md#retrieve_account_details) | **GET** /api/v2/accounts/{id}/details/ | 
*AccountsApi* | [**retrieve_account_metadata**](docs/AccountsApi.md#retrieve_account_metadata) | **GET** /api/v2/accounts/{id}/ | 
*AccountsApi* | [**retrieve_account_transactions**](docs/AccountsApi.md#retrieve_account_transactions) | **GET** /api/v2/accounts/{id}/transactions/ | 
*AgreementsApi* | [**accept_eua**](docs/AgreementsApi.md#accept_eua) | **PUT** /api/v2/agreements/enduser/{id}/accept/ | 
*AgreementsApi* | [**create_eua**](docs/AgreementsApi.md#create_eua) | **POST** /api/v2/agreements/enduser/ | 
*AgreementsApi* | [**delete_eua_by_id**](docs/AgreementsApi.md#delete_eua_by_id) | **DELETE** /api/v2/agreements/enduser/{id}/ | 
*AgreementsApi* | [**retrieve_all_euas_for_an_end_user**](docs/AgreementsApi.md#retrieve_all_euas_for_an_end_user) | **GET** /api/v2/agreements/enduser/ | 
*AgreementsApi* | [**retrieve_eua_by_id**](docs/AgreementsApi.md#retrieve_eua_by_id) | **GET** /api/v2/agreements/enduser/{id}/ | 
*InstitutionsApi* | [**retrieve_all_supported_institutions_in_a_given_country**](docs/InstitutionsApi.md#retrieve_all_supported_institutions_in_a_given_country) | **GET** /api/v2/institutions/ | 
*InstitutionsApi* | [**retrieve_institution**](docs/InstitutionsApi.md#retrieve_institution) | **GET** /api/v2/institutions/{id}/ | 
*RequisitionsApi* | [**create_requisition**](docs/RequisitionsApi.md#create_requisition) | **POST** /api/v2/requisitions/ | 
*RequisitionsApi* | [**delete_requisition_by_id**](docs/RequisitionsApi.md#delete_requisition_by_id) | **DELETE** /api/v2/requisitions/{id}/ | 
*RequisitionsApi* | [**requisition_by_id**](docs/RequisitionsApi.md#requisition_by_id) | **GET** /api/v2/requisitions/{id}/ | 
*RequisitionsApi* | [**retrieve_all_requisitions**](docs/RequisitionsApi.md#retrieve_all_requisitions) | **GET** /api/v2/requisitions/ | 
*TokenApi* | [**get_a_new_access_token**](docs/TokenApi.md#get_a_new_access_token) | **POST** /api/v2/token/refresh/ | 
*TokenApi* | [**obtain_new_accessrefresh_token_pair**](docs/TokenApi.md#obtain_new_accessrefresh_token_pair) | **POST** /api/v2/token/new/ | 

## Documentation For Models

 - [GocardlessBankaccountdataAccount](docs/GocardlessBankaccountdataAccount.md)
 - [GocardlessBankaccountdataAccountBalance](docs/GocardlessBankaccountdataAccountBalance.md)
 - [GocardlessBankaccountdataAccountDetail](docs/GocardlessBankaccountdataAccountDetail.md)
 - [GocardlessBankaccountdataAccountSchema](docs/GocardlessBankaccountdataAccountSchema.md)
 - [GocardlessBankaccountdataAccountTransactions](docs/GocardlessBankaccountdataAccountTransactions.md)
 - [GocardlessBankaccountdataAllOfAccountDetailGocardlessBankaccountdataAccount](docs/GocardlessBankaccountdataAllOfAccountDetailGocardlessBankaccountdataAccount.md)
 - [GocardlessBankaccountdataAllOfAccountTransactionsGocardlessBankaccountdataTransactions](docs/GocardlessBankaccountdataAllOfAccountTransactionsGocardlessBankaccountdataTransactions.md)
 - [GocardlessBankaccountdataAllOfBalanceSchemaGocardlessBankaccountdataBalanceAmount](docs/GocardlessBankaccountdataAllOfBalanceSchemaGocardlessBankaccountdataBalanceAmount.md)
 - [GocardlessBankaccountdataAllOfDetailSchemaGocardlessBankaccountdataOwnerAddressStructured](docs/GocardlessBankaccountdataAllOfDetailSchemaGocardlessBankaccountdataOwnerAddressStructured.md)
 - [GocardlessBankaccountdataAllOfRequisitionGocardlessBankaccountdataStatus](docs/GocardlessBankaccountdataAllOfRequisitionGocardlessBankaccountdataStatus.md)
 - [GocardlessBankaccountdataAllOfSpectacularRequisitionGocardlessBankaccountdataStatus](docs/GocardlessBankaccountdataAllOfSpectacularRequisitionGocardlessBankaccountdataStatus.md)
 - [GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataCreditorAccount](docs/GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataCreditorAccount.md)
 - [GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataDebtorAccount](docs/GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataDebtorAccount.md)
 - [GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataTransactionAmount](docs/GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataTransactionAmount.md)
 - [GocardlessBankaccountdataBalanceAmountSchema](docs/GocardlessBankaccountdataBalanceAmountSchema.md)
 - [GocardlessBankaccountdataBalanceSchema](docs/GocardlessBankaccountdataBalanceSchema.md)
 - [GocardlessBankaccountdataBankTransaction](docs/GocardlessBankaccountdataBankTransaction.md)
 - [GocardlessBankaccountdataCurrencyExchangeSchema](docs/GocardlessBankaccountdataCurrencyExchangeSchema.md)
 - [GocardlessBankaccountdataDetailSchema](docs/GocardlessBankaccountdataDetailSchema.md)
 - [GocardlessBankaccountdataEndUserAgreement](docs/GocardlessBankaccountdataEndUserAgreement.md)
 - [GocardlessBankaccountdataEndUserAgreementRequest](docs/GocardlessBankaccountdataEndUserAgreementRequest.md)
 - [GocardlessBankaccountdataEnduserAcceptanceDetailsRequest](docs/GocardlessBankaccountdataEnduserAcceptanceDetailsRequest.md)
 - [GocardlessBankaccountdataErrorResponse](docs/GocardlessBankaccountdataErrorResponse.md)
 - [GocardlessBankaccountdataIntegration](docs/GocardlessBankaccountdataIntegration.md)
 - [GocardlessBankaccountdataIntegrationRetrieve](docs/GocardlessBankaccountdataIntegrationRetrieve.md)
 - [GocardlessBankaccountdataJWTObtainPairRequest](docs/GocardlessBankaccountdataJWTObtainPairRequest.md)
 - [GocardlessBankaccountdataJWTRefreshRequest](docs/GocardlessBankaccountdataJWTRefreshRequest.md)
 - [GocardlessBankaccountdataOwnerAddressStructuredSchema](docs/GocardlessBankaccountdataOwnerAddressStructuredSchema.md)
 - [GocardlessBankaccountdataPaginatedEndUserAgreementList](docs/GocardlessBankaccountdataPaginatedEndUserAgreementList.md)
 - [GocardlessBankaccountdataPaginatedRequisitionList](docs/GocardlessBankaccountdataPaginatedRequisitionList.md)
 - [GocardlessBankaccountdataRequisition](docs/GocardlessBankaccountdataRequisition.md)
 - [GocardlessBankaccountdataRequisitionRequest](docs/GocardlessBankaccountdataRequisitionRequest.md)
 - [GocardlessBankaccountdataSpectacularJWTObtain](docs/GocardlessBankaccountdataSpectacularJWTObtain.md)
 - [GocardlessBankaccountdataSpectacularJWTRefresh](docs/GocardlessBankaccountdataSpectacularJWTRefresh.md)
 - [GocardlessBankaccountdataSpectacularRequisition](docs/GocardlessBankaccountdataSpectacularRequisition.md)
 - [GocardlessBankaccountdataStatusEnum](docs/GocardlessBankaccountdataStatusEnum.md)
 - [GocardlessBankaccountdataTransactionAmountSchema](docs/GocardlessBankaccountdataTransactionAmountSchema.md)
 - [GocardlessBankaccountdataTransactionSchema](docs/GocardlessBankaccountdataTransactionSchema.md)

## Documentation For Authorization


## jwtAuth



## Author

