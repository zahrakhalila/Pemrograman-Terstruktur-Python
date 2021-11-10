def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    listABC = [a, b, c]
    return listABC

try:
    banyakBil = int(input('Masukkan banyak bilangan bulat  : '))
    i = 1
    semuaBil = []
    while i <= banyakBil:
        bilBulat = int(input('Silahkan masukkan bilangan ke-{} : '.format(i)))
        semuaBil.append(bilBulat)
        i += 1
    
    print(dataStat(semuaBil))

except ValueError:
    print('Maaf data yang anda masukkan invalid, tolong hanya masukkan bilangan bulat')
