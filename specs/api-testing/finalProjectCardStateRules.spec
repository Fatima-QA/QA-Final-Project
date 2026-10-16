# GRAD-203 və GRAD-204 — Kartın statusuna uyğun əməliyyat qaydaları

## API_CARD_STATE_001 — Dondurulmuş kart təkrar dondurula bilməməlidir
tags: final-project, cards, regression, state-transition

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
* Json cavabında "status" deyeri "FROZEN" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-freeze.json"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "ALREADY_FROZEN" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir


## API_CARD_STATE_002 — Dondurulmuş kart itirildikdə daimi bloklana bilməlidir
tags: final-project, cards, regression, state-transition

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
* Json cavabında "status" deyeri "FROZEN" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-lost.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
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


## API_CARD_STATE_003 — Daimi bloklanmış kart yenidən dondurula bilməməlidir
tags: final-project, cards, regression, state-transition

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
* Json cavabında "status" deyeri "BLOCKED" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-freeze.json"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir


## API_CARD_STATE_004 — Aktiv kart üçün blokdan çıxarma əməliyyatı rədd edilməlidir
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
* Add Endpoint "/cards/${cardId}/unblock"
* Add as a header "Authorization" = "token"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NOT_FROZEN" beraberdir

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