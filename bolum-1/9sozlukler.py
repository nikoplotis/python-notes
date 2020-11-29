notlar = {"niko":15, "faruk":20} # tirnak icinde belirttigimiz degerimizin anahtaridir
print(notlar["niko"]) # anahtarimizi girerek 15 sonucunu aliyoruz
print(type(notlar)) # notlar adli degiskenin tipini ogrenoyoruz
# sozluklerde siralama yoktur rastgele sirada verir
notlar["feyzi"] = 25 # sozlugumuze 25 degerini
print(notlar) # notlar adli degiskenimizi yazdiriyorz
notlar.pop("faruk") # pop ile faruk anahtarini sozlukten cikartiyoruz
print(notlar) # notlar adli degiskenimizi yazdiriyorz
notlar.popitem() # rastgele birtane cikartiyoruz
print(notlar) # notlar adli degiskenimizi yazdiriyorz
notlar2 = notlar.copy() # copy ile notlar sozlugunu notlar2 sozlugune aktariyoruz
print(notlar2) # notlar 2 adli degiskeni yazdiriyoruz
notlar.clear() # sozlugu temizliyoruz
print(notlar) # notlar adli degiskenimizi yazdiriyorz