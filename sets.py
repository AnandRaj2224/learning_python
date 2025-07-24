# sets ====> like maths sets
# sets are like dictionaries but they are not key value pair
# sets cant have duplicate values
# unordered ,can be accessed via index

# syntax
s = {1,2,3} # one way

s = set({1,2,3,4,5}) # another way

# accessing
print(5 in s) # returns true or false

for num in s:
    print(num)

# SET METHODS

s.add(6) # insert /adding new elements 
s.remove(2) # remove the element
s.discard(2) # same as remove but wont throw error if val not in set
ss = s.copy() # copy s into ss
ss.clear() # remove everything

# sets can be used to do set maths

bio_students = {"arti","anand","ram","ramesh"}
cs_students  = {"anand","harsh","naman"}

# set operation union(\) ----> gives all the elements excluding commons
all_students = bio_students | cs_students

# set operation intersection(&) ----> gives all the common elements only
double_major = bio_students & cs_students

print(all_students,double_major)

# SET COMPREHENSION

s = {num**2 for num in range(5)}
print(s)