# GRAD-201 və GRAD-202 — Kartlara giriş və kart sayı limiti

## API_CARD_ACCESS_001 — Token olmadan kart məlumatları əldə edilə bilməməlidir
tags: final-project, cards, regression, negative

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

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Get request and display respons
* Status kodunun "401" olmalıdır
* Json cavabında "error" deyeri boş olmamalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir


## API_CARD_ACCESS_002 — Mövcud olmayan kart üçün məlumat qaytarılmamalıdır
tags: final-project, cards, regression, negative

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/vcd_00000000"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir


## API_CARD_LIMIT_001 — Üç aktiv və ya dondurulmuş kart olduqda yeni kart yaradılmamalı, daimi bloklamadan sonra yaradılmalıdır
tags: final-project, cards, regression, boundary

* Login Test User

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "firstCardId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "secondCardId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "thirdCardId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${firstCardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-freeze.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${firstCardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-lost.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${firstCardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir