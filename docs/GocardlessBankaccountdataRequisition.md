# GocardlessBankaccountdataRequisition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created** | **datetime** | The date &amp; time at which the requisition was created. | [optional] 
**redirect** | **str** | redirect URL to your application after end-user authorization with ASPSP | 
**status** | **GocardlessBankaccountdataAllOfRequisitionGocardlessBankaccountdataStatus** | status of this requisition | [optional] 
**institution_id** | **str** | an Institution ID for this Requisition | 
**agreement** | **str** | EUA associated with this requisition | [optional] 
**reference** | **str** | additional ID to identify the end user | [optional] 
**accounts** | **list[str]** | array of account IDs retrieved within a scope of this requisition | [optional] 
**user_language** | **str** | A two-letter country code (ISO 639-1) | [optional] 
**link** | **str** | link to initiate authorization with Institution | [optional] [default to 'https://ob.gocardless.com/psd2/start/3fa85f64-5717-4562-b3fc-2c963f66afa6/{$INSTITUTION_ID}']
**ssn** | **str** | optional SSN field to verify ownership of the account | [optional] 
**account_selection** | **bool** | option to enable account selection view for the end user | [optional] [default to False]
**redirect_immediate** | **bool** | enable redirect back to the client after account list received | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

