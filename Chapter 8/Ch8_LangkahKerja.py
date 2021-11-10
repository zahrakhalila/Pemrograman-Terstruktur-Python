#CHAPTER 8 LANGKAH KERJA

#No 1: Membuat list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#No 2: Sisipkan nilai 10 ke dalam indeks ke 3 dari a dan 15 ke dalam indeks ke 2 dari b
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)

#No 3: Sisipkan nilai 4 ke indeks terakhir dari a dan 8 ke indeks terakhir dari b
a.append(4)
b.append(8)
print(a)
print(b)

#No 4: Lakukan sorting secara ascending pada list a dan b
a.sort()
b.sort()
print(a)
print(b)

#No 5: Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)
c = a[:8]
d = b[2:10]
print(c)
print(d)

#No 6: Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya
e = []
for i in range(len(c)):
    e.append(c[i] + d[i])
print(e)

#No 7: Ubahlah list e ke dalam tuple
tupleE = tuple(e)
print(tupleE)

#No 8: Carilah nilai min, maks, dan jumlahan seluruh elemen dari e
print(min(tupleE))
print(max(tupleE))
print(sum(tupleE))

#No 9: Buatlah sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”
myString = 'python adalah bahasa pemrograman yang menyenangkan'

#No 10: Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut
hurufPenyusun = set(myString)
print(hurufPenyusun)

#No 11: Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list
listHuruf = list(myString)
print(listHuruf)
listHuruf.sort()
print(listHuruf)
