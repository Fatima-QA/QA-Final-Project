# GRAD-302 — Aktiv olmayan kartla ödəniş

| Reason | CardStatus |
|--------|------------|
| TEMPORARY | FROZEN |
| LOST | BLOCKED |

## API_PAY_STATE_001 — Aktiv olmayan kartla ödəniş rədd edilməli və balans dəyişməməlidir
tags: final-project, payments, regression, negative

* Login Test User

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "cardId"

* "testBlockReason" deyişenine <Reason> deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-block-check.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri <CardStatus> beraberdir

* "testBillerId" deyişenine "bakcell" deyerini ver
* "testSubscriberNo" deyişenine "551234567" deyerini ver
* "paymentAmount" deyişenine "10" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-state-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri <CardStatus> beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir