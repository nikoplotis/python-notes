a = ["ahmet" , "faruk" , "5" , "niko" , "nihad" , "mehmet" , "zlatan"] # listemizi olusturuyoruz
print(a[2]) # listemizin icindeki 
print(a[1:]) # 1'den baslayarak listenin sonuna kadar olan stringleri yazar
print(a[2::2]) # 2 kerede bir olan stringleri yazar
print(a[0:3]) # 0'dan baslayarak 3'e kadar olan stringleri yazar
print(len(a)) # a'nin karakter sayisini yazar
print(type(a)) # a'nin tipini yazar

b = ["nihad","faruk"] # listemizi olusturuyoruz
print(b) # listemizi yazdiriyoruz

b.append("feyzioglu") # listemize "feyzioglu" ekliyoruz
print(b) # listemizi yazdiriyoruz

b.remove("nihad") # listemizden "nihad" 'i cikartiyoruz
print(b) # listemizi yazdiriyoruz

a.append("feyzi") # listemize "feyzi" ekliyoruz
del (a[0]) # listemizdeki 0. stringi siliyoruz
print(a) # listemizi yazdiriyoruz
a.append("ahmet") # listemize "ahmet" ekliyoruz
print(a) # listemizi yazdiriyoruz






print(a.count("ahmet")) # kac tane oldugunu soyler

print(a+b) # a listesi ile b listesini yazdirir

a.sort() # alfabeye gore siralar
print(a) # listemizi yazdiriyoruz

a.reverse () # listemizi terse cevirir
print(a) # listemizi yazdiriyoruz