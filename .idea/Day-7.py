import random

from numpy.f2py.symbolic import eliminate_quotes

stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r''' 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()

word_list = ["happy","kindness","verygood","normal","hardwork"]
lives =6
choose = random.choice(word_list)
print(choose)
space=len(choose)
word=""
for i in range(space):
    word +="_"
print(word)
game_ovear = False
correct_letters =[]
while not game_ovear:
    Guess = input("Guess a letter: ").lower()

# print(Guess)
    display=""
    k=len(stages)
    for letter in choose:
            if letter==Guess:
                display += letter
                correct_letters.append(Guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += '_'
    print(display)
    if Guess not in choose:
        lives -= 1
        if lives == 0:
            game_ovear=True
            print("You lose!")

    if '_' not in display:
            game_ovear=True
            print("You win!")
    print (stages[lives])








