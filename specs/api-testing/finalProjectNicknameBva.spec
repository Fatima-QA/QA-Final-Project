# GRAD-101 — Ləqəbin uzunluq sərhədləri

| Nickname | Status | CheckPath | Expected |
|----------|--------|-----------|----------|
| A | 201 | nickname | A |
| AbcdefghijAbcdefghij | 201 | nickname | AbcdefghijAbcdefghij |
| AbcdefghijAbcdefghijA | 400 | code | VALIDATION_ERROR |

## API_BEN_NICK_BVA_001 — Ləqəb yalnız icazə verilən uzunluqda qəbul edilməlidir
tags: final-project, beneficiaries, bva, regression

* Login Test User
* "testNickname" deyişenine <Nickname> deyerini ver
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-nickname.json"
* Post request and display respons
* Status kodunun <Status> olmalıdır
* Json cavabında <CheckPath> deyeri <Expected> beraberdir