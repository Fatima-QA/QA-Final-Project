# Bakcell — Tarif seçimi və detalları
tags: final-project, bakcell, ui, regression

## UI_BAK_001 — İstifadəçi seçdiyi tarifin detallarını görə bilməlidir
tags: smoke, tariffs

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell GO 11 Details Link" görsensin deye maksimum "30" saniye gözle
* "Bakcell GO 11 Details Link" elementine scroll et ve klik et
* "Bakcell Tariff Detail Title" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/go-11-99" olmalıdır
* "Bakcell Additional Information" elementine scroll et ve klik et
* "Bakcell Tariff Detail Title" elementinin metni "GO 11.99" olmalıdır
* Sehifede "GO 11.99 tarifinə keçmək üçün balansda minimum 11.99₼ olmalıdır." yazısı olmalıdır
* "Bakcell Tariff Activate Button" görsensin deye maksimum "10" saniye gözle
* "Bakcell Tariff Activate Button" aktiv olmalıdır
* Brauzeri bağla


## UI_BAK_002 — GO 17.99 seçildikdə uyğun tarifin detalları göstərilməlidir
tags: tariffs, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell GO 17 Details Link" görsensin deye maksimum "30" saniye gözle
* "Bakcell GO 17 Details Link" elementine scroll et ve klik et
* "Bakcell Tariff Detail Title" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/go-17-99" olmalıdır
* "Bakcell Tariff Detail Title" elementinin metni "GO 17.99" olmalıdır
* "Bakcell Tariff Activate Button" görsensin deye maksimum "10" saniye gözle
* "Bakcell Tariff Activate Button" aktiv olmalıdır
* Brauzeri bağla

## UI_BAK_003 — GO 29.99 seçildikdə uyğun tarifin detalları göstərilməlidir
tags: tariffs, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell GO 29 Details Link" görsensin deye maksimum "30" saniye gözle
* "Bakcell GO 29 Details Link" elementine scroll et ve klik et
* "Bakcell Tariff Detail Title" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/go-29-99" olmalıdır
* "Bakcell Tariff Detail Title" elementinin metni "GO 29.99" olmalıdır
* "Bakcell Tariff Activate Button" görsensin deye maksimum "10" saniye gözle
* "Bakcell Tariff Activate Button" aktiv olmalıdır
* Brauzeri bağla


## UI_BAK_004 — İstifadəçi mövcud xidmət barədə axtarış etdikdə uyğun nəticə görməlidir
tags: search, smoke, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Open Search" görsensin deye maksimum "20" saniye gözle
* "Bakcell Open Search" elementine klik et
* "Bakcell Search Input" görsensin deye maksimum "10" saniye gözle
* "Bakcell Search Input" elementine "eSIM" yaz
* "Bakcell Search Esim Result" görsensin deye maksimum "20" saniye gözle
* "Bakcell Search Esim Result" elementinin metni "eSIM nədir?" olmalıdır
* "Bakcell Search Input" input deyeri "eSIM" olmalıdır
* Brauzeri bağla

## UI_BAK_005 — Axtarışa uyğun məlumat olmadıqda istifadəçiyə aydın mesaj göstərilməlidir
tags: search, negative, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Open Search" görsensin deye maksimum "20" saniye gözle
* "Bakcell Open Search" elementine klik et
* "Bakcell Search Input" görsensin deye maksimum "10" saniye gözle
* "Bakcell Search Input" elementine "zzqafinal987654" yaz
* "Bakcell Search No Results" görsensin deye maksimum "20" saniye gözle
* "Bakcell Search No Results" elementinin metni "Məlumat tapılmadı" olmalıdır
* "Bakcell Search Input" input deyeri "zzqafinal987654" olmalıdır
* Brauzeri bağla


## UI_BAK_006 — İngilis dilinə keçdikdə seçilmiş tarif və tərcümə edilmiş məzmun göstərilməlidir
tags: language, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/go-11-99"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Current Language AZ" görsensin deye maksimum "20" saniye gözle
* "Bakcell Current Language AZ" elementine klik et
* "Bakcell English Language" görsensin deye maksimum "10" saniye gözle
* "Bakcell English Language" elementine klik et
* "Bakcell English Calls Heading" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/en/go-11-99" olmalıdır
* "Bakcell Tariff Detail Title" elementinin metni "GO 11.99" olmalıdır
* "Bakcell English Calls Heading" elementinin metni "Calls" olmalıdır
* Brauzeri bağla

