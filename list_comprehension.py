# syntax for list comprehension

values = [1,222,55,34,11,99,10]
my_name = "anand raj"
# explaination ---> [operation on x FOR x IN list]  returns the new list
new_values =        [val*10 for val in values];
my_name = [char.upper() for char in my_name]

print(my_name)
print(new_values)

# list comprehension with conditional logic

# explaination ---> [only that x FOR x IN list if condition satisfied]
new_values = [val for val in values if val % 2 != 0]

print(new_values)

# explaination ---> [operation on x IF conditon true ELSE other operation for each x in list]
new_values = [val*2 if val % 2 != 0 else val-1 for val in values]
print(new_values)
