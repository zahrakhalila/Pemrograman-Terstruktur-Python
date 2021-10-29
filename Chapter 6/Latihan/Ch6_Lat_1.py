def isPythagoras(a, b, c):
#rumus triple pythagoras adalah a^2 + b^2 = c^2 dengan c merupakan sisi miring
    print((a**2 + b**2) == c**2)

print('a = 3, b = 4, c = 5   -> ', end='')
isPythagoras(3, 4, 5)
print('a = 5, b = 9, c = 12  -> ', end='')
isPythagoras(5, 9, 12)
print('a = 8, b = 6, c = 10  -> ', end='')
isPythagoras(8, 6, 10)
print('a = 7, b = 8, c = 11  -> ', end='')
isPythagoras(7, 8, 11)
