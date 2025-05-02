import random


def my_function():
    for i in range(1,21):
        if i==20:
            print("You got it")
my_function()

dice_images =["!", "@","#","$","%","^"]
duce_num=random.randint(0,5)
print(duce_num,dice_images[duce_num])

year = int(input("What is your year of birth"))

if year > 1980 and year < 1994:
    print("You are a millennial")
elif year >= 1994:
    print("You are a Gen Z.")
else:
    print("Enter the valid Year")

age=int(input("What is Your Age"))
if age >18:
    print(f"You can drive at the age : {age}")
else:
    print("Not Authorised")