inputFile = input('Masukkan nama file yang akan di enkripsi : ')
n = int(input('Masukkan nilai n pergeseran : '))
openFile = open(inputFile, 'r')

char = []
while True:
    readFile = openFile.read(1)
    if not readFile:
        break
    Ord = ord(readFile)
    char.append(Ord)
    
for i in range(len(char)):
    if char[i] != 32:
        if (char[i] >= 65) and (char[i] <= 90):
            result = ((char[i] + n-65) %26 + 65)
        else:
            result = ((char[i] + n-97) %26 + 97)
        del char[i]
        char.insert(i, chr(result))
    else:
        char.insert(i, chr(char[i]))
        del char[i+1]
        continue

hasil = ''.join(char)
fileHasil = open('data6_hasil.txt', 'w')
fileHasil.write(hasil)
openFile.close()
fileHasil.close()

myFile1 = open(inputFile, 'r')
baca1 = myFile1.read()
myFile2 = open('data6_hasil.txt', 'r')
baca2 = myFile2.read()

print('-'*32)
print('Teks asli  : ', baca1)
print('Teks sandi : ', baca2)

myFile1.close()
myFile2.close()
