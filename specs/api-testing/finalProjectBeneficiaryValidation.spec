# GRAD-101 — IBAN və valyuta validasiyası

| Iban | Currency | ErrorPath |
|------|----------|-----------|
| AZ12TEST0000000000000000000 | AZN | details.find { it.field == 'iban' }.message |
| AZ12TEST000000000000000000001 | AZN | details.find { it.field == 'iban' }.message |
| TR12TEST00000000000000000001 | AZN | details.find { it.field == 'iban' }.message |
| AZ12TEST00000000000000000001 | GBP | details.find { it.field == 'currency' }.message |
| AZ12TEST00000000000000000001 | 123 | details.find { it.field == 'currency' }.message |

## API_BEN_VALIDATION_001 — Keçərsiz IBAN və ya dəstəklənməyən valyuta ilə alıcı yaradılmamalıdır
tags: final-project, beneficiaries, negative, regression

* Login Test User
* "testIban" deyişenine <Iban> deyerini ver
* "testCurrency" deyişenine <Currency> deyerini ver
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-validation.json"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında <ErrorPath> deyeri boş olmamalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır