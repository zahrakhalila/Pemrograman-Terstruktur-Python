buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

try:
    beli = str(input('Nama buah yang dibeli : '))
    if beli in buah:
        berat = int(input('Berapa Kg             : '))
        print('-'*33)
    print('Total harga           : Rp.', buah[beli]*berat)

except ValueError:
    print('Maaf hanya masukkan angka')

except KeyError:
    print('Maaf buah yang anda masukkan tidak tersedia')
