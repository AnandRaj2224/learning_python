# OOP --> a method to model things from life in code using class and object

# class --> a bluePrint for objects,they specify what object should contain
#           they contain methods(functions) and attribuites

# instance --> objects that are constructed from class bluePrint what contain the methods and attribuite.

# syntax
class UserClass: # ---> class syntax use the js name scheme for it 

    active_user = 0 # class attribuite

    @classmethod # --> class method syntax

    def display_active_users(cls):
        return f"the number of active users is : {UserClass.active_user}"

    def __init__(self,first,last,age): # constructor function def __init__(self) ,self ---> pointer to that instance
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first}"

    def full_name(self): # instance method syntax
        print(self.first + " " + self.last)

    def log_in(self):
        UserClass.active_user +=1

    def log_out(self):
        UserClass.active_user -=1

user1 = UserClass("Anand","Raj",23) # ---> to initiate use = className()
print(user1.first)
print(user1.last)
print(user1.age)

user1.full_name()

print(UserClass.display_active_users())
print(user1)