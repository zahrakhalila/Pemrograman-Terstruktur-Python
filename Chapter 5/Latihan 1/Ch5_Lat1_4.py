kode=input("Masukkan kode karyawan :")
nama=input("Masukkan nama karyawan :")
while(True):
    gol=str(input("Masukkan golongan      :"))
    if (gol=="A") or (gol=="a"):
        gjp = 10000000
        pot = 2.5
        break
    elif (gol=="B") or (gol=="b"):
        gjp = 8500000
        pot = 2.0
        break
    elif (gol=="C") or (gol=="c"):
        gjp = 7000000
        pot = 1.5
        break
    elif (gol=="D") or (gol=="d"):
        gjp = 5500000
        pot = 1.0
        break

#Struk gaji karyawan
print("=========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------")
print("{:22}".format("Nama Karyawan"),":", nama, "( Kode :", kode,")")
print("{:22}".format("Golongan"),":", gol)
print("-----------------------------------------")
print("{:22}".format("Gaji Pokok"),": Rp.",gjp)
totalpot=gjp*(pot/100)
print("{:22}".format("Potongan", "(", pot, "% )"), ": RP.", totalpot)
print("----------------------------------------- -")
gjbr=gjp-totalpot
print("{:22}".format("Gaji Bersih"),": Rp.", gjbr)
