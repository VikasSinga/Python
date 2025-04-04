# Random Module
# import random
#
# import my_module
#
# random_integer=random.randint(23, 34)
# print(round(random.random()*10))
# print(random.uniform(20,40))
# print(random_integer)
# print(my_module.my_favourite_number)

#  coin toss
import random

# number = round(random.random())
#
# if number%2 == 0:
#     print("HEAD")
# else:
#     print("TAIL")
#
# # LISTS
#
# states = ["AP", "TN", "KA","TN", " AK"]
# print(states[0])
# print(states[-1])
# states[-1] = "KA"
# print(states[2])
# states.append("HS")
# print(states)
# print(len(states))
#
# # random card selection
# cards = ["vikas", "Golul","Dille","sai","bhargav"]
# # first choice
# print(random.choice(cards))
#
# #secound Choice
# random_index = random.randint(0,4)
# print(cards[random_index])
#
# fruits = ["apple", "banana", "mango", "orange", "grapes", "watermelon", "pineapple", "strawberry"]
# vegitables = ["Ash gourd","Broccoli	","Cucumber","Celery",
#               "Bitter gourd	Elephant ya]"]
# bunch = (fruits, vegitables)
# print(bunch)
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
game_images = [Rock,Scissors,paper]
me = int(input("What You are going to choose 0(Rock), 1(Scissors), 2(Paper) ?"))
game = ["Rock","Scissors","Paper"]
system= random.randint(0,2)

print(game_images[me])
print(game[me])
print(game_images[system])
print(game[system])
if (me == 0 and system ==1) or (me == 1 and system== 2)or (me==2 and system == 0):
    print("You Win!")
elif game[me]==game[system]:
    print("Draw")
else:
    print("You Lose")

