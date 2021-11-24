nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

for i in range(len(nilai)):
    nilaiAkhir = (nilai[i]['mid'] + 2*nilai[i]['uas'])/3
    nilai[i]['akhir'] = nilaiAkhir
    if nilaiAkhir >= 60:
        nilai[i]['status'] = 'LULUS'
    else:
        nilai[i]['status'] = 'TIDAK LULUS'
    
print('============================================================')
print('NIM	NAMA	     N.MID   N.UAS	N.AKHIR    STATUS')
print('------------------------------------------------------------')

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(8), end='')
    print(nilai[i]['nama'].ljust(12), end='')
    print(str(nilai[i]['mid']).rjust(6), end='')
    print(str(nilai[i]['uas']).rjust(8), end='')
    print(str("%2.f"%(nilai[i]['akhir'])).rjust(13), end='')
    print(nilai[i]['status'].rjust(10))

print('------------------------------------------------------------')
