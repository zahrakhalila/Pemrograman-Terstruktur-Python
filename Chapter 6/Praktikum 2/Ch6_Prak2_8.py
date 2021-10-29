def luasSegitiga(a, t):
   luas = a * t / 2
   return luas

alas = 10
tinggi = 20

alas2 = 15
tinggi2 = 45

print('Luas total kedua segitiga tersebut adalah ', luasSegitiga (alas, tinggi)+luasSegitiga(alas2, tinggi2))
