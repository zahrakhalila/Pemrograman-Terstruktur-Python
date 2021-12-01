myFile = open('data2.txt', 'r')
readFile = myFile.read().splitlines()

NIM = input('Masukkan NIM yang mau dicari : ')
print()

for i in range(len(readFile)):
    data = readFile[i].split('|')
    if NIM == data[0] :
        status = 'ada'
        print('Data Mahasiswa')
        print('NIM    : ' + data[0])
        print('Nama   : ' + data[1])
        print('Alamat : ' + data[2])
        break
    else :
        status = 'tidak ada'

if status == 'tidak ada':
    print('Data Mahasiswa tidak ditemukan')

myFile.close()
