myFile = open('data1.txt','r')
bil = myFile.readlines()

ganjil = []
genap = []

for i in range(len(bil)):
    if int(bil[i]) %2 == 0:
        genap.append(bil[i])
    else:
        ganjil.append(bil[i])

print('Banyaknya bilangan genap  : {0}'.format(len(genap)))
print('Banyaknya bilangan ganjil : {0}'.format(len(ganjil)))

myFile.close()