## UI_BAK_007 — Rus dilinə keçdikdə seçilmiş tarif və tərcümə edilmiş məzmun göstərilməlidir
tags: language, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/go-11-99"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Current Language AZ" görsensin deye maksimum "20" saniye gözle
* "Bakcell Current Language AZ" elementine klik et
* "Bakcell Russian Language" görsensin deye maksimum "10" saniye gözle
* "Bakcell Russian Language" elementine klik et
* "Bakcell Russian Calls Heading" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/ru/go-11-99" olmalıdır
* "Bakcell Tariff Detail Title" elementinin metni "GO 11.99" olmalıdır
* "Bakcell Russian Calls Heading" elementinin metni "Звонки" olmalıdır
* Brauzeri bağla


## UI_BAK_008 — Həftəlik internet kateqoriyasında uyğun paket və aktivləşdirmə kodu göstərilməlidir
tags: internet, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/internet"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Weekly Category" görsensin deye maksimum "20" saniye gözle
* "Bakcell Weekly Category" elementine scroll et ve klik et
* "Bakcell Weekly Heading" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/weekly-packages" olmalıdır
* "Bakcell Weekly Package Volume" elementinin metni "2 GB" olmalıdır
* "Bakcell Weekly Activation Code" görünür olmalıdır
* "Bakcell Weekly Activation Code" elementinin "href" atributu "tel:*444*02%23" olmalıdır
* Brauzeri bağla

## UI_BAK_009 — Wi-Fi paketini seçən istifadəçi həmin paketin detalını və internet həcmini görə bilməlidir
tags: internet, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/internet"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Wifi20 Details" görsensin deye maksimum "20" saniye gözle
* "Bakcell Wifi20 Details" elementine scroll et ve klik et
* "Bakcell Wifi20 Breadcrumb" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/bakcell-wi-fi-20" olmalıdır
* "Bakcell Wifi20 Breadcrumb" elementinin metni "Bakcell Wi-Fi 20" olmalıdır
* Sehifede "20 GB" yazısı olmalıdır
* Sehifede "28 gün" yazısı olmalıdır
* "Bakcell Tariff Activate Button" görsensin deye maksimum "10" saniye gözle
* "Bakcell Tariff Activate Button" aktiv olmalıdır
* Brauzeri bağla


## UI_BAK_010 — Ölkəni axtarıb seçən istifadəçi həmin ölkənin rouminq operatorlarını görə bilməlidir
tags: roaming, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/roaming"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Roaming Country Input" görsensin deye maksimum "20" saniye gözle
* "Bakcell Roaming Country Input" elementine "Türkiyə" yaz
* "Bakcell Roaming Turkey Suggestion" görsensin deye maksimum "20" saniye gözle
* "Bakcell Roaming Turkey Suggestion" elementine klik et
* "Bakcell Roaming Turkey Heading" görsensin deye maksimum "20" saniye gözle
* URL "prices-and-countries?country=" içermelidir
* "Bakcell Roaming Turkey Heading" elementinin metni "Türkiyə" olmalıdır
* Sehifede "Turkcell Iletisim Hizmetleri A.S." yazısı olmalıdır
* Sehifede "Vodafone Telekomunikasyon A.S" yazısı olmalıdır
* Brauzeri bağla

## UI_BAK_011 — Rouminq ölkəsi dəyişdirildikdə əvvəlki ölkənin məlumatları yeni ölkənin məlumatları ilə əvəzlənməlidir
tags: roaming, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/prices-and-countries?country=T%C3%BCrkiy%C9%99"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Roaming Turkey Heading" görsensin deye maksimum "20" saniye gözle
* "Bakcell Roaming Georgia Choice" elementine scroll et ve klik et
* "Bakcell Roaming Georgia Heading" görsensin deye maksimum "20" saniye gözle
* "Bakcell Roaming Georgia Heading" elementinin metni "Gürcüstan" olmalıdır
* "Bakcell Roaming Turkey Heading" görünmemelidir
* Sehifede "Silknet JSC (Geocell Ltd)" yazısı olmalıdır
* Sehifede "Magticom Ltd" yazısı olmalıdır
* Brauzeri bağla


