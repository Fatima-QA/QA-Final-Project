# GRAD-303 — Tarixçə sorğusunun səhifələmə parametrləri

| Parameter | Value | CheckPath |
|-----------|-------|-----------|
| page | 0 | details.find { it.field == 'page' }.message |
| page | -1 | details.find { it.field == 'page' }.message |
| page | abc | details.find { it.field == 'page' }.message |
| limit | 0 | details.find { it.field == 'limit' }.message |
| limit | 51 | details.find { it.field == 'limit' }.message |

## API_PAY_HISTORY_VALIDATION_001 — Keçərsiz səhifə və səhifə ölçüsü rədd edilməlidir
tags: final-project, payments, regression, negative, boundary

* Login Test User

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et <Parameter> = <Value>
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında <CheckPath> deyeri boş olmamalıdır