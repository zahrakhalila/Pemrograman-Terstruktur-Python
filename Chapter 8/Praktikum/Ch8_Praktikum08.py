def hargaRerata(buah):
    hargaBuah = list(buah.values())
    print(sum(hargaBuah)/len(hargaBuah))

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Daftar nama dan harga buah:')
print(buah)
print('Harga rata-rata buah yaitu ', end='')
hargaRerata(buah)
