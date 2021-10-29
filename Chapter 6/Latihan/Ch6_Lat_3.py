#Fungsi Faktorial
def faktorial(n):
    f = 1
    for i in range(1, n + 1):
        f*=i
    return f

#Fungsi Combinasi
def C(a, b):
    kombinasi = faktorial(a) / (faktorial(b) * faktorial(a-b))
    print(kombinasi)

#Fungsi Permutasi
def P(a, b):
    permutasi = faktorial(a) / faktorial(a-b)
    print(permutasi)

print('C(5, 3) = ', end='')
C(5, 3)
print('P(10, 7) = ', end='')
P(10, 7)
