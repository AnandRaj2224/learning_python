"""
iterator ---> an object that can be iterated upon.an object which return data,one element at a time when next() is called on it.

iterable ---> an object which return a iterator when iter() is called on it.

next() ---> when called upon a iterator it return the next item. it keeps going untill stopIteration error
"""

# custom for Loop 

def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
          i = next(iterator)
        except: 
            StopIteration
            break
        else:
            func(i)

my_for([1,2,3,4,5,6],print)


# generators
"""
genrators are iterators
genreators can be created with generator functions
it uses yield keyword
"""

def count_upto(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counterr = count_upto(5)

next(counterr)

# generator expresssion

def count_upto(max):
    for num in range(1,max):
        yield num