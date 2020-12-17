def user(isim,soyisim,sehir,meslek):
    print("-"*30)
    print("Isminiz: " + isim + "\nSoyisminiz: " + soyisim + "\nSehriniz: " + sehir + "\nMesleginiz: " + meslek)
    print("-" * 30)

name = input("isminizi giriniz: ")
surname = input("soyisminizi giriniz: ")
location = input("Sehrinizi giriniz: ")
job = input("Mesleginizi giriniz: ")


user(name , surname , location , job)