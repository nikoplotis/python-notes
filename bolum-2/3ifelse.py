sayi = int(input("Sayi giriniz: ")) # kullanicidan sayi alip integer tipipne donusturup sayi degiskenin icine yaziyoruz
sayi2 = int(input("Sayi giriniz: ")) # kullanicidan sayi alip integer tipipne donusturup sayi2 degiskenin icine yaziyoruz
if sayi < sayi2 or sayi2 == sayi: # eger sayi2 sayi dan buyukse veya sayi2 ile sayi esit ise:
    print("birinci sayi ikinci sayidan kucuktur veya iki sayida esittir")

elif sayi > sayi2: # sayi sayi2 den buyukse:
    print("birinci sayi ikinci sayidan buyuktur")

else: # hicbiri degilse
    print("lutfen gecerli sayi giriniz")

number = int(input("lutfen 10'dan kucuk bir sayi giriniz: ")) # kullanicidan sayi alip integer tipipne donusturup number degiskenin icine yaziyoruz
if number < 10: # eger number 10 dan kucuk ise:
    print("tebrikler 10 dan kucuk bir sayi girdiniz")
else: # hicbiri dehilse:
    print("lutfen 10'dan kucuk bir sayi giriniz veya gecerli bir sayi giriniz")