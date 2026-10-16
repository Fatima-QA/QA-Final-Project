# GRAD-101 — Alıcının ad uzunluğu və formatı

| Name | Status | CheckPath | Expected |
  |------|--------|-----------|----------|
  | A | 400 | code | VALIDATION_ERROR |
  | Al | 201 | fullName | Al |
  | AbcdefghijAbcdefghijAbcdefghijAbcdefghijAbcdefghij | 201 | fullName | AbcdefghijAbcdefghijAbcdefghijAbcdefghijAbcdefghij |
  | AbcdefghijAbcdefghijAbcdefghijAbcdefghijAbcdefghijA | 400 | code | VALIDATION_ERROR |
  | --- | 400 | code | VALIDATION_ERROR |
  | Ali2 | 400 | code | VALIDATION_ERROR |
  | 2Ali | 400 | code | VALIDATION_ERROR |
  | Əli Məmmədov | 201 | fullName | Əli Məmmədov |
  | Ali-Vəli O'Neil | 201 | fullName | Ali-Vəli O'Neil |


## API_BEN_BVA_001 — Alıcının adı yalnız icazə verilən uzunluq daxilində qəbul edilməlidir
tags: final-project, beneficiaries, bva, regression

* Login Test User
* "bvaName" deyişenine <Name> deyerini ver
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-name.json"
* Post request and display respons
* Status kodunun <Status> olmalıdır
* Json cavabında <CheckPath> deyeri <Expected> beraberdir