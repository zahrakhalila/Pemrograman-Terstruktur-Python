openFile = open('data6_hasil.txt', 'r')
n = -2

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
fileHasil = open('data7.txt', 'w')
fileHasil.write(hasil)
openFile.close()
fileHasil.close()

myFile1 = open('data6_hasil.txt', 'r')
baca1 = myFile1.read()
myFile2 = open('data7.txt', 'r')
baca2 = myFile2.read()

print('Teks sandi : ', baca1)
print('Teks asli  : ', baca2)

myFile1.close()
myFile2.close()
