sayi = 34 # bulunacak sayiyi belirliyoruz

while(True): # donguyu surekli devam ettirmesini sagliyoruz
    user = int(input("bir sayi giriniz")) # dongu devam ettigi surece kullanicidan veri alip integer a donusturup user a yazdiriyoruz
    if sayi > user: # eger sayi userdan buyukse:
        print("lutfen daha buyuk bir sayi giriniz")
    elif sayi < user: # eger sayi userden kucukse:
        print("lutfen daha kucuk bir sayi giriniz")
    else: # hicbiri degilse
        print("tebrikler buldun")
        break # donguyu durduruyoruz