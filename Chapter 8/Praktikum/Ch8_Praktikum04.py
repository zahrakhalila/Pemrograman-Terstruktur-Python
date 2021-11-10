dataSayur = ['Bayam', 'Kangkung', 'Wortel', 'Selada']
while True:
    print('Menu:')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    print('D. Keluar')
    pilih = input('Pilihan Anda: ')

    if pilih == 'A' or pilih == 'a':
        print('-'*30)
        tambahSayur = input('Masukkan nama sayur yang akan ditambahkan: ')
        if tambahSayur not in dataSayur:
            dataSayur.append(tambahSayur)
        else:
            print('Maaf nama sayur yang anda tambahkan sudah ada')
        print('-'*30)
    elif pilih == 'B' or pilih == 'b':
        print('-'*30)
        hapusSayur = input('Masukkan nama sayur yang akan dihapus: ')
        if hapusSayur in dataSayur:
            dataSayur.remove(hapusSayur)
        else:
            print('Maaf nama sayur yang anda ingin hapus tidak ada')
        print('-'*30)
    elif pilih == 'C' or pilih == 'c':
        print('-'*30)
        print('Data sayur saat ini: ')
        for i in range(len(dataSayur)):
            print(dataSayur[i])
        print('-'*30)
    elif pilih == 'D' or pilih == 'd':
        break
