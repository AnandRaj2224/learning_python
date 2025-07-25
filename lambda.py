# lambda ----> like anonymous functions in js

# syntax
anonymous = lambda: print("i am anonymous")
anonymous()

# map() ---> take 2 args 1-> anonymous function or normal function to do stuff , 2--> data ,its like map() in js
nums = [1,2,3,4]
double  = list(map(lambda x:x**2,nums))
print(double)

# filter() --> takes 2 args one function and data , run function through data, if it true it gets into new object, return new object that can be converted into other type 

even = list(filter(lambda x: x%2 == 0,nums))
print(even)


# MORE BUILT-IN FUNCTIONS

all([1,2,3,4,5,False]) # return true if only if all the val are truthy
any([1,2,3,4,5,False]) # return true if any val are truthy

sorted([5,6,7,833,10,99], key= lambda x: x%2) # takes 2 args 1st the data ,and the premeter to sort them

max([999,3444,910,32,1],key=lambda x:len(x)) # return max value
min([999,3444,910,32,1]) # return min value

reversed("hello world") # returns dlr... reversed string or any other itrateable object

len("anand") # can run on any iteratable object in background ---> calls .__len__() method of the class of thing u are passing, list,dictionary,string.

abs(-11) # returns absolute value of a number 
sum([10,10],10) # val ,start adds everything to start the return the val
round(1.555,1) # rounds the val to specified digits

zip([1,2][3,4]) # returns (1,3),(2,4)