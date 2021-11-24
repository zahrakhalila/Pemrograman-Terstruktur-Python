mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('==========================================================================')
print('NIM  	    NAMA MAHASISWA		TGL LAHIR	    TEMPAT LAHIR')
print('--------------------------------------------------------------------------')

data = []
tglLahir = []
tglLahirFix = []

for i in range(len(mhs)):
    data.append(mhs[i].split(':'))
    tglLahir.append(data[i][2].split('-'))

for i in range(len(tglLahir)):
    tglLahirFix.append('/'.join(tglLahir[i][::-1]))

for i in range(len(data)):
    print(data[i][0].ljust(12), end='')
    print(data[i][1].ljust(28), end='')
    print(tglLahirFix[i].ljust(20), end='')
    print(data[i][3].ljust(3))

print('--------------------------------------------------------------------------')
