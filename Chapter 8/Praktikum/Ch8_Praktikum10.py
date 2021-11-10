buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
totalHarga = []

def beliBuah(buah):
    try:
        beli = str(input('Nama buah yang dibeli : '))
        if beli in buah:
            berat = int(input('Berapa Kg             : '))
            print('-'*33)
        totalHarga.append(buah[beli]*berat)

    except ValueError:
        print('Maaf hanya masukkan angka')

    except KeyError:
        print('Maaf buah yang anda masukkan tidak tersedia')

def tambahLagi():
    global tambah
    tambah = input('Beli buah yang lain (y/n)? ')
    print('-'*33)

while True:
    beliBuah(buah)
    tambahLagi()
    if tambah == 'y':
        continue
    elif tambah == 'n':
        break
    elif tambah != 'y' and tambah != 'n':
        print('Maaf, tolong hanya masukkan y/n')
        tambahLagi()
        if tambah == 'y':
            continue
        elif tambah == 'n':
            break

total = sum(totalHarga)
print('Total harga           : Rp.', total)
