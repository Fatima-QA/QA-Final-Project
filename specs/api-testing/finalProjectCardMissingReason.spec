# GRAD-203 — Bloklama səbəbinin məcburiliyi

## API_CARD_BLOCK_VALIDATION_002 — Səbəb göstərilmədikdə kart bloklanmamalıdır
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
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.find { it.field == 'reason' }.message" deyeri boş olmamalıdır

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