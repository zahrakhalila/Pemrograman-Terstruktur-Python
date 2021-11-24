import random

def shuffleString(x, n):
    banyakKemungkinan = 1
    for i in range(1, len(x)+1):
        banyakKemungkinan = i*banyakKemungkinan

    if n>banyakKemungkinan:
        print('Maaf permintaan anda terlalu banyak')
    else:
        listHasil = []
        while True:
            if len(listHasil) == n:
                break
            hasilAcak = ''.join(random.sample(x,len(x)))
            if hasilAcak in listHasil:
                continue
            listHasil.append(hasilAcak)
        print(listHasil)

k = str(input('Masukkan kata yang ingin anda shuffle : '))
l = int(input('Masukkan banyak kali shuffle : '))
print('randomString(\'' + str(k) + '\', ' + str(l) + ') -> ', end='')
shuffleString(k, l)
