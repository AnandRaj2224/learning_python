# higher order function
'''
takes other functions as args or returns functions

example 

def full_name(func):
    name = input("enter your full name\n")
    return func(name)

def greeting(name):
    print(f"hello {name}")

full_name(greeting)


'''

# decorators
'''
decorators ---> are higher oder functions
                they wrap around other functions and inhance their behavior
                they use @ --> syntatical sugar for higher order functions
'''

def first_name(func):
    f_name = input("enter your first Name\n")
    return func(f_name)

@first_name
def greeting_first_name(f_name):
    print(f"hello {f_name}\n")


# ---> dont have to do this first_name(greeting_first_name)
first_name()