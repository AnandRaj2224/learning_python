# syntax to define a function

def first_python_function(name = "Anand"):  # default parameter for name 
    '''def ---> define (always to use to define a function) '''
    print(name)

first_python_function()

print(first_python_function.__doc__) # .__doc__ gets the multi-line comments 

# *args ---> takes all args passed and make them 1 tuple

def second_python_function(*args):
    print(args)

second_python_function(1,2,3,4,5,6,7,8)

# **kwargs ---> takes all args passed and make them 1 dictionary

def third_python_function(**kwargs):
    print(kwargs)

third_python_function(first_name="anand",last_name="raj")

# unpacking

def sum_all(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all(*[1,2,3])) # *[1,2,3] ==> it take the elements as seperate args

# **{name : anand} ===> for unpacking dictionaries