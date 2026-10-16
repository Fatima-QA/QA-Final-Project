# GRAD-302 — Keçərsiz ödəniş məlumatları

| SubscriberNo | Amount | Status | ErrorCode |
|--------------|--------|--------|-----------|
| 551234567 | 0.49 | 422 | AMOUNT_OUT_OF_RANGE |
| 551234567 | 200.01 | 422 | AMOUNT_OUT_OF_RANGE |
| 551234567 | -1 | 400 | VALIDATION_ERROR |
| 551234567 | 1.001 | 400 | VALIDATION_ERROR |
| 551234567 | "10" | 400 | VALIDATION_ERROR |
| 55123456 | 10 | 422 | INVALID_SUBSCRIBER |
| 5512345678 | 10 | 422 | INVALID_SUBSCRIBER |
| 501234567 | 10 | 422 | INVALID_SUBSCRIBER |

## API_PAY_VALIDATION_001 — Keçərsiz ödəniş məlumatları rədd edilməli və kartın balansı dəyişməməlidir
tags: final-project, payments, regression, negative, validation

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
* "testSubscriberNo" deyişenine <SubscriberNo> deyerini ver
* "paymentAmount" deyişenine <Amount> deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-invalid-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun <Status> olmalıdır
* Json cavabında "code" deyeri <ErrorCode> beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir