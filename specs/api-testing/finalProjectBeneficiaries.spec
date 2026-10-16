# Final layihəsi — Benefisiarlar

## API_BEN_001 — İstifadəçi keçərli məlumatlarla benefisiar yarada bilməlidir
tags: final-project, beneficiaries, positive, smoke, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Cavab "final-beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Save value of "id" as "cardId"
* Save value of "id" as "cardId"
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "fullName" deyeri "Fatima Test" beraberdir
* Json cavabında "iban" deyeri "AZ12TEST00000000000000000001" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "nickname" deyeri "Final QA" beraberdir
* Json cavabında "createdAt" deyeri boş olmamalıdır
* Header "Location" movcud olmalıdır

## API_BEN_002 — Məcburi məlumatlar daxil edilmədikdə benefisiar yaradılmamalıdır
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" deyeri boş olmamalıdır
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır
* Json cavabında "details.find { it.field == 'iban' }.message" deyeri boş olmamalıdır
* Json cavabında "details.find { it.field == 'currency' }.message" deyeri boş olmamalıdır

## API_BEN_003 — Token olmadan benefisiar yaratmaq mümkün olmamalıdır
tags: final-project, beneficiaries, negative, regression

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Json cavabında "error" deyeri boş olmamalıdır

## API_BEN_004 — Eyni IBAN ilə təkrar benefisiar yaradılmamalıdır
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## API_BEN_005 — Boşluqlu və kiçik hərfli IBAN normallaşdırılmalı, verilməyən ləqəb null saxlanmalıdır
tags: final-project, beneficiaries, positive, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-normalized.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "iban" deyeri "AZ12TEST00000000000000000001" beraberdir
* Json cavabında "ibanMasked" deyeri "AZ12 **** **** **** **** 0001" beraberdir
* Json cavabında "nickname" açarı mövcud olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır
* Json cavabında "currency" deyeri "AZN" beraberdir

## API_BEN_006 — İstifadəçi öz hesabını alıcı kimi əlavə edə bilməməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-own.json"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "OWN_ACCOUNT" beraberdir

## API_BEN_007 — Yeni sessiyada alıcılar siyahısı boş görünməlidir
tags: final-project, beneficiaries, positive, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## API_BEN_008 — Mövcud olmayan alıcının silinməsi rədd edilməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries/ben_00000000"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## API_BEN_009 — Yaradılmış alıcı siyahıda görünməli və silindikdən sonra əlçatan olmamalıdır
tags: final-project, beneficiaries, positive, smoke, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "beneficiaryId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].id" deyeri "${beneficiaryId}" beraberdir
* Json cavabında "items[0].iban" deyeri "AZ12TEST00000000000000000001" beraberdir
* Json cavabında "items[0].fullName" deyeri "Fatima Test" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries/${beneficiaryId}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "204" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries/${beneficiaryId}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## API_BEN_010 — Alıcı axtarış və valyuta şərtlərinin hər ikisinə uyğun olduqda göstərilməlidir
tags: final-project, beneficiaries, positive, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "beneficiaryId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "fatima"
* Query parametri elave et "currency" = "AZN"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].id" deyeri "${beneficiaryId}" beraberdir
* Json cavabında "items[0].currency" deyeri "AZN" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "fatima"
* Query parametri elave et "currency" = "USD"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "NoMatchingRecipient"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## API_BEN_011 — İstifadə olunan ləqəb fərqli hərf ölçüsü ilə təkrar qəbul edilməməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-duplicate-nickname.json"
* Post request and display respons
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NICKNAME_TAKEN" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].iban" deyeri "AZ12TEST00000000000000000001" beraberdir

## API_BEN_012 — Alıcılar ada görə artan və azalan qaydada sıralana bilməlidir
tags: final-project, beneficiaries, positive, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "fatimaId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-second.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Save value of "id" as "aliId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${aliId}" beraberdir
* Json cavabında "items[1].id" deyeri "${fatimaId}" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "desc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${fatimaId}" beraberdir
* Json cavabında "items[1].id" deyeri "${aliId}" beraberdir

## API_BEN_013 — Başqa istifadəçi alıcını silə bilməməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "foreignBeneficiaryId"
* "ownerToken" deyişenine "${token}" deyerini ver

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/auth/login"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-login-user1.json"
* Post request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "user.email" deyeri "user1@test.com" beraberdir
* Login cavabından accesTokeni yadda saxla "response"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries/${foreignBeneficiaryId}"
* Add as a header "Authorization" = "token"
* Delete request and display response
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Header elave et "Authorization" = "${ownerToken}"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "${foreignBeneficiaryId}" beraberdir

## API_BEN_014 — Etibarsız JSON göndərildikdə alıcı yaradılmamalıdır
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as text "{"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## API_BEN_015 — Token olmadan mövcud alıcı silinməməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Save value of "id" as "beneficiaryId"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries/${beneficiaryId}"
* Delete request and display response
* Status kodunun "401" olmalıdır
* Json cavabında "error" deyeri boş olmamalıdır

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "${beneficiaryId}" beraberdir



## API_BEN_016 — On alıcıdan sonra yeni alıcı əlavə edilməsi rədd edilməlidir
tags: final-project, beneficiaries, bva, regression

* Login Test User
* Final limit alıcısını yarat "01"
* Final limit alıcısını yarat "02"
* Final limit alıcısını yarat "03"
* Final limit alıcısını yarat "04"
* Final limit alıcısını yarat "05"
* Final limit alıcısını yarat "06"
* Final limit alıcısını yarat "07"
* Final limit alıcısını yarat "08"
* Final limit alıcısını yarat "09"
* Final limit alıcısını yarat "10"

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır
* Json cavabında "items.id" siyahısındakı deyerler unikal olmalıdır

* "limitSuffix" deyişenine "11" deyerini ver
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-limit.json"
* Post request and display respons
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "LIMIT_REACHED" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır

## API_BEN_017 — Açıq şəkildə boş göndərilən ləqəb rədd edilməlidir
tags: final-project, beneficiaries, negative, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-empty-nickname.json"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.find { it.field == 'nickname' }.message" deyeri boş olmamalıdır

## API_BEN_018 — Adın kənar boşluqları təmizlənməli və EUR valyutası qəbul edilməlidir
tags: final-project, beneficiaries, positive, regression

* Login Test User
* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "final-beneficiary-trim.json"
* Post request and display respons
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Al" beraberdir
* Json cavabında "currency" deyeri "EUR" beraberdir
* Json cavabında "nickname" açarı mövcud olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır