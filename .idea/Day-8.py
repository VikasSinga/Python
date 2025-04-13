# def greet():
#     print("hi")
#     print("Hello")
#     print("how are you")
# greet()
# #Function That Allows Input
#
# def Greet_with_name(name,age):#Parameter
#     print(f"My age: {age}")
#     print(f"hello {name}")
# Greet_with_name("vikas",26) #Argument
#
# def greet_with(name,location):
#     print(name)
#     print(location)
# greet_with("vikas","pileru")
from functools import total_ordering

# MY CODE
# def calculate_love_score(name1,name2):
#     count=0
#     count1=0
#     word1 ="TRUE"
#     word2 = "LOVE"
#     check1=[]
#     check2=[]
#     for i in word1:
#         check1.append(i)
#     # print(check1)
#     for j in word2:
#         check2.append(j)
#     for k,l in zip(name1,name2):
#         for m in check1:
#             if k ==m.lower():
#                 count +=1
#             if l==m.lower():
#                 count+=1
#         for n in check2:
#             if k == n.lower():
#                  count1+=1
#             if l == n.lower():
#                 count1+=1
#     print(f": The love score should be {count}{count1}")



# calculate_love_score(name1="Kanye West",name2="Kim Kardashian")
# Aejila YU code
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
# calculate_love_score("Kanye West", "Kim Kardashian")
#

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encripyt,type 'decode' to decrypt \n").lower()
# text = input("Type your message: \n")
# shift = int(input("Type the shift number: \n"))
# word=""
# def encrypt(Original_text,shift_amount):
#     total=""
#     for i in Original_text:
#         position=alphabet.index(i)+shift_amount
#         position %= len(alphabet) # IMP
#         total+=alphabet[position]
#     print(total)
#
# def decrypt(Original_text,shift_amount):
#     reverse=""
#     for i in Original_text:
#         position= alphabet.index(i) - shift_amount
#         position %= len(alphabet)
#         reverse +=alphabet[position]
#     print(reverse)

def caeser(encode_or_decode,Original_text,shift_amount):
    output=""
    for i in Original_text:

        if i not in alphabet:
            output +=i
        elif encode_or_decode == "decode":
                # shift_amount = shift_amount *-1
                position= alphabet.index(i) - shift_amount
                position %= len(alphabet)
                output +=alphabet[position]
        elif encode_or_decode == "encode":
                position= alphabet.index(i) + shift_amount
                position %= len(alphabet)
                output +=alphabet[position]
    print(output)
    # encode=encrypt(Original_text=text, shift_amount=shift)
    # decode=decrypt(Original_text=text, shift_amount=shift)
# caeser(Original_text=text, shift_amount=shift, encode_or_decode=direction)
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encripyt,type 'decode' to decrypt \n").lower()
    text = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))
    caeser(Original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("You want to restart again type YES else type NO: \n").lower()
    if restart == "no":
        should_continue = False
        print("BYE")
