#Subscripting
print("hello"[0])
print("hello"[-1])

print("123"+"345") #concatinating
print(123 + 345)# it will  add
#large integer
print(123_345_567)

#floating point
print(3.3456)

#Boolean
print(True)
print(False)

print(type("geook"))
print(type(123))
print(type(True))
print(type(3.567))

# Type casting
print(int("123"))

print(int("123")+int("345" ))
print(bool(3))
print("Number Of letters in your name: "+str(len(input("Enter Your name"))))
# print(type("Number Of letters in your name: "))
# print(type(str(len(input("Enter Your name")) ) ) )
print("my_age: "+str(26))
print(123+345)
print(7-34)
print(3*2)
print(3/3) #with floating point
print(6//3)#with out floating point
print(2**4)# it will give exponent


#PEMDASLR #precedence
# ()
# **
# *
# /
# +
# -
print(3*3+3/3-3)
bmi=84/1.64**2
print(int(bmi))
print(round(bmi))
print(round(23.65778))
print(round(23.6574, 2))

score = 0
height = 1.8
is_winning = True
# score += 2
# print(score)

# f string
# print("your Score is: "+str(score))
print(f"your winning socre is : {score} your height if {height} ")
print(4/2)


# TIP Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip =int(input("how much tip would you like to give? 10,12, or 15?"))
share = int(input("How many people split the bill?"))
k=(tip/100*bill+bill)
n=(k/share)
g=round(n,2)
print(f"Each person should pay: ${g}")






