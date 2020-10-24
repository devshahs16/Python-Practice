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


## Some more python practice:

# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# PRACTICE:

# 1. input, age, turn 100
name = input("Enter name: ")
age = int(input("Enter age: "))
number = int(input("to print copies: "))
current_year = 2020
out = (100-age)
year_turn = current_year+out
print(f'Hi, {name}, you will turn 100 in the year {year_turn}!!' '\n' * number)


# 2. odd/even
nums = 5  # int (input("enter number: "))
check = 25  # int (input("enter number: "))
if nums % 4 == 0:
    print(" multiple of 4")
elif nums % 2 == 0:
    print("even")
else:
    print("odd")


if nums % check == 0:
    print('divides')
else:
    print("NO. ")


# 3.
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for n in list_a:
#   if n < 5:
#       list_b.append(n)
# print(list_b)
# OR : in one line - List Comprehension.
list_b = []
list_b = [n for n in list_a if n < 5]  # List comprehension
print(list_b)

number = 8  # int(input(":: "))
lst_c = []
# for x in list_a:
#    if x < number:
#        lst_c.append(x)
# print(lst_c)
# OR: list comprehension
lst_c = [x for x in list_a if x < number]  # List comprehension
print(lst_c)

# 4. Divisors
nos = 35  # int(input("give number: "))
for n in range(1, nos):
    if nos % n == 0:
        print(n)

# 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_set = set(a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b_set = set(b)
c = a_set & b_set
print(list(c))

# OR:
c = []
for n in a:
    if n in b and n not in c:
        c.append(n)
print(c)


# 6. palindrome
names = 'devved'
revs = names[::-1]
if names == revs:
    print("pali")


# 7. list comprehension. div by 2?
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [n for n in a if n % 2 == 0]
print(b)

# 8. rock-paper-scissor
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
player_one = 'scissor'
player_two = 'rock'

if player_one == 'rock' and player_two == 'scissor':
    print('player_one wins')

elif player_one == 'scissor' and player_two == 'rock':
    print('player_two wins')

elif player_one == 'scissor' and player_two == 'paper':
    print('player_one wins')

elif player_one == 'paper' and player_two == 'scissor':
    print('player_two wins')

elif player_one == 'paper' and player_two == 'rock':
    print('player_one wins')

elif player_one == 'rock' and player_two == 'paper':
    print('player_two wins')


# 9. guess game

randoms = "10"
exit = False
chances = 0
while exit == False:
    guess = input("> ")
    if guess == randoms:
        chances += 1
        print("Correct", chances)
    elif guess == "quit":
        chances += 1
        exit = True
        print("bye", chances)
    else:
        chances += 1
        print('not correct', chances)


# 10. DONE. (Same as above)

# 11. prime no, but using functions.
def primy(num):
    for n in range(2, num):
        if num % n == 0:
            return n

    print("prime")


primy(11)


# 12. first and last using func

def new():
    a = [5, 10, 15, 20, 25]
    b = a[0], a[-1]
    print(list(b))


new()


# 13. Fibonacci (recursive - ik!)

def fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return (fib(n-1)+fib(n-2))


print(fib(8))


# 14. List remove duplicates

def remove_dups(take_list):
    take_list = set(take_list)
    new_one = list(take_list)
    return new_one


print(remove_dups([2, 4, 6, 11, 2, 4, 66, 99, 66]))

# OR:


def remove_dup(take_list):
    new_list = []
    for n in take_list:
        if n not in new_list:
            new_list.append(n)
    print(new_list)


remove_dup([2, 4, 6, 11, 2, 4, 66, 99, 66])

# 15. Reverse word order

ask_string = "hello guys my name is dev shah"
ask_string = ask_string.split()
new_str = []
new_str.append(ask_string[::-1])
print(new_str)
# OR:
ask_string = "hello guys my name is dev shah"
new_str = ask_string.split()
print(' '.join(new_str[::-1]))

# 16. Password generator


def pwd(size, chars):
    print(''.join(random.sample(chars, size)))


pwd(size=8, chars=string.ascii_letters+string.digits+string.punctuation)


# 17. Decode webpage (Will try after learning)

# 18. Cows & Bulls:
# 4-digit number,
# ask user to guess 4 digit number
# Every digit user guessed correctly and in right position - give Cow.
# If guessed correctly but in wrong place, give Bull.


def cow_bull():
    number = random.sample(nums, size)  # random return a list
    number = str(random)
    sums = 0
    while sums != 4:
        ask_num = input('Enter no: ')
        cow = 0
        bull = 0
        for indexs, digit in enumerate(ask_num):   # 1 2 3 4
            for indexxs, digits in enumerate(number):
                if digit == digits and indexs == indexxs:
                    cow += 1
                elif digit == digits:
                    bull += 1
                else:
                    pass
                    # give input again
        sums = cow + bull
        print(f'{cow} Cows, {bull} Bulls')


size = 4
nums = range(10)
cow_bull()  # [1, 2, 3, 4]

# 19. Decode webpage (Will try after learning)


# 20. Element searching (and binary search)

number = [5, 3, 8, 5, 9, 16, 1]
number.sort()
ask = int(input("enter: "))
if ask in number:
    print("True")
else:
    print("False")


# 21. Write to a file: (later)
# 22. Read from a file: (later)
# 23. Overlap file: (later)

# 24. Draw a game:

# 25. Guessing game 2. This time pc will guess your number

print("Select a number from 0-10 in your mind")
correct = False
while correct != True:
    num = range(11)
    pc_guess = random.choice(num)
    print(pc_guess)
    correct_one = input('Too low, high or correct?  ')
    if correct_one == 'too high':
        pass
    elif correct_one == 'too low':
        pass
    elif correct_one == 'correct':
        print("guess done")
        correct = True
    else:
        pass

# 26, 27 tic tac game

# 28. max of three w/o max()


def maxxy(vara, varb, varc):
    if vara > varb and vara > varc:
        print('vara greatest', vara)
    elif varb > vara and varb > varc:
        print('varb greatest', varb)
    elif varc > varb and varc > vara:
        print('varc greatest', varc)
    else:
        pass


maxxy(50, 8, 200)

# 29. tic tac game (again!)

# 30. pick word from random list  of words
list_of_words = ['hello', 'sky', 'blue', 'garden', 'house']
print(random.choice(list_of_words))
