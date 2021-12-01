myFile = open('data2.txt', 'w')

while True:
    nim = input('Masukkan NIM            : ')
    nama = input('Masukkan Nama Mhs       : ')
    alamat = input('Masukkan Alamat         : ')

    hasil = nim + '|' + nama + '|' +alamat

    myFile.write(hasil + '\n')

    print()
    ans = input('Ulangi input lagi (y/n) : ')
    print()
    
    if ans in ('N', 'n'):
        break

myFile.close()
