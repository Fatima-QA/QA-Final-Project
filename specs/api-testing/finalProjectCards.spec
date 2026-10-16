# Final layihəsi — Virtual kartlar

## API_CARD_001 — İstifadəçi öz hesabına virtual kart yarada və məlumatlarını görə bilməlidir
tags: final-project, cards, positive, smoke, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Cavab "final-card.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Save value of "id" as "cardId"
* Json cavabında "accountId" deyeri "acc_001" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "label" deyeri "Final QA" beraberdir
* Json cavabında "limits.dailyOnline" deyeri "500" beraberdir
* Json cavabında "limits.perTransaction" deyeri "300" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir
* Header "Location" movcud olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "accountId" deyeri "acc_001" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "label" deyeri "Final QA" beraberdir

## API_CARD_002 — Məcburi məlumatlar olmadan virtual kart yaradılmamalıdır
tags: final-project, cards, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.find { it.field == 'accountId' }.message" deyeri boş olmamalıdır
* Json cavabında "details.find { it.field == 'initialAmount' }.message" deyeri boş olmamalıdır

## API_CARD_003 — Müvəqqəti bloklanan kart yenidən aktivləşdirilə bilməlidir
tags: final-project, cards, positive, smoke, regression

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
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-freeze.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" açarı mövcud olmalıdır
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" açarı mövcud olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabında "availableBalance" deyeri "50" beraberdir

## API_CARD_004 — İtirilmiş kart daimi bloklanmalı və blokdan çıxarılmamalıdır
tags: final-project, cards, negative, regression

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
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-lost.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir