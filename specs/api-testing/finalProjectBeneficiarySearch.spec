# GRAD-102 — Alıcı axtarışı və sıralama

* Final axtarış alıcılarını hazırla

## API_BEN_019 — İstifadəçi alıcını ləqəbinə görə tapa bilməlidir
tags: final-project, beneficiaries, positive, regression

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "Dostum"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].id" deyeri "${secondId}" beraberdir

## API_BEN_020 — Axtarış I, İ və ı hərflərinin fərqindən asılı olmamalıdır
tags: final-project, beneficiaries, positive, regression

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "işıq"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "${firstId}" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "q" = "İŞIQ"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "${firstId}" beraberdir

## API_BEN_021 — Adlar Azərbaycan əlifbasına uyğun sıralanmalıdır
tags: final-project, beneficiaries, positive, regression

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${firstId}" beraberdir
* Json cavabında "items[1].id" deyeri "${secondId}" beraberdir

## API_BEN_022 — Alıcılar yaradılma tarixinə görə hər iki istiqamətdə sıralana bilməlidir
tags: final-project, beneficiaries, positive, regression

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "sort" = "createdAt"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${firstId}" beraberdir
* Json cavabında "items[1].id" deyeri "${secondId}" beraberdir

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Query parametri elave et "sort" = "createdAt"
* Query parametri elave et "order" = "desc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${secondId}" beraberdir
* Json cavabında "items[1].id" deyeri "${firstId}" beraberdir

## API_BEN_023 — Standart siyahıda ən yeni alıcı əvvəl göstərilməlidir
tags: final-project, beneficiaries, positive, regression

* Initalize request specification
* Set base Url to "https://api.anarabbas.com"
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "token"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items[0].id" deyeri "${secondId}" beraberdir
* Json cavabında "items[1].id" deyeri "${firstId}" beraberdir