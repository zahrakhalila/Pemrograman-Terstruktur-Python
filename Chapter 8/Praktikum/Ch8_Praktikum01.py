try:
    banyakBil = int(input('Masukkan banyak bilangan bulat yang akan anda urutkan : '))
    i = 1
    semuaBil = []
    while i <= banyakBil:
        bilBulat = int(input('Silahkan masukkan bilangan ke-{} anda : '.format(i)))
        semuaBil.append(bilBulat)
        i += 1

    semuaBil.sort(reverse=True)
    print(semuaBil)

except ValueError:
    print('Maaf data yang anda masukkan invalid, tolong hanya masukkan bilangan bulat')

