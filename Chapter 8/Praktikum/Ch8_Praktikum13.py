def nilaiTertinggi(nilaiMhs):
    nilaiAkhir = []
    for i in range(len(nilaiMhs)):
        nilaiAkhir.append((nilaiMhs[i]['mid'] + 2*nilaiMhs[i]['uas'])/3)
    tertinggi = max(nilaiAkhir)
    posisi = nilaiAkhir.index(tertinggi)
    print('Nilai tertinggi diraih oleh {} NIM {} dengan perolehan nilai {}'.format(nilaiMhs[posisi]['nama'], nilaiMhs[posisi]['nim'], nilaiAkhir[posisi]))

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	 {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

nilaiTertinggi(nilaiMhs)
