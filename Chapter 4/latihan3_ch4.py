def berapa(literbensin,kapasitas):
    """fungsi untuk menghitung Berapa kali minimal isi bensin"""
    return literbensin/kapasitas
#input data
literbensin= float(input("Masukkan liter bensin yang diperlukan: "))
kapasitas= float(input("Masukkan kapasitas tangki bbm mobil: "))
Berapa=berapa(literbensin,kapasitas)
print("Berapa kali minimal isi bensin: ", Berapa)