## UI_BAK_012 — Nömrə daxil edilmədikdə giriş davam etməməli və məcburi sahə mesajı göstərilməlidir
tags: login-validation, negative, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/login"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Login Phone" görsensin deye maksimum "20" saniye gözle
* "Bakcell Login Phone" elementini temizle
* "Bakcell Login Continue" elementine klik et
* "Bakcell Login Required Error" görsensin deye maksimum "10" saniye gözle
* "Bakcell Login Required Error" elementinin metni "Tələb olunur" olmalıdır
* URL "https://bakcell.com/login" olmalıdır
* "Bakcell Login Phone" görünür olmalıdır
* Brauzeri bağla


## UI_BAK_013 — Nəticəsiz axtarış dəyişdirildikdə uyğun nəticə göstərilməlidir
tags: search-recovery, regression

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Open Search" görsensin deye maksimum "20" saniye gözle
* "Bakcell Open Search" elementine klik et
* "Bakcell Search Input" görsensin deye maksimum "10" saniye gözle
* "Bakcell Search Input" elementine "zzqafinal987654" yaz
* "Bakcell Search No Results" görsensin deye maksimum "20" saniye gözle
* "Bakcell Search Input" elementini temizle
* "Bakcell Search Input" elementine "eSIM" yaz
* "Bakcell Search Esim Result" görsensin deye maksimum "20" saniye gözle
* "Bakcell Search Esim Result" elementinin metni "eSIM nədir?" olmalıdır
* "Bakcell Search No Results" görünmemelidir
* "Bakcell Search Input" input deyeri "eSIM" olmalıdır
* Brauzeri bağla


## UI_BAK_014 — Əlavə məlumat bölməsi açılıb bağlandıqda məzmunun görünməsi uyğun dəyişməlidir
tags: bakcell-final, accordion

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/go-11-99"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell Additional Information" görsensin deye maksimum "20" saniye gözle
* "Bakcell Additional Information" elementine scroll et ve klik et
* "xpath=//div[normalize-space()='- GO 11.99 tarifinə keçmək üçün balansda minimum 11.99₼ olmalıdır.']" görsensin deye maksimum "10" saniye gözle
* "Bakcell Additional Information" elementine scroll et ve klik et
* "xpath=//div[normalize-space()='- GO 11.99 tarifinə keçmək üçün balansda minimum 11.99₼ olmalıdır.']" yox olana qeder maksimum "10" saniye gözle
* "Bakcell Additional Information" görünür olmalıdır
* "Bakcell Additional Information" elementine klik et
* "xpath=//div[normalize-space()='- GO 11.99 tarifinə keçmək üçün balansda minimum 11.99₼ olmalıdır.']" görsensin deye maksimum "10" saniye gözle
* Brauzeri bağla

## UI_BAK_015 — Tarifdən geri qayıtdıqda başqa tarif seçmək mümkün olmalıdır
tags: bakcell-final, navigation

* "chrome" brauzeri aç ve keçid et "https://bakcell.com/"
* "Bakcell Advertisement Close" elementi "10" saniye içinde görünerse klik et
* "Bakcell GO 11 Details Link" görsensin deye maksimum "30" saniye gözle
* "Bakcell GO 11 Details Link" elementine scroll et ve klik et
* "Bakcell Tariff Detail Title" görsensin deye maksimum "20" saniye gözle
* "Bakcell Tariff Detail Title" elementinin metni "GO 11.99" olmalıdır
* Evvelki sehifeye qayıt
* "Bakcell Advertisement Close" elementi "3" saniye içinde görünerse klik et
* "Bakcell GO 17 Details Link" görsensin deye maksimum "30" saniye gözle
* "Bakcell GO 17 Details Link" elementine scroll et ve klik et
* "Bakcell Tariff Detail Title" görsensin deye maksimum "20" saniye gözle
* URL "https://bakcell.com/go-17-99" olmalıdır
* "Bakcell Tariff Detail Title" elementinin metni "GO 17.99" olmalıdır
* "Bakcell Tariff Activate Button" aktiv olmalıdır
* Brauzeri bağla