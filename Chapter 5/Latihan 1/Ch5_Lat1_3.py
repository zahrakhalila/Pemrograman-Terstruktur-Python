#Input nilai-nilai mata pelajaran
nilaiBI=float(input("Masukkan nilai Bhs Indonesia :"))
nilaiIPA=float(input("Masukkan nilai IPA           :"))
nilaiMate=float(input("Masukkan nilai Matematika    :"))

#Status kelulusan
if (nilaiBI >= 60) and (nilaiIPA >= 60) and (nilaiMate >= 70):
    status = "LULUS"
elif (0 < nilaiBI < 60) or (0 < nilaiIPA < 60) or (0 < nilaiMate < 70):
    status = "TIDAK LULUS"
elif (nilaiBI < 0) or (nilaiIPA < 0) or (nilaiMate < 0):
    print("Maaf input ada yang tidak valid")
print("{:28}".format("Status kelulusan"),":"+status)

#Sebab
if status=="TIDAK LULUS":
    print("{:28}".format("Sebab"),":")
if (nilaiBI < 60):
    print("-Nilai Bhs Indonesia kurang dari 60")
if (nilaiIPA < 60):
    print("-Nilai IPA kurang dari 60")
if (nilaiMate < 70):
    print("-Nilai Matematika kurang dari 70")
