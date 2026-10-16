# Bakcell Shop — Əsas alış axınları
tags: final-project, bakcell-shop, ui, regression

## UI_SHOP_001 — İstifadəçi məhsulu adı ilə axtarıb həmin məhsulun detallarına keçə bilməlidir
tags: shop-search, smoke

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* URL "/az/search?" içermelidir
* "Shop TCL Search Result" elementinin metni "Televizor TCL 55P755 4K UHD Google TV" olmalıdır
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* URL "/az/Televizorlar/TCL-55P755" içermelidir
* "Shop Product Detail Title" elementinin metni "Televizor TCL 55P755 4K UHD Google TV" olmalıdır
* "Shop Product Code" görünür olmalıdır
* "Shop Product Code" elementin içinde "207-0003" yazısı var
* Brauzeri bağla

## UI_SHOP_002 — Axtarışa uyğun məhsul olmadıqda boş nəticə mesajı göstərilməlidir
tags: shop-search, negative

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "zzqafinal987654" yaz ve Enter düymesine bas
* "Shop No Results" görsensin deye maksimum "30" saniye gözle
* URL "search=zzqafinal987654" içermelidir
* "Shop No Results" elementinin metni "Nəticə tapılmadı" olmalıdır
* Sehifede "0 məhsul" yazısı olmalıdır
* "Shop Product Cards" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla


## UI_SHOP_003 — Nəticəsiz axtarışdan sonra sorğu dəyişdirildikdə uyğun məhsul göstərilməlidir
tags: shop-search, recovery

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "zzqafinal987654" yaz ve Enter düymesine bas
* "Shop No Results" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementini temizle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementinin metni "Televizor TCL 55P755 4K UHD Google TV" olmalıdır
* "Shop No Results" görünmemelidir
* "Shop Search Input" input deyeri "TCL 55P755" olmalıdır
* Brauzeri bağla


## UI_SHOP_004 — 256 GB yaddaş filtri seçildikdə yalnız uyğun yaddaşlı məhsullar göstərilməlidir
tags: shop-filter

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "Samsung" yaz ve Enter düymesine bas
* "Shop Samsung 128 Product" görsensin deye maksimum "30" saniye gözle
* "Shop Memory 256 Label" elementine scroll et ve klik et
* "Shop Memory 256 Checkbox" seçilmiş olmalıdır
* "Shop Samsung 128 Product" yox olana qeder maksimum "30" saniye gözle
* "Shop Samsung 256 Product" görsensin deye maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı en az "1" olmalıdır
* "Shop Products Outside 256" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## UI_SHOP_005 — Filtrlər sıfırlandıqda yaddaş məhdudiyyəti götürülməli və digər məhsullar yenidən göstərilməlidir
tags: shop-filter

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "Samsung" yaz ve Enter düymesine bas
* "Shop Samsung 128 Product" görsensin deye maksimum "30" saniye gözle
* "Shop Memory 256 Label" elementine scroll et ve klik et
* "Shop Memory 256 Checkbox" seçilmiş olmalıdır
* "Shop Samsung 128 Product" yox olana qeder maksimum "30" saniye gözle
* "Shop Clear Filters" elementine scroll et ve klik et
* "Shop Memory 256 Checkbox" seçilmemiş olmalıdır
* "Shop Search Input" input deyeri "" olmalıdır
* URL "https://shop.bakcell.com/az/search?category=all" olmalıdır
* "Shop Apple Brand Checkbox" görsensin deye maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı en az "1" olmalıdır
* Brauzeri bağla


## UI_SHOP_006 — Televizor kateqoriyası seçildikdə yalnız televizorlar göstərilməlidir
tags: shop-category-brand

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az/search?category=all"
* "Shop TV Category" görsensin deye maksimum "30" saniye gözle
* "Shop TV Category" elementine scroll et ve klik et
* "Shop TV Category Heading" görsensin deye maksimum "30" saniye gözle
* URL "category=Televizorlar-12" içermelidir
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı en az "1" olmalıdır
* "Shop Non TV Products" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## UI_SHOP_007 — TCL brendi seçildikdə yalnız həmin brendin məhsulları göstərilməlidir
tags: shop-category-brand

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az/search?category=all"
* "Shop TCL Brand Label" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Brand Label" elementine scroll et ve klik et
* "Shop TCL Brand Checkbox" seçilmiş olmalıdır
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı en az "1" olmalıdır
* "Shop Non TCL Products" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla


