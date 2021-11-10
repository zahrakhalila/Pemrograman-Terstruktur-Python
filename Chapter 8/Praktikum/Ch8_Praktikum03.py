banyakMhs = int(input('Masukkan jumlah mahasiswa : '))
i = 1
namaMhs = []
while i <= banyakMhs:
    inputNama = str(input('Masukkan nama mahasiswa ke-{} : '.format(i)))
    namaMhs.append(inputNama)
    i += 1

namaMhs.sort()
for i in range(len(namaMhs)):
    print(namaMhs[i], end='')
    print('({} karakter)'.format(len(namaMhs[i])))
