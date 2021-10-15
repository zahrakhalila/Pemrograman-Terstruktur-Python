import random
angkarahasia = random.randint(0, 100)

print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")

while True:
    jawaban = int(input("Masukkan Tebakan Anda:"))
    if jawaban == angkarahasia:
        print("Yeeee... Bilangan tebakan anda BENAR :-)")
        break
    elif (jawaban < angkarahasia):
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
    else:
        print("Hehehe… Bilangan tebakan anda terlalu besar")

        