## UI_SHOP_008 — Məhsul səbətə əlavə edildikdə adı, miqdarı və cəmi düzgün göstərilməlidir
tags: shop-cart, smoke

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* "Shop Detail Add To Cart" elementine scroll et ve klik et
* "Shop Cart Has Items" görsensin deye maksimum "20" saniye gözle
* "Shop Open Cart" elementine scroll et ve klik et
* "Shop View Cart" görsensin deye maksimum "20" saniye gözle
* "Shop View Cart" elementine klik et
* "Shop Cart Quantity" görsensin deye maksimum "30" saniye gözle
* URL "/az/view-cart" içermelidir
* "Shop Product Detail Title" elementinin metni "Televizor TCL 55P755 4K UHD Google TV" olmalıdır
* "Shop Cart Quantity" elementinin metni "1" olmalıdır
* "Shop Cart Total" elementinin metni "720,00 ₼" olmalıdır
* Brauzeri bağla

## UI_SHOP_009 — Səbətdə miqdar artırılıb azaldıldıqda cəmi məbləğ uyğun yenilənməlidir
tags: shop-cart

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* "Shop Detail Add To Cart" elementine scroll et ve klik et
* "Shop Cart Has Items" görsensin deye maksimum "20" saniye gözle
* "Shop Open Cart" elementine scroll et ve klik et
* "Shop View Cart" görsensin deye maksimum "20" saniye gözle
* "Shop View Cart" elementine klik et
* "Shop Cart Quantity" görsensin deye maksimum "30" saniye gözle
* "Shop Cart Quantity" elementinin metni "1" olmalıdır
* "Shop Cart Plus" elementine scroll et ve klik et
* "Shop Cart Quantity" elementinin metni "2" olmalıdır
* "Shop Cart Total" elementinin metni "1440,00 ₼" olmalıdır
* "Shop Cart Minus" elementine klik et
* "Shop Cart Quantity" elementinin metni "1" olmalıdır
* "Shop Cart Total" elementinin metni "720,00 ₼" olmalıdır
* Brauzeri bağla


## UI_SHOP_010 — Səbətdən silmə ləğv ediləndə məhsul qalmalı, təsdiqlənəndə silinməlidir
tags: shop-cart-delete

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* "Shop Detail Add To Cart" elementine scroll et ve klik et
* "Shop Cart Has Items" görsensin deye maksimum "20" saniye gözle
* "Shop Open Cart" elementine scroll et ve klik et
* "Shop View Cart" görsensin deye maksimum "20" saniye gözle
* "Shop View Cart" elementine klik et
* "Shop Cart Quantity" görsensin deye maksimum "30" saniye gözle
* "Shop Cart Remove" elementine scroll et ve klik et
* "Shop Cart Delete Confirmation" görsensin deye maksimum "10" saniye gözle
* "Shop Cart Cancel Delete" elementine klik et
* "Shop Cart Delete Confirmation" yox olana qeder maksimum "10" saniye gözle
* "Shop Product Detail Title" görünür olmalıdır
* "Shop Cart Quantity" elementinin metni "1" olmalıdır
* "Shop Cart Total" elementinin metni "720,00 ₼" olmalıdır
* "Shop Cart Remove" elementine klik et
* "Shop Cart Confirm Delete" görsensin deye maksimum "10" saniye gözle
* "Shop Cart Confirm Delete" elementine klik et
* "Shop Empty Cart" görsensin deye maksimum "20" saniye gözle
* "Shop Empty Cart" elementinin metni "Səbət boşdur" olmalıdır
* "Shop Product Detail Title" sehifede mövcud olmamalıdır
* Brauzeri bağla


## UI_SHOP_011 — Bir kliklə alışda nömrə boş olduqda davam etmək mümkün olmamalıdır
tags: shop-form, negative

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* "Shop Quick Buy" elementine scroll et ve klik et
* "Shop Quick Buy Heading" görsensin deye maksimum "20" saniye gözle
* "Shop Quick Buy Phone" input deyeri "" olmalıdır
* "Shop Quick Buy Continue" deaktiv olmalıdır
* URL "/az/Televizorlar/TCL-55P755" içermelidir
* Brauzeri bağla

## UI_SHOP_012 — Bir kliklə alışda natamam nömrə daxil edildikdə davam etmək mümkün olmamalıdır
tags: shop-form, negative

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* "Shop Quick Buy" elementine scroll et ve klik et
* "Shop Quick Buy Phone" görsensin deye maksimum "20" saniye gözle
* "Shop Quick Buy Phone" elementine "55123" yaz
* "Shop Quick Buy Continue" deaktiv olmalıdır
* "Shop Quick Buy Heading" görünür olmalıdır
* URL "/az/Televizorlar/TCL-55P755" içermelidir
* Brauzeri bağla


