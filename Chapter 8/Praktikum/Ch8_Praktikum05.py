def kuadrat(bil):
    hasilKuadrat = []
    for i in bil:
        hasilBilangan = i**2
        hasilKuadrat.append(hasilBilangan)
    print(hasilKuadrat)

try:
    banyakBil = int(input('Masukkan banyak bilangan bulat : '))
    i = 1
    semuaBil = []
    while i <= banyakBil:
        bilBulat = int(input('Silahkan masukkan bilangan ke-{} : '.format(i)))
        semuaBil.append(bilBulat)
        i += 1
    
    print('-'*36)
    print('bilangan =', semuaBil)
    print('hasil = ', end='')
    kuadrat(semuaBil)

except ValueError:
    print('Maaf data yang anda masukkan invalid, tolong hanya masukkan bilangan bulat')

