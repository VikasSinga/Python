import random
from itertools import count

fruits: list[str] = ["apple", "banana","graphs","oranges"]
for fruit in fruits:
    print(fruit)
    print(fruit +" Thinu")
print(fruits)

Student_score = [112,456,654,345,323,543,233,433,234,433,675,276,]
total_score = sum(Student_score)
# print(total_score)
sum = 0
for score in Student_score:
    sum +=score
print(sum)
print(max(Student_score))

# MAX number in student list
large = 0
for socre in Student_score:

    if large < socre:
        large=socre
print(large)

#  Range functio1
count =0
for number in range(1 ,11,2):
    print(number)


# gulls problem
for num1 in range(1,101):
    count += num1
print(count)

# FizzBuzz Problem
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%5 == 0:
        print("Buzz")
    elif num%3 == 0 :
        print("Fizz")
    else:
        print(num)

# Password Generater

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!","#","$","%","&","(",")","*","+"]
print("Welcome to the PyPassword Generater")
no_letters = int(input("How maney letters would you like in your PASSWORD\n"))
no_symbols = int(input("How maney symbols would you like\n"))
no_numbers = int(input("how maney numbers would you like\n"))

k=""
for them1 in range(0,no_letters):
   k += random.choice(letters)
for them2 in range(0,no_symbols):
    k += random.choice(symbols)
for them in range(0,no_numbers):
    k += random.choice(numbers)
l=''.join(random.sample(k,len(k)))
print(f"Your Password is: {l}")


# Aenjelas code
password_list = []
for char in range(0, no_letters):
    password_list.append(random.choice(letters))
for char in range(0, no_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, no_numbers):
    password_list.append(random.choice(numbers))
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password=""

for char in password_list:

   password += char

print (f"Your password is{password}")
