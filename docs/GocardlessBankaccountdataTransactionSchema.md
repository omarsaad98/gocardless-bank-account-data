# GocardlessBankaccountdataTransactionSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | transactionId | [optional] 
**entry_reference** | **str** | entryReference | [optional] 
**end_to_end_id** | **str** | endToEndId | [optional] 
**mandate_id** | **str** | mandateId | [optional] 
**check_id** | **str** | checkId | [optional] 
**creditor_id** | **str** | creditorId | [optional] 
**booking_date** | **str** | bookingDate | [optional] 
**value_date** | **str** | valueDate | [optional] 
**booking_date_time** | **str** | bookingDateTime | [optional] 
**value_date_time** | **str** | valueDateTime | [optional] 
**transaction_amount** | **GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataTransactionAmount** | transactionAmount | 
**currency_exchange** | [**list[GocardlessBankaccountdataCurrencyExchangeSchema]**](GocardlessBankaccountdataCurrencyExchangeSchema.md) |  | [optional] 
**creditor_name** | **str** | creditorName | [optional] 
**creditor_account** | **GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataCreditorAccount** | creditorAccount | [optional] 
**ultimate_creditor** | **str** | ultimateCreditor | [optional] 
**debtor_name** | **str** | debtorName | [optional] 
**debtor_account** | **GocardlessBankaccountdataAllOfTransactionSchemaGocardlessBankaccountdataDebtorAccount** | debtorAccount | [optional] 
**ultimate_debtor** | **str** | ultimateDebtor | [optional] 
**remittance_information_unstructured** | **str** | remittanceInformationUnstructured | [optional] 
**remittance_information_unstructured_array** | **list[str]** | remittanceInformationUnstructuredArray | [optional] 
**remittance_information_structured** | **str** | remittanceInformationStructured | [optional] 
**remittance_information_structured_array** | **list[str]** | remittanceInformationStructuredArray | [optional] 
**additional_information** | **str** | additionalInformation | [optional] 
**purpose_code** | **str** | purposeCode | [optional] 
**bank_transaction_code** | **str** | bankTransactionCode | [optional] 
**proprietary_bank_transaction_code** | **str** | proprietaryBankTransactionCode | [optional] 
**internal_transaction_id** | **str** | internalTransactionId | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

