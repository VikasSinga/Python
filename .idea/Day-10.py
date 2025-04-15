#Title function
# def format_name(f_name,l_name):
#     # Doc String OR Multiline comment
#     """ hi this id my new
#     function i
#     created"""
#     if f_name =="" or l_name == "":
#         return "Invalid Input"
#     k=f_name.title()
#
#     l=l_name.title()
#     return f"My name is {k} {l}"
# print(format_name(input("Enten the first name : \n"),input("Enter the last name: \n")))
from symtable import Symbol


# def function_1(text):
#     return text +text
# def function_2(text):
#     return text.title()
#
# output = function_2(function_1("hello"))
# print(output)


# Calculater Program

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# hear the functions not using () because
calculatons = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
    ''')
    number1=float(input("Enter the first number: \n"))
    Re_calculate = True
    while Re_calculate:

    # number1=float(input("Enter the first number: \n"))
        Symbol=input("Enter the symbol: \n")
        number2= float(input("Enter the secound number: \n"))
        answer=calculatons[Symbol](number1,number2)
        print(f"{number1}{Symbol}{number2} = {answer}")
        Re_calculate = input("If you want to re-calculate type 'YES' or 'NO': \n").lower()
    # print(calculatons[Symbol](number1,number2))
        if Re_calculate == "yes":
            number1 = answer
        elif Re_calculate =="no":
            Re_calculate=False
            print(F"Total is : {answer}")



calculator()