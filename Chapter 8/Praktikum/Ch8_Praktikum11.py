buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
while True:
    print('Menu:')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Hapus buah')
    print('D. Keluar')
    pilih = input('Pilihan menu: ')
    print('-'*33)

#Menu A
    if pilih == 'A' or pilih == 'a':
        namaBuah = input('Masukkan nama buah    : ')
        if namaBuah in buah:
            print('Maaf nama buah yang anda tambahkan sudah ada')
        elif namaBuah not in buah:
            hargaSatuan = int(input('Masukkan harga satuan : Rp. '))
            buah[namaBuah] = hargaSatuan
            key = list(buah.keys())
            value = list(buah.values())
            print('Data buah :')
            for i in range(len(buah)):
                print('- {} (Harga Rp. {}) '.format(key[i], value[i]))
        print('-'*33)

#Menu B
    elif pilih == 'B' or pilih == 'b':
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
        print('-'*33)
            
#Menu C
    elif pilih == 'C' or pilih == 'c':
        break
