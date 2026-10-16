# GRAD-303 — Ödəniş tarixçəsi və səhifələmə

## API_PAY_HISTORY_001 — İstifadəçi ödənişlərini tarixçədə görə, karta görə süzə və səhifələrə bölə bilməlidir
tags: final-project, payments, regression, history

* Login Test User

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "cardId"
* Save value of "id" as "firstCardId"

* "testBillerId" deyişenine "bakcell" deyerini ver
* "testSubscriberNo" deyişenine "551234567" deyerini ver
* "paymentAmount" deyişenine "10" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "history-first-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "firstPaymentId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "cardId"
* Save value of "id" as "secondCardId"

* "paymentAmount" deyişenine "11" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Header elave et "Idempotency-Key" = "history-second-${cardId}"
* Add body as file resource "final-payment-fee.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "secondPaymentId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${secondPaymentId}" beraberdir
* Json cavabında "items[1].id" deyeri "${firstPaymentId}" beraberdir
* Json cavabında "items[0].amount" deyeri "11" beraberdir
* Json cavabında "items[1].amount" deyeri "10" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "cardId" = "${firstCardId}"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].id" deyeri "${firstPaymentId}" beraberdir
* Json cavabında "items[0].amount" deyeri "10" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "1"
* Query parametri elave et "limit" = "1"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].id" deyeri "${secondPaymentId}" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "2"
* Query parametri elave et "limit" = "1"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].id" deyeri "${firstPaymentId}" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "token"
* Query parametri elave et "page" = "3"
* Query parametri elave et "limit" = "1"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır