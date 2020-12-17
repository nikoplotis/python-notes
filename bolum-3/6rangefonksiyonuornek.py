while True: #dongumuzu surekli olacak sekilde baslatiyoruz
    parola = input("Parola: ")

    if not parola: # eger parola bossa:
        print("parola bos gecilemez")
    elif len(parola) in range(3,8): # parola uzunlugu 3 ile 8 arasinda ise
        print("kaydedildi", parola)
        break #dongu durdurukur
    else: #degilse:
        print("tekrar dene")