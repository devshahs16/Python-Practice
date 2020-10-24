# Swap 2 variables:

import string
from pathlib import Path
import random
x = 25
y = 79
print(x, y)
x, y = y, x
print(x, y)
# OR:
x = 44
y = 88
print(x, y)
z = y
y = x
x = z
print(x, y)

# Celcius to Farenh..
temp_c = 2
temp_f = (temp_c * 9/5) + 32
print(temp_f)
# OR:
# temp = float(input("Enter Temp: "))
# c_f = input("C or F: ")
# c_f = c_f.lower()
# if c_f == 'c':
#   temp = (temp * 9/5) + 32
#   print(f'Input is in celcuis, hence, F = {temp}')
# else:
#   temp = 5/9 * (temp-32)
#  print(f'Input is in Fahr, hence, C = {temp}')

# Sum of all digits in a number:
number = 1024
number = str(number)
sum = 0
for n in number:
    n = int(n)
    sum += n
print(sum)

# Check prime:
n = 7
if n > 1:
    for x in range(2, n):
        if n % x == 0:
            print('not prime')
            break
    else:
        print('prime')
