#variable global
def hitung_nilai(lives,score,menu):
    if(jawaban == solusi):
        score = score + 2
        lives = lives
        print("Hore... benar!!! Skor Anda", score, "(Lives : ", lives, ")")
    else:
        score = score - 2
        lives = lives - 1
        print("Wah... salah!!! Skor Anda", score, "(Lives : ", lives, ")")
    if(lives == 0):
        print("Game Over")
        menu = False
    return lives,score,menu     
    
#Pilihan menu
print("Menu pilihan level :")
listmenu = ["1. Level 1 (Penjumlahan)", "2. Level 2 (Pengurangan)", "3. Level 3 (Perkalian)", "4. Exit"]
print(listmenu[0])
print(listmenu[1])
print(listmenu[2])
print(listmenu[3])

#Input level
level = int(input("Pilih nomor pilihan : "))
print("-" * 25)

#Game
lives = 3
score = 0
menu = True

import random
while menu:
    x = random.randrange(-100, 100)
    y = random.randrange(-100, 100)   
    if(level == 1):
        soal = str(x) + " + " + str(y)
        print("Hasil dari", soal, end='')
        jawaban = int(input(" adalah "))     
        solusi = x + y
        lives,score,menu=hitung_nilai(lives,score,menu)
    elif(level == 2):
        soal = str(x) + " - " + str(y)
        print("Hasil dari", soal, end='')
        jawaban = int(input(" adalah "))     
        solusi = x - y
        lives,score,menu=hitung_nilai(lives,score,menu)
    elif(level == 3):
        soal = str(x) + " * " + str(y)
        print("Hasil dari", soal, end='')
        jawaban = int(input(" adalah "))     
        solusi = x * y
        lives,score,menu=hitung_nilai(lives,score,menu)
    elif(level == 4):
        print("Exit Game")
        menu = False

  
