# # if statements
# water_leve1=40
# if water_leve1 >80:
#     print ("Drain")
# else:
#     print("Continuve")
#
# Rollercoster problem
# print("Welcone to Rollercoaster")
# height = int(input("what is your Height in cm? "))
# if height >= 120:
#     print("You can rode the rollercoaster")
#     age = int(input("What is your age: "))
#     if age < 12:
#         bill =5
#         print("Chaild Tickets $5")
#     elif age > 12 and age < 18:
#         bill=7
#         print("Youth Tickets $7")
#     elif 45 <= age <= 55:#age >= 45 and age <= 55:
#         print("Free Tickets")
#     else:
#         bill = 12
#         print("Adult tickets $12")
#     wants_photo=input("Do you want to have a photo take? type Y for Yes  and N for NO. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Total bill you hae to pay is ${bill}")
#
# else:
#
#     print("Sorry You have to grow toller to get ride")

#
# # Enen or Odd
# number = int(input("enter the number"))
# if number % 2 ==0:
#     print("the Number ie Even")
# else:
#     print("The number is ODD")
# print(number%2)
#
# # Pizza Order

# print(("Welcome to python pizza Deliveries!"))
# Size = input("What size pizza do you want? S, M, or L: ")
# Pepperoni = input("Do You want pepperoni on your pizza? Y or N : ")
# extra_chease = input("Do you ewant extra chease? Y or N: ")
# if Size == "S":
#      bill = 15
#      if Pepperoni == "Y":
#          bill += 2
#          if extra_chease == "Y":
#              bill += 1
#      print(f"Your final bill is: ${bill}")
# elif Size == "M":
#     bill = 20
#     if Pepperoni == "Y":
#         bill += 3
#         if extra_chease == "Y":
#             bil += 1
#     print(f"Your final bill is: ${bill}")
# elif Size == "L":
#     bill = 25
#     if Pepperoni == "y":
#         bill += 3
#         if extra_chease == "Y":
#             bill += 1
#     print(f" Your total bill is : ${bill}")
# else:
#     print("You Typed a worng input")

# if Size == "S":
#      bill = 15
# elif Size == "M":
#     bill = 20
#
# elif Size == "L":
#     bill = 25
# else:
#     print("You Typed a worng input")
#
# if Pepperoni == "Y":
#     if Size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_chease == "Y":
#     bill += 1
#
# print(f"Yoyr final bill is: ${bill}")


# Treasuer Hunt
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print(" Welcome To the Treasure Hunt")
cross_Road=(input("You are at a Cross Road. Whrae do you want to go? 'Left' or 'right' "))
if cross_Road == "Right":
    print("Fall into HOLE Game Over")
elif cross_Road == "Left":
    River = input("You Reached Rever.there is an island? you want Swim or wait? ")
    if River == "Swim":
        print("Killed By Crocodail,Game Over")
    elif River == "Wait":
        Door = input("You reached island, here you have 3 doors RED, YELLOW, BLUE Which One you want to Opean")
        if Door == "RED".lower():
            print('''
                       (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             ''')
            print("Fall into fire pit,Game Ovear")
        elif Door == "YELLOW".lower():


            print("You Won")
        elif Door == "BLUE".lower():
            print('''
                        (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            ''')

            print("eaten by beasts, Game Ovear")





