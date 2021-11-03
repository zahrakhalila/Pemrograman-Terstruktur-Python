#kode program untuk menampilkan isi sebuah file text
try:
    #input namafile
    namafile = str(input('Masukkan nama file : '))
    file = open(namafile, 'r')

    #output isi file
    print('Isi file ', namafile, ' adalah:')
    print(file.read())

except FileNotFoundError:
    print('Maaf file tidak ditemukan')
