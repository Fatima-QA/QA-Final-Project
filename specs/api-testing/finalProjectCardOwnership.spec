# GRAD-202, GRAD-203 və GRAD-204 — Başqa istifadəçinin kartına giriş

## API_CARD_OWNER_001 — İstifadəçi başqasının kartını görə və onun vəziyyətini dəyişə bilməməlidir
tags: final-project, cards, regression, authorization

* Login Test User
* "cardOwnerToken" deyişenine "${token}" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "foreignCardId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/auth/login"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-login-user1.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Login cavabından accesTokeni yadda saxla "response"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${foreignCardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${foreignCardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-lost.json"
* Post request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${foreignCardId}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${foreignCardId}"
* Header elave et "Authorization" = "${cardOwnerToken}"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${foreignCardId}" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabında "availableBalance" deyeri "50" beraberdir