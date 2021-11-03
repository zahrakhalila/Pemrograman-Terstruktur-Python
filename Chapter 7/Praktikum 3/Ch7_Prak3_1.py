try:
    file = open("d:/data_1.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)

except ValueError:
    print('Maaf data yang anda masukkan invalid (ada data yang bukan angka)')
