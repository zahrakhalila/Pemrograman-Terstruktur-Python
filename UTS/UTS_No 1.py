#Input tahun
tahun = int(input("Masukkan Tahun : "))

#Menentukan kabisat atau tidak
if((tahun % 400)== 0):
    print("Tahun", tahun, "merupakan TAHUN KABISAT")
elif((tahun % 100) == 0):
    print("Tahun", tahun, "BUKAN merupakan TAHUN KABISAT")
elif((tahun % 4) == 0):
    print("Tahun", tahun, "merupakan TAHUN KABISAT")
else:
    print("Tahun", tahun, "BUKAN merupakan TAHUN KABISAT")
