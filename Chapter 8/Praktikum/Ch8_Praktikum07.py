def hargaTermahal(buah):
    termahal = max(buah.values())
    key = list(buah.keys())
    value = list(buah.values())
    print(key[value.index(termahal)])

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Daftar nama dan harga buah:')
print(buah)
print('Harga buah termahal yaitu buah ', end='')
hargaTermahal(buah)
