not1 = int(input("1. notunuzu giriniz: ")) # kullanicidan veri alip integer tipine donusturup not1 degiskenine tanimliyoruz
not2 = int(input("2. notunuzu giriniz: ")) # kullanicidan veri alip integer tipine donusturup not2 degiskenine tanimliyoruz
not3 = int(input("3. notunuzu giriniz: ")) # kullanicidan veri alip integer tipine donusturup not3 degiskenine tanimliyoruz

toplam = not1 + not2 + not3 # not1 not2 not3u toplayim toplam a yazdiriyoruz
ortalama = toplam // 3 # toplami 3 e noktasiz sekilde bolup ortalamaya yazdiriypriz

if (not1 or not2 or not3) >= 0 and (not1 or not2 or not3) <= 100: # eger not1 veya not2 veya not3 0 dan buyuk veya esitse ve not1 veya not2 veya not3 100 den kucukse veya esitse:
    if ortalama >= 50: # eger ortalama 50 den buyuk veya kucukse:
        print("ortalamanız:" , ortalama)
        print("dersten geçtiniz")
    else: # degilse
        print("ortalamanız:" , ortalama)
        print("dersten geçemediniz")

else: # degilse
    print("lutfen gecerli sayı giriniz")


