#Input nilai-nilai mata pelajaran
nilaiBI=float(input("Masukkan nilai Bhs Indonesia :"))
nilaiIPA=float(input("Masukkan nilai IPA           :"))
nilaiMate=float(input("Masukkan nilai Matematika    :"))

#Status kelulusan
if (nilaiBI >= 60) and (nilaiIPA >= 60) and (nilaiMate >= 70):
    print("{:28}".format("Status kelulusan"),": LULUS")
elif (0 < nilaiBI < 60) or (0 < nilaiIPA < 60) or (0 < nilaiMate < 70):
    print("{:28}".format("Status kelulusan"),": TIDAK LULUS")
elif (nilaiBI < 0) or (nilaiIPA < 0) or (nilaiMate < 0):
    print("Maaf input ada yang tidak valid")
