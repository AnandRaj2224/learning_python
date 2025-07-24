# syntax ------> same as js object

about_me = {
    "name" : "anand raj",
    "height": "6 feet 1 inch",
    "college_year": 4,
    "employed": False
}
# another way to create dictionary(objects)
learning_status = dict(learning_python = True)

# accessing the values

print(about_me["name"])

for v in about_me.values(): # .values() return a iteratable array of values
    print(v)

print()

for v in about_me.keys():  # .keys() return a iteratable array of keys
    print(v)

print()

for key,value in about_me.items():  # .items() return a iteratable array of keys,values[key,value]
    print(f"{key} : {value}")

# to check if a key is present in dictionary
is_present = "name" in about_me.keys()
# can do this with in about_me.keys()|.values()
print(is_present)


# DICTIONARY METHODS

d = dict(my_luck = 0)

d.clear() # removes everything

c = d.copy() # copy key,values of dictionary d in c

d = {}.fromkeys(["first","one","start"],1) # can set values of keys to 1 value


d.get("one") # check if key present if ! present returns none

d.pop("first") # removes the key,value pair and returns value for key passed

checker = d.popitem() # removes a key,value pair at random returns them

d2 = dict(original_one = 1)

d2.update(d) # take the passed dict and appends it after the dict the method is used on

# DICTIONARY COMPREHENSION
# syntax  {key : value FOR key IN dictionary} ---> oprations on key ,values
squares = {num : num**2 for num in [1,2,3,4,5]}


for key,value in squares.items():
    print(f"{key} : {value}")
