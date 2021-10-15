kode=input("Masukkan kode karyawan                   :")
nama=input("Masukkan nama karyawan                   :")

#Golongan 
while(True):
    gol=str(input("Masukkan golongan                        :"))
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

#Tunjangan
while(True):
    tji=str(input("Masukkan status (1 : menikah, 2 : belum) :"))
    if (tji=="1"):
        potji = 10
        tja=int(input("Masukkan jumlah anak                     :"))
        potja = 5
        break
    elif (tji=="2"):
        break

#Struk gaji karyawan
print("=============================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------------")
print("{:22}".format("Nama Karyawan"),":", nama, "( Kode :", kode,")")
print("{:22}".format("Golongan"),":", gol)
print("---------------------------------------------")
print("{:22}".format("Gaji Pokok"),": Rp.",gjp)
while(True):
    if (tji=="1"):
        totalpotji=gjp*(potji/100)
        print("{:22}".format("Tunjangan Istri/Suami"),": Rp.", totalpotji)
        totalpotja=tja*(gjp*(potja/100))
        print("{:22}".format("Tunjangan anak"),": Rp.", totalpotja)
        print("--------------------------------------------- +")
        gjk=gjp+totalpotji+totalpotja
        print("{:22}".format("Gaji Kotor"),": Rp.", gjk)
        totalpot=gjp*(pot/100)
        print("{:22}".format("Potongan", "(", pot, "% )"), ": RP.", totalpot)
        print("--------------------------------------------- -")
        gjbr=gjk-totalpot
        print("{:22}".format("Gaji Bersih"),": Rp.", gjbr)
        break
    elif (tji=="2"):
        print("{:22}".format("Tunjangan Istri/Suami"),": Rp.0")
        print("{:22}".format("Tunjangan Anak"),": Rp.0")
        print("--------------------------------------------- +")
        print("{:22}".format("Gaji Kotor"),": Rp.", gjp)
        totalpot=gjp*(pot/100)
        print("{:22}".format("Potongan", "(", pot, "% )"), ": RP.", totalpot)
        print("--------------------------------------------- -")
        gjbr=gjp-totalpot
        print("{:22}".format("Gaji Bersih"),": Rp.", gjbr)
        break 
