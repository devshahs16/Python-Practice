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



# generate random nos :

print(random.randint(1, 50))        # random nos from 1-50. 1 included.
print(random.random())              # only from 0-1
number = range(0, 90)
names = ['dev', 'chupre']
print(random.choice(names))

# remove duplicates
remove = [3, 6, 7, 8, 88, 5, 8, 2, 0, 2, 3]
new_list = []

for n in remove:
    if n not in new_list:
        new_list.append(n)
print(new_list)


# check if palindrome
straight = 'ded'
reverse = straight[::-1]
if straight == reverse:
    print("palin")
else:
    print("NO")

# Greatest common divisor
n1 = 12
n2 = 24
n1_div = []
n2_div = []

for n in range(1, n1+1):
    if n1 % n == 0:
        n1_div.append(n)
max2 = max(n1_div)

for x in range(1, n2+1):
    if n2 % x == 0:
        n2_div.append(x)
max1 = max(n2_div)

print(f'GCD: {min(max1, max2)}')

# guessing game
secret = 9
guess_start = 1
while guess_start < 4:
    guess = int(input(">> "))
    guess_start += 1
    if guess == secret:
        print("Correct")
        break

else:
    print("failed")
