# GRAD-302 — Ödəniş üçün balansın kifayət etməsi

## API_PAY_FUNDS_001 — Balansdan artıq ödəniş rədd edilməli, balansa bərabər ödəniş qəbul edilməlidir
tags: final-project, payments, regression, boundary

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
* "paymentAmount" deyişenine "50.01" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-funds-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir

* "paymentAmount" deyişenine "50" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-funds-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "50" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "50" beraberdir
* Json cavabında "balanceAfter" deyeri "0" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "0" beraberdir
* Json cavabında "spentToday" deyeri "50" beraberdir