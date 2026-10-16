# GRAD-302 — Bir ödəniş üzrə məbləğ limiti

| Amount | Status | CheckPath | Expected | BalanceAfter | SpentToday |
|--------|--------|-----------|----------|--------------|------------|
| 300 | 201 | status | SUCCESS | 700 | 300 |
| 300.01 | 422 | code | PER_TRANSACTION_LIMIT | 1000 | 0 |

## API_PAY_LIMIT_001 — Limitə bərabər ödəniş qəbul edilməli, limiti aşan ödəniş rədd edilməlidir
tags: final-project, payments, regression, boundary

* Login Test User
* "cardAmount" deyişenine "1000" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-amount.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "cardId"
* Json cavabında "availableBalance" deyeri "1000" beraberdir

* "testBillerId" deyişenine "azerisiq" deyerini ver
* "testSubscriberNo" deyişenine "1234567890" deyerini ver
* "paymentAmount" deyişenine <Amount> deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-per-limit-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun <Status> olmalıdır
* Json cavabında <CheckPath> deyeri <Expected> beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri <BalanceAfter> beraberdir
* Json cavabında "spentToday" deyeri <SpentToday> beraberdir