def total(jarak,konsumsi):
    """fungsi untuk menhitung Total Liter Bensin yang diperlukan"""
    return jarak/konsumsi
#input data
jarak= float(input("Masukkan total jarak yang ditempuh: "))
konsumsi= float(input("Masukkan jarak yang dapat ditempuh dengan konsumsi bbm 1 liter: "))
Total=total(jarak,konsumsi)
print("Total Liter Bensin yang diperlukan: ", Total)
