#Harga sewa rental mobil
print("_____________________Rental Mobil Murah______________________")
tarifawal=int(input("Tarif awal rental 12 jam pertama: Rp."))
tariftambahan=int(input("Tarif tambahan setelah 12 jam per jamnya: Rp."))
print("_____________________________________________________________")

#Waktu sewa
print("Waktu peminjaman mobil:")
jam1=float(input("Jam:"))
menit1=float(input("Menit:"))
print("Waktu pengembalian mobil:")
jam2=float(input("Jam:"))
menit2=float(input("Menit:"))
selisihjam=jam2-jam1
selisihmenit=menit2-menit1
print("Lama peminjaman:",round(selisihjam),"jam",round(selisihmenit),"menit")
print("_____________________________________________________________")

#Total harga
if(selisihjam > 12):
    print('Harga sewa total:Rp.',tarifawal+(tariftambahan*(selisihjam-12)+tariftambahan*(selisihmenit/60)))
elif(selisihjam < 12):
    print('Harga sewa total:Rp.',(tarifawal/12*(selisihjam)+tarifawal/12/60*(selisihmenit)))
else:
    print("Total harga sewa: Rp.", tarifawal)

#Pembayaran
Bayar= float(input("Jumlah Nominal Uang: Rp. "))
Hargasewa= float(input("Masukkan kembali total harga sewa: Rp."))
Kembalian=(Bayar-Hargasewa)
print("Uang kembalian: Rp.", Kembalian)
print("_____________________________________________________________")


