def sum(*daftar_nilai):
    jumlah = 0
    for nilai in daftar_nilai:
        jumlah += nilai
    return jumlah

def average(*daftar_nilai):
    i = 0
    sum = 0
    for nilai in daftar_nilai:
        sum += nilai
        i += 1
    return  sum/i   

def maks(*daftar_nilai):
    nilai_terbesar = daftar_nilai[0]
    for nilai in daftar_nilai:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def min(*daftar_nilai):
    nilai_terkecil = daftar_nilai[0]
    for nilai in daftar_nilai:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil
