# GRAD-102 — Keçərsiz axtarış parametrləri

| Parameter | Value |
|-----------|-------|
| q | A |
| currency | GBP |
| sort | unknown |
| order | upward |

## API_BEN_QUERY_001 — Keçərsiz axtarış və sıralama parametrləri rədd edilməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et <Parameter> = <Value>
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" deyeri boş olmamalıdır