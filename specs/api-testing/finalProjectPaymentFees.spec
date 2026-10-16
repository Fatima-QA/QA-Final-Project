# GRAD-302 — Ödəniş komissiyası və kart balansı

| BillerId | SubscriberNo | Amount | Fee | Total | BalanceAfter |
|----------|--------------|--------|-----|-------|--------------|
| bakcell | 551234567 | 10 | 0 | 10 | 40 |
| aztelekom | 1234567 | 10 | 0.5 | 10.5 | 39.5 |
| citynet | CN123456 | 5 | 0.2 | 5.2 | 44.8 |
| citynet | CN123456 | 20 | 0.2 | 20.2 | 29.8 |
| citynet | CN123456 | 21 | 0.21 | 21.21 | 28.79 |

## API_PAY_FEE_001 — Ödənişə uyğun komissiya hesablanmalı və kartdan məbləğlə komissiyanın cəmi çıxılmalıdır
tags: final-project, payments, regression, fees

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
* Json cavabında "availableBalance" deyeri "50" beraberdir

* "testBillerId" deyişenine <BillerId> deyerini ver
* "testSubscriberNo" deyişenine <SubscriberNo> deyerini ver
* "paymentAmount" deyişenine <Amount> deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "final-fee-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Cavab "final-payment.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "receiptNo" deyeri boş olmamalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "biller.id" deyeri <BillerId> beraberdir
* Json cavabında "subscriberNo" deyeri <SubscriberNo> beraberdir
* Json cavabında "cardId" deyeri "${cardId}" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "amount" deyeri <Amount> beraberdir
* Json cavabında "fee" deyeri <Fee> beraberdir
* Json cavabında "total" deyeri <Total> beraberdir
* Json cavabında "balanceAfter" deyeri <BalanceAfter> beraberdir
* Header "Location" movcud olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri <BalanceAfter> beraberdir
* Json cavabında "spentToday" deyeri <Total> beraberdir