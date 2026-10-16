# GRAD-201 — Kartın bağlı olduğu hesabın yoxlanılması

| AccountId | Status | ErrorCode |
|-----------|--------|-----------|
| acc_002 | 403 | FORBIDDEN |
| acc_nonexistent | 404 | ACCOUNT_NOT_FOUND |

## API_CARD_ACCOUNT_001 — İstifadəçi yalnız özünün mövcud hesabına kart yarada bilməlidir
tags: final-project, cards, regression, negative

* Login Test User
* "testAccountId" deyişenine <AccountId> deyerini ver
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/cards"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-card-account-check.json"
* Post request and display respons
* Status kodunun <Status> olmalıdır
* Json cavabında "code" deyeri <ErrorCode> beraberdir