# 1
print("Hi, My name is Arpita")

# 2.1
num1=10
num2=20
num3=num1+num2
print(num3)

# 2.2
str1="Hello "
str2="World"
str3=str1+str2
print(str3)

# 2.3
string="My age is: "
n=19
print(string, str(n))

# 3.1
number=int(input("Enter number:"))
if number > 0:
    print("Number is positive.")
elif number < 0:
    print("Number is negative.")
else:
    print("Number is zero.")

# 3.2
number=int(input("Enter number:"))
if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# 4.1

for i in range(1, 11):
    print(i)


# 4.2

i = 1
while i <= 10:
    print(i)
    i += 1


# 4.3
sum_ = 0
for i in range(1, 101):
    sum_ += i
print( sum_)

# 5.1
numbers = [3, 7, 1, 9, 5]
print( max(numbers))
print(min(numbers))

# 5.2
my_dict = {"a": 1, "b": 2, "c": 3}
key = "b"
print(my_dict[key])

# 5.3
num = [5, 2, 9, 1, 7]
num.sort()
print(num)
num.reverse()
print(num)

# 5.4
dict1 = {"x": 10, "y": 20}
dict2 = {"z": 30, "w": 40}
merged_dict = {**dict1, **dict2}  
print( merged_dict)

# 6.1
string = "My name is Arpita"
vowels = "aeiou"
vowel_count = sum(1 for char in string.lower() if char in vowels)
print(vowel_count)


# 6.2
string="Arpita"
reversed_string = string[::-1]
print(reversed_string)

# 6.3
string = "radar"
if string==string[::-1]:
    print("Yes")
else:
    print("No")

#7.1
with open("my.txt", "w") as file:
    file.write("Hey, it's me")

#7.2
with open("my.txt","r") as file:
    content=file.read()
    print(content)

#7.3
with open("my.txt", "r") as file:
    lines=sum(1 for _ in file)
    print(lines)

#8.1
try:
    n=int(input("Enter a n"))
    d=int(input("Enter d: "))
    result=n/d
except ZeroDivisionError:
    print("Zero not allowed")

#8.2
try:
    n=int(input("Enter: "))
    print(n)
except ValueError:
    print("Invalid input!")

#8.3
try:
    file= open("my.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Not fpund")
finally:
    print("Opened")

#9.1
import random

n=[random.randint(1,100) for _ in range(5)]
print(n)

#9.2
import random

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        return True

random_num= random.randint(1,100)
print("Is prime", is_prime(random_num))

#9.3
import random

die_roll=random(1,6)
print("Rolled a six-sided die", die_roll)

#9.4
import random
n=[1,2,3,4,5,6]
random.shuffle(n)
print(n)

#9.5
import random

items=[1,2,3,5,7,8]
select= random.choice(items)
print(select)

#9.6
import random
import string

length= int (input("Enter password length: "))
password= ''.join(random.choices(string.ascii_letters+ string.digits+ string.punctuation, k=length))
print(password)

#9.7
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck=[f"{rank} of {suits}" for suit in suits for rank in ranks]
card= random.choice(deck)
print(card)

#10.1
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)

#10.2
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <string>")
else:
    string = sys.argv[1]
    print("Length of string:", len(string))

#11.1
import math

number = float(input("Enter a number: "))
print( math.sqrt(number))


#11.2
from datetime import datetime

now = datetime.now()
print("date and time:", now)


#11.3
import os


files = os.listdir(".")
print("Files:")
for file in files:
    print(file)