## UI_SHOP_013 — Qalereyada şəkil seçildikdə əsas məhsul şəkli uyğun dəyişməlidir
tags: shop-final

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Selected Image" görsensin deye maksimum "30" saniye gözle
* "Shop Thumbnail One" elementinin "src" atributunu "firstImage" olaraq yadda saxla
* "Shop Thumbnail Two" elementinin "src" atributunu "secondImage" olaraq yadda saxla
* "Shop Thumbnail Two" elementine scroll et ve klik et
* "Shop Selected Image" elementinin "src" atributu "${secondImage}" olmalıdır
* "Shop Thumbnail One" elementine scroll et ve klik et
* "Shop Selected Image" elementinin "src" atributu "${firstImage}" olmalıdır
* Brauzeri bağla

## UI_SHOP_014 — Məhsulun siyahıda göstərilən satış qiyməti detal səhifəsində qorunmalıdır
tags: shop-final

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Card Price" elementinin metnini "listedPrice" olaraq yadda saxla
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* "Shop Detail Price" elementinin metni "${listedPrice}" olmalıdır
* Brauzeri bağla

## UI_SHOP_015 — Məhsul detalından geri qayıdıb səhifəni yenilədikdə axtarış nəticəsi əlçatan qalmalıdır
tags: shop-final

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az"
* "Shop Search Input" görsensin deye maksimum "30" saniye gözle
* "Shop Search Input" elementine "TCL 55P755" yaz ve Enter düymesine bas
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementine scroll et ve klik et
* "Shop Product Detail Title" görsensin deye maksimum "30" saniye gözle
* Evvelki sehifeye qayıt
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* URL "search=TCL" içermelidir
* "Shop Search Input" input deyeri "TCL 55P755" olmalıdır
* Sehifeni yenile
* "Shop TCL Search Result" görsensin deye maksimum "30" saniye gözle
* "Shop TCL Search Result" elementinin metni "Televizor TCL 55P755 4K UHD Google TV" olmalıdır
* "Shop Search Input" input deyeri "TCL 55P755" olmalıdır
* Brauzeri bağla


## UI_SHOP_016 — Brend və yaddaş birlikdə seçildikdə məhsullar hər iki filtrə uyğun olmalıdır
tags: shop-combined-filter

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az/search?category=all"
* "Shop Apple Brand Label" görsensin deye maksimum "30" saniye gözle
* "Shop Apple Brand Label" elementine scroll et ve klik et
* "Shop Apple Brand Checkbox" seçilmiş olmalıdır
* "Shop Apple 128 Product" görsensin deye maksimum "30" saniye gözle
* "Shop Non Apple Products" elementlerinin sayı "0" olmalıdır
* "Shop Memory 256 Label" elementine scroll et ve klik et
* "Shop Memory 256 Checkbox" seçilmiş olmalıdır
* "Shop Apple 128 Product" yox olana qeder maksimum "30" saniye gözle
* "Shop Apple Brand Checkbox" seçilmiş olmalıdır
* "Shop Product Cards" elementlerinin sayı en az "1" olmalıdır
* "Shop Non Apple Products" elementlerinin sayı "0" olmalıdır
* "Shop Products Outside 256" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla


## UI_SHOP_017 — Qiymət intervalı seçildikdə yalnız həmin aralıqdakı məhsullar göstərilməlidir
tags: shop-price-range

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az/search?category=all"
* "Shop Price Range 101 500" görsensin deye maksimum "30" saniye gözle
* "Shop Prices Outside Range" görsensin deye maksimum "30" saniye gözle
* "Shop Price Range 101 500" elementine scroll et ve klik et
* "Shop Prices Outside Range" yox olana qeder maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı en az "1" olmalıdır
* "Shop Prices Outside Range" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla


## UI_SHOP_018 — Daha çox yükləndikdə yeni məhsullar əlavə edilməli və əvvəlkilər qorunmalıdır
tags: shop-load-more

* "chrome" brauzeri aç ve keçid et "https://shop.bakcell.com/az/search?category=all"
* "Shop Load More" görsensin deye maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı "9" olmalıdır
* "xpath=(//h4[ancestor::*[@role='button']])[1]" elementinin metnini "firstProductBeforeLoad" olaraq yadda saxla
* "Shop Load More" elementine scroll et ve klik et
* "Shop Tenth Product" görsensin deye maksimum "30" saniye gözle
* "Shop Product Cards" elementlerinin sayı en az "10" olmalıdır
* "xpath=(//h4[ancestor::*[@role='button']])[1]" elementinin metni "${firstProductBeforeLoad}" olmalıdır
* Brauzeri bağla
