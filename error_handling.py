# to throw(called raise in python) errors

age =  input("enter your age\n")
if type(age) is not str:
    # syntax
    raise TypeError("input can only be integer type\n")
else:
    print(age)

# try and except -----> try and catch in other languages.

d = {"wb" : "kolkata"}

def get(d,key):
    try:
        d[key]
    except KeyError:
        return None

print(get(d,"delhi"))

# try , except else and finally -----> try this, if does not work except runs, if except does not run else with run and finally will always run

while True:
    try:
        num = int(input("enter a number\n"))
    except:
        print("thats not a number\n")
    else :
        print("yes that a number\n")
        break
    finally:
        print("it will run always\n")