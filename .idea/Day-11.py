# Black Jack Problem
import random

print("Welcome to the Black Jack Problem")
cards=['11','2','3','4','5','6','7','8','9','10','10','10','10']
player=[]
computer=[]

player.append(int(random.choice(cards)))
player.append(int(random.choice(cards)))
computer.append(int(random.choice(cards)))
computer.append(int(random.choice(cards)))
# print(f"The cards you got selected is: {player}")
# print(f"Computer {computer}")
# player_total = player[0]+player[1]
# computer_total = computer[0]+computer[1]
# print(player_total)
# print(computer_total)

# if player[0]+player[1] == 21 :
#     if computer[0]+computer[1] != 21:
#         print("Player has Black Jack")
#     else:
#         print ("Computer has Black Jack")
# elif player[0]+player[1] > 21:
#     for i in range(len(player)):
#         if player[i] == 11:
#             player[i]=1
#             if player[0]+player[1] > 21:
#                 print("You Lose")
#         else:
#             print("You Lose")

#My Code
# if player[0]+player[1] <= 21:
#       # player.append(int(random.choice(cards)))
#       # player.append(int(random.choice(cards)))
#       # computer.append(int(random.choice(cards)))
#       # computer.append(int(random.choice(cards)))
#       print(f"The cards you got selected is: {player}")
#       print(f"Computer {computer}")
#       player_total = player[0]+player[1]
#       computer_total = computer[0]+computer[1]
#       print(player_total)
#       print(computer_total)
#       draw_cards = True
#       draw_card=input("Please select another vcard \n").lower()
#       # draw_card=input("Please select another vcard \n").lower()
#       while draw_cards:
#           # draw_card=input("Please select another vcard \n")
#           # draw_card=input("Please select another vcard \n").lower()
#           player[0]=player_total
#           player[1]=int(random.choice(cards))
#           print(player[1])
#           computer[0]=computer_total
#           computer[1]=int(random.choice(cards))
#           print(computer[1])
#           if player[0]+player[1] == 21 :
#             if computer[0]+computer[1] != 21:
#                 print("Player has Black Jack")
#                 break
#             else:
#                 print ("Computer has Black Jack")
#                 break
#           elif player[0]+player[1] > 21:
#             for i in range(len(player)):
#                 if player[i] == 11:
#                   player[i]=1
#                   if player[0]+player[1] > 21:
#                     print("You Lose")
#                     break
#                 else:
#                  print("You Lose")
#                  break
#             break
#
# while not draw_card:
#         if computer_total > 21:
#             print("You Win..")
#         elif player_total > computer_total:
#             print("You Win..")
#         elif computer_total > player_total:
#             print("You Lose..")
#         elif player_total == computer_total:
#             print("Game Draw")


# Aegilas code

import random

# 2 usages

def deal_card():

    """Returns a random card from the deck"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card=random.choice(cards)
    return card
def calculate_score (cards):

    if sum(cards) == 21 and len(cards) == 2:

        return 0

    if 11 in cards and sum(cards) > 21:

        cards.remove(11)

        cards.append(1)

        return sum(cards)
def compare(u_score, c_score):

    if u_score == c_score:

        return "Draw"

    elif c_score == 0:

        return "Lose, opponent has Blackja"

    elif u_score == 0:

        return "Win with a Blackjack"

    elif u_score > 21:
      return "You went ovear, you lose"

    elif c_score > 21:

        return "Opponent went over. You win"

    elif u_score > c_score:
        return "you win"
    else:
        return "You Lose"


user_cards = []
computer_cards = []
computer_score=-1
user_score=-1
is_game_over =False

for _ in range(2):

    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while not is_game_over:

    user_score=calculate_score (user_cards)

    computer_score=calculate_score (computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")

    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:

        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")

        if user_should_deal == "y":

            user_cards.append(deal_card())
        else:

            is_game_over = True

while computer_score != 0 and computer_score < 17 :

    computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)
print(compare(user_score,computer_score))









