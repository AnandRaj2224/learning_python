# list syntax ===> same as array
values = [1,'Anand raj',3.14,False]
# when used with (-ve) indices it start from the end of the list
print(values[-1])

# in ----> check be used to access list 
if 1 in values:
    print(True)

for val in values:
    print(val)

# len ----> for length of the array
print(len(values))

# LIST METHODS

values.append("added") # for appending 1 element
values.extend(["extended", 69,"*","$"]) # for appending multiple items

# list.append ---> ([1,2,3,4]) ===>  [prev],[1,2,3,4]
# list.extend ---> ([1,2,3,4]) ===>  [prev,1,2,3,4]

values.insert(4,"inserted here") # it insert value at specified index

fake_value = ["dead","dead"]
fake_value.clear() # it clears the whole list  ==> remove all the values

values.pop(3) # removes a specified index value, or if no index provided the last index

values.remove(3.14) # remove the first value in the list that match passed value ,if not found throws error

values.index("inserted here") # returns index of passed value can also give ===> index(value,start,end)

values.count(3.14) # returns the no of count of value passed

values.reverse() # reverses the list --> inplace

values.sort() # sorts the list asending order ---> inplace 


# list.slice ====> returns a list from the passed start and end
# list[start : end : step]   

new_values = values[2:4:1]