def tambahlagi():
    global jawaban
    jawaban= input("Lagi (y/n)? : ")

#header
print('-' * 30)
print('   PROGRAM HITUNG RATA-RATA   ')
print('-' * 30)

#kode program hitung rata-rata
sum = 0
banyakdata = 0
while True:
    try: 
        bilangan = int(input('Masukkan bilangan bulat : '))
        sum += bilangan
        banyakdata += 1
        tambahlagi()
        if jawaban == 'y':
            continue
        elif jawaban == 'n':
            break
        else: 
            print('Maaf jawaban yang bisa dimasukkan hanya y/n, silahkan coba lagi!')
            tambahlagi()
            if jawaban == 'y':
                continue
            elif jawaban == 'n':
                break
    except ValueError:
        print('Maaf bilangan yang anda masukkan invalid, masukkan hanya bilangan bulat')

print('Rata-ratanya adalah ', sum/banyakdata)        
