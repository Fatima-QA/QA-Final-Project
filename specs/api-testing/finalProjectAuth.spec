# Final layihəsi — Hesablara giriş

## API_AUTH_001 — Token olmadan hesab məlumatları əldə edilə bilməməlidir
tags: final-project, auth, negative, regression

* API e GET request gönder "https://api.anarabbas.com/me/accounts"
* Status kodunun "401" olmalıdır

## API_AUTH_002 — Daxil olmuş istifadəçi öz hesablarını görə bilməlidir
tags: final-project, auth, positive, smoke, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/me/accounts"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında verilen "total" deyeri ededdir
* Json cavabında "data[0].id" deyeri boş olmamalıdır
* Json cavabında "data[0].currency" deyeri boş olmamalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "data[0].id" deyeri "acc_001" beraberdir
* Json cavabında "data[0].currency" deyeri "AZN" beraberdir
* Json cavabında "data[0].owner.id" deyeri "1" beraberdir
* Json cavabında "data[0].owner.email" deyeri "admin@test.com" beraberdir