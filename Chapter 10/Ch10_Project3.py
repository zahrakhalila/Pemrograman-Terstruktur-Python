myFile = open('data2.txt', 'r')
data = myFile.read().splitlines()

dataList = []
for i in range(len(data)):
    pecahData = data[i].split('|')
    dataDict = {'NIM': pecahData[0], 'Nama': pecahData[1], 'Alamat': pecahData[2]}
    dataList.append(dataDict)

print('dataMhs = ' + str(dataList))

myFile.close()
