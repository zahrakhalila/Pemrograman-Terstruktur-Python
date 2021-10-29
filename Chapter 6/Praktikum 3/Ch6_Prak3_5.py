from operation import *

#Nomor 5a
print('2 + 4 * 6 - 4 =', '2 +', kali(4, 6), '- 4 =', jumlah(2,kali(4, 6)), ' - 4 = ', kurang((jumlah(2, kali(4, 6))), 4))

#Nomor 5b
print('(4 + 7) * (6 - 9) =', jumlah(4, 7), '*', kurang(6, 9), '=', kali(jumlah(4, 7), kurang(6, 9)))

#Nomor 5c
print('(10 + 2) / (7 + 5) / (12 - 34) =', jumlah(10, 2), '/',  jumlah (7, 5), '/', kurang(12, 34), '=', bagi(bagi(jumlah(10,2),jumlah(7,5)) ,kurang(12,34)))
