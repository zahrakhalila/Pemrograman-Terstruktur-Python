import math

def bintang(n):
    space = 2*n-1
    for i in range(math.ceil(n/2)):
        print(('*'*(2*i+1)).center(space))
    for i in range(math.ceil(n/2)-2,-1,-1):
        print(('*'*(2*i+1)).center(space))

bintang(7)
