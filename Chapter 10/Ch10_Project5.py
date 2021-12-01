myFile = open('data5_bil.txt', 'r')
myFile1 = open('data5_hasil.txt', 'w')
readFile = myFile.read().splitlines()

for i in range(len(readFile)):
    bil = readFile[i].split('|')
    tambah = int(bil[0]) + int(bil[1])
    hasil = str(tambah)
    myFile1.write(hasil + '\n')
myFile1.close()

result = open('data5_hasil.txt', 'r')
isi = result.read()
print(isi)

myFile.close()
result.close()
