# soilders=2
# def increase_soilders():
#     soilders=10
#     print(f"currently we have {soilders} soilders")
#
# increase_soilders()
# print(f"currently we have {soilders} soilders")
#
# # Local Scope : With in the function
# # cars =17
# def NO_Cars():
#     cars=10
#     print(cars)
# NO_Cars()
#
# # print(cars) // No global scope
#
# cats=3
# def cats_count():
#     print(cats)
# cats_count()
# print(cats) #Global scope
#
# # nested function cant access global variables
# # there is no block scope in python like eg:if: block
#
# level=10
# enemies=["skeliton","zombie","Alien"]
#
# def create_enemy():
#     new_enemy=""
#     if level < 5:
#         new_enemy=enemies[0]
#     print(new_enemy)# Block level
# create_enemy()
# nu=13
# print(nu/2)
#
# #  Modify Global Variable
# soilders=1
# def increase_soilders():
#     global soilders
#     soilders+=1
#     print(f"currently we have {soilders} soilders")
#
# increase_soilders()
# print(f"currently we have {soilders} soilders")
#
#
# pi=6.342
from mimetypes import guess_type
#
# #  MY CODE
# import random
#
# logo= """ ..|'''.|                        |''||'''||            '|.   '|'             '||
# .|'     ... ... .... .... ....      ||   || ..  ....    |'|   ... ..... .. .. || ...  ....... ..
# ||    ...||  |.|...|||. '||. '      ||   ||' |.|...||   | '|. |||  || || || ||||'  |.|...||||' ''
# '|.    ||||  |||    . '|.. '|..     ||   ||  |||        |   |||||  || || || ||||    ||     ||
#  ''|...'|'|..'|'|...|'..||'..|'    .||. .||. ||'|...'  .|.   '|'|..'|.|| || ||'|...' '|....||."""
#
# print(logo)
#
# print("Welcome To The Number Gussing Game! ")
# print("I'm Thinking Of a number between 1 and 100 ")
# difficulty = input("Choose a difficulty , Type 'Easy' or 'Hard : \n").lower()
#
# number = random.randint(1,100)
# if difficulty == "hard":
#     chances=5
#     while chances != 0:
#
#         if chances !=0:
#             choose = int(input("Make a Guess : "))
#             if choose==number:
#                 print("You Win!")
#                 break
#             elif choose < number:
#                 print("Too Low")
#                 chances -= 1
#                 if chances ==0:
#                     print("Running out of chances, You Lose...")
#                     break
#                 print("Guess again")
#                 print(f"Remaing {chances} chances you have")
#
#             elif choose > number:
#                 print("Too High")
#                 chances -= 1
#                 if chances ==0:
#                     print("Running out of chances, You Lose...")
#                     break
#                 print("Guess again")
#                 print(f"Remaing {chances} chances you have")
#
#
# if difficulty == "easy":
#     chances=10
#     while chances != 0:
#
#         if chances !=0:
#             choose = int(input("Make a Guess : "))
#             if choose==number:
#                 print("You Win!")
#                 break
#             elif choose < number:
#                 print("Too Low")
#                 chances -= 1
#                 if chances ==0:
#                     print("Running out of chances, You Lose...")
#                     break
#                 print("Guess again")
#                 print(f"Remaing {chances} chances you have")
#
#             elif choose > number:
#                 print("Too High")
#                 chances -= 1
#                 if chances ==0:
#                     print("Running out of chances, You Lose...")
#                     break
#                 print("Guess again")
#                 print(f"Remaing {chances} chances you have")
#

# Aengilas code

from random import randint

EASY_LEVEL_TURNS = 10

HARD_LEVEL_TURNS = 5
turns =0

# Function to check users' guess against actual answer

def check_answer(user_guess, actual_answer,turns):

    if user_guess > actual_answer:

        print("Too high.")
        return turns - 1

    elif user_guess < actual_answer:

        print("Too low.")
        return turns -1

    else:

        print(f"You got it! The answer was {actual_answer}")
#Function to set difficulty

def set_difficulty():

    level= input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":

        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#Choosing a random number between 1 and 100.
def game():
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    #  Let the user guess a number
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))

        check_answer(guess, answer, turns)
game()


