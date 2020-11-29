kullaniciadi = "nikoplotis" # kullaniciadi nin icine nikoplotis yazdiriyoruz
sifre = "1234" # sifre nin icine 1234 yazdiriyoruz

username = input("kullanici adinizi giriniz: ") # kullanicidan veri alip username e yazdiriyoruz
password = input("sifrenizi giriniz") # kullanicidan veri alip password e yazdiriyoruz

if sifre == password: # eger sifre password e esitse:
   if username == kullaniciadi: # eger username kullanici adina esite:
       print("tebrikler giris yaptiniz")

   else: # hicbir durum gecerli degilse :
       print("lutfen tekrar deneyiniz")

else:print("lutfen tekrar deneyiniz") # hicbir durum gecerli degilse :





