# GocardlessBankaccountdataRequisitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect** | **str** | redirect URL to your application after end-user authorization with ASPSP | 
**institution_id** | **str** | an Institution ID for this Requisition | 
**agreement** | **str** | EUA associated with this requisition | [optional] 
**reference** | **str** | additional ID to identify the end user | [optional] 
**user_language** | **str** | A two-letter country code (ISO 639-1) | [optional] 
**ssn** | **str** | optional SSN field to verify ownership of the account | [optional] 
**account_selection** | **bool** | option to enable account selection view for the end user | [optional] [default to False]
**redirect_immediate** | **bool** | enable redirect back to the client after account list received | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

