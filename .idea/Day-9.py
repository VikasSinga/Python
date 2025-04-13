programming_dictionary ={"Bug":"An error in program that prevent program to run",
                        "function":"A piece of code that you can easyly call ovear and ovear again"

                     }
print(programming_dictionary["function"])
programming_dictionary["loop"]="The action of doing somthing ovear and ovear again"
print(programming_dictionary)

empty_dictionary={}

# Clear a dictionary
# programming_dictionary={}
# print(programming_dictionar
programming_dictionary["function"]="A celebration st home"
print(programming_dictionary["function"])

for items in programming_dictionary:
    print(items+":")
    print(programming_dictionary[items])


# student_grades = {}
#
# # Loop through each key in the student_scores dictionary
# for student in student_scores:
#
#     #Get the value (student score) by using the key each time.
#     score = student_scores[student]
#
#     #Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'

# Normal
capitals = {
    "India":"delhi",
    "bangladesh":"dhaka"

}

#  Nested

# traval_log={
#     "France":["paris","lille","Dijon"],
#     "Germany":["Stuttgart","berlin"]
# }
#
# print(traval_log["France"][1])
# traval_log={
#     "France":{
#         "cities_visited":["paris","lille","Dijon"],
#         "total_visits":12
#     },
#     "Germany":{
#         "cities_visited":["Berlin","hamburg","Stuttgart"],
#         "total_visits":5
# }}
# print(traval_log["France"]["cities_visited"][1])

hammer='''
            T                                    \`.    
       |    T     .--------------.___________) \   |    T
       !    |     |//////////////|___________[ ]   !  T |
            !     `--------------'           ) (      | !
                                         mn  '-'      !          
        '''

print(hammer)
# def bidding(bidder_name,bid_amount):
#     bids ={name:bid}
# bids={}
# Any_other_biders = True
# while Any_other_biders:
#     name = input("What is your name: \n")
#     bid  = int(input("At what prise you are going to Bid $ \n"))
#     # bidding(bidder_name=name,bid_amount=bid)
#     bids.update({name:bid})
#     last=input("Is there any other bidders in the room \n").lower()
#     if last == "no" :
#         Any_other_biders=False
#         k=[]
#         for i,j  in bids.items():
#             k.append(j)
#         k.sort()
#         for i,j  in bids.items():
#             if j==k[-1]:
#                 print(i)










    # last=input("Is there any other bidders in the room \n").lower()
# Angelas code
def find_highest_bidder(bidding_dictionary):

    winner =""

    highest_bid=8

    max(bidding_dictionary)

    for bidder in bidding_dictionary:

        bid_amount = bidding_dictionary [bidder]

        if bid_amount > highest_bid:

            highest_bid>bid_amount

            winner=bidder

    print(f"The winner is {winner} with the bid of {highest_bid}")


bids={}
continue_bidding = True
while continue_bidding :

    name=input("What is your name?: ")

    price=int(input("What is your bid?: $"))

    bids [name]=price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")

    if should_continue == "no":

        continue_bidding = False

        find_highest_bidder(bids)

    elif should_continue == "yes":

        print("\n"*28)


