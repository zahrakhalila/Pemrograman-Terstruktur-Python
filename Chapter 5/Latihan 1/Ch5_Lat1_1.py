#Input nilai-nilai mata pelajaran
nilaiBI=float(input("Masukkan nilai Bhs Indonesia :"))
nilaiIPA=float(input("Masukkan nilai IPA           :"))
nilaiMate=float(input("Masukkan nilai Matematika    :"))

#Status kelulusan
if (nilaiBI >= 60) and (nilaiIPA >= 60) and (nilaiMate >= 70):
    print("{:28}".format("Status kelulusan"),": LULUS")
else:
    print("{:28}".format("Status kelulusan"),": TIDAK LULUS")
