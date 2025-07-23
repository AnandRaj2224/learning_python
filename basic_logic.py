'''
# input syntax 
first_input = input("the way to take inputs in python (input taken is a string)\n")
print("\n"+first_input)
# conditional statements
name = input("enter your name\n")

if name == "Anand Raj":
    print("W rizz")
elif name == "anand raj":
    print("L rizz")
else :
    print("stop gooning")


# logical AND,OR 
screen_time = int(input("enter your screen time\n"))
age = int(input("enter your age\n"))

if screen_time >= 0 and screen_time <= 1 :
    print("Bruh, you actually out here living?")
elif screen_time >= 10 and age >= 25 :
    print("ayy, we got a reddit mod here")
elif screen_time >= 7 or age >= 20 :
    print("full time gooner")
'''
# loops

# for loop syntax

name = "Anand raj"
print("The Characters in your Name are:\n")
for char in name:
    print(char)


# range --- can print numbers in range (0,5) --> prints 0,1,2,3,4.
# can also only give end ===> range(5) ---> 0,1,2,3,4.

for num in range(11):
    print(num) 
