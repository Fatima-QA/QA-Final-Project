# Final layihəsi — Kommunal ödənişlər

## API_PAY_001 — İstifadəçi ödəniş edə biləcəyi xidmət təminatçılarını görə bilməlidir
tags: final-project, payments, positive, smoke, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/billers"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Cavab body-sinde "Bakcell" olmalıdır
* Cavab body-sinde "Azercell" olmalıdır

## API_PAY_002 — Ödəniş balansdan bir dəfə çıxılmalı və eyni sorğunun təkrarı ikinci ödəniş yaratmamalıdır
tags: final-project, payments, positive, smoke, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Save value of "id" as "cardId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "final-payment-002"
* Add body as file resource "final-payment.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "paymentId"
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "40" beraberdir
* Header "Location" movcud olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "40" beraberdir
* Json cavabında "spentToday" deyeri "10" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add as a header "Idempotency-Key" = "final-payment-002"
* Add body as file resource "final-payment.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${paymentId}" beraberdir
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "balanceAfter" deyeri "40" beraberdir
* Header "Idempotent-Replay" deyerinde "true" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "40" beraberdir
* Json cavabında "spentToday" deyeri "10" beraberdir