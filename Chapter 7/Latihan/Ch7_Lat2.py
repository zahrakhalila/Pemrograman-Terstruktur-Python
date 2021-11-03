def maulagi():
    global jawaban
    jawaban = str(input('Mau lagi (y/n) : '))

try:
    #input namafile
    namafile = str(input('Masukkan nama file : '))

    #membuka file
    file = open(namafile, 'a')

    #input data yang akan ditambahkan
    while True:
        tambahan = input('Data yang mau ditambahkan : ')
        file.write(tambahan)
        maulagi()
        if jawaban == 'y':
            continue
        elif jawaban == 'n':
            break
            file.close()
        else: 
            print('Maaf jawaban yang bisa dimasukkan hanya y/n, silahkan coba lagi!')
            maulagi()
            if jawaban == 'y':
                continue
            elif jawaban == 'n':
                break
                file.close()
                
except FileNotFoundError:
    print('Maaf file tidak ditemukan')

except PermissionError:
    print('Maaf file tidak ditemukan')
