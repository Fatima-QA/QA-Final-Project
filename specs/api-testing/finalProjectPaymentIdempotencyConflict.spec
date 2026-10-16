# GRAD-302 — Təkrar ödənişdən qorunma

## API_PAY_IDEMPOTENCY_001 — İstifadə olunmuş ödəniş açarı ilə fərqli məbləğ göndərildikdə ödəniş rədd edilməlidir
tags: final-project, payments, regression, idempotency

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
* Header elave et "Idempotency-Key" = "final-conflict-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "originalPaymentId"
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "40" beraberdir

* "paymentAmount" deyişenine "11" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-conflict-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_CONFLICT" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "40" beraberdir
* Json cavabında "spentToday" deyeri "10" beraberdir

* "paymentAmount" deyişenine "10" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-conflict-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Header "Idempotent-Replay" deyerinde "true" olmalıdır
* Json cavabında "id" deyeri "${originalPaymentId}" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "40" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "40" beraberdir
* Json cavabında "spentToday" deyeri "10" beraberdir