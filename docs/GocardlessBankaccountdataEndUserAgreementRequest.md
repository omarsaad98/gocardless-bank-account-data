# GocardlessBankaccountdataEndUserAgreementRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | an Institution ID for this EUA | 
**max_historical_days** | **int** | Maximum number of days of transaction data to retrieve. | [optional] [default to 90]
**access_valid_for_days** | **int** | Number of days from acceptance that the access can be used. | [optional] [default to 90]
**access_scope** | **list[object]** | Array containing one or several values of [&#x27;balances&#x27;, &#x27;details&#x27;, &#x27;transactions&#x27;] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

