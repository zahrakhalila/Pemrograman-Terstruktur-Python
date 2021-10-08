#Menghitung waktu tempuh perjalanan
print("_______________Menghitung Waktu Tempuh Perjalanan_______________")
jarakAB=float(input("Jarak dari kota A ke B (km):"))
kecepatanAB=float(input("Kecepatan rata-rata dari kota A ke B (km/jam):"))
print("Waktu tempuh perjalanan dari kota A ke B:", round(jarakAB//kecepatanAB),"Jam",round((jarakAB/kecepatanAB-jarakAB//kecepatanAB)*60),"Menit")
print("________________________________________________________________")
jarakBC=float(input("Jarak dari kota B ke C (km):"))
kecepatanBC=float(input("Kecepatan rata-rata dari kota B ke C (km/jam):"))
print("Waktu tempuh perjalanan dari kota B ke C:", round(jarakBC//kecepatanBC),"Jam",round((jarakBC/kecepatanBC-jarakBC//kecepatanBC)*60),"Menit")
print("----------------------------------------------------------------")

#Menghitung pukul berapa tiba di kota C
print("__________________Menghitung Tiba Pukul Berapa__________________")
print("Waktu berangkat dari kota A:")
jam1=int(input("Jam:"))
menit1=int(input("Menit:"))
print("Waktu tiba di kota B")
print("Jam:",jam1+round(jarakAB//kecepatanAB))
print("Menit:",menit1+round((jarakAB/kecepatanAB-jarakAB//kecepatanAB)*60))
print("Istirahat di kota B")
jam2=int(input("Jam:"))
menit2=int(input("Menit:"))
print("Waktu tiba di kota C")
jamtotalC=jam1+round(jarakAB//kecepatanAB)+round(jarakBC//kecepatanBC)+jam2
menittotalC=menit1+round((jarakAB/kecepatanAB-jarakAB//kecepatanAB)*60)+round((jarakBC/kecepatanBC-jarakBC//kecepatanBC)*60)+menit2
if(jamtotalC > 24):
    print("Jam:",jamtotalC-24)
elif(menittotalC > 59):
    print("Jam:",jamtotalC+1)
    print("menit:",menittotalC-60)
else:
    print("Jam:",jamtotalC)
    print("menit:",menittotalC)
