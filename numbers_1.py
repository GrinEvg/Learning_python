a = 1
b = 5
c = 100
e = 2.411
total = a + b + c
print(total)
total = a + b + c + e
print(total)
total = c // 5
print(total)
total = c % 5
print(total)
from math import ceil, floor
print('обычное округление', round(e),'\n', 'округление вверх', ceil(e), '\n', 'округление вниз', floor(e))
comp = 1 + 3j # комплексное число
print( comp.real, comp.imag) # выделение реальной(.real) и комплексной (.imag) частей
