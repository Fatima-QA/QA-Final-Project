# GRAD-201 — Kartın başlanğıc məbləğinin sərhədləri

| Amount | Status | CheckPath | Expected |
|--------|--------|-----------|----------|
| 0.99 | 400 | code | VALIDATION_ERROR |
| 1 | 201 | availableBalance | 1 |
| 1000 | 201 | availableBalance | 1000 |
| 1000.01 | 400 | code | VALIDATION_ERROR |
| 0 | 400 | code | VALIDATION_ERROR |
| -1 | 400 | code | VALIDATION_ERROR |
| 1.001 | 400 | code | VALIDATION_ERROR |
| "50" | 400 | code | VALIDATION_ERROR |


## API_CARD_AMOUNT_BVA_001 — Kart yalnız icazə verilən başlanğıc məbləği ilə yaradılmalıdır
tags: final-project, cards, bva, regression

* Login Test User
* "cardAmount" deyişenine <Amount> deyerini ver
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-amount.json"
* Post request and display respons
* Status kodunun <Status> olmalıdır
* Json cavabında <CheckPath> deyeri <Expected> beraberdir