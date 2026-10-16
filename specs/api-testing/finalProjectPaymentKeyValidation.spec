# GRAD-302 — Ödəniş açarının uzunluğu

| Key |
|-----|
| 1234567 |
| abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm |

## API_PAY_KEY_001 — İcazə verilən uzunluqdan kənar ödəniş açarı rədd edilməlidir
tags: final-project, payments, regression, negative, boundary

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

* "testBillerId" deyişenine "bakcell" deyerini ver
* "testSubscriberNo" deyişenine "551234567" deyerini ver
* "paymentAmount" deyişenine "10" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = <Key>
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_INVALID" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir