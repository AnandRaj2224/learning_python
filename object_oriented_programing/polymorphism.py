# polymorphism --> 1 into many forms
"""
use cases:
1. using method overriding to have 2 or more class with same named method which behaves differently depending on who called it.

2. operator overriding ---> same as method but with operators such as + etc
"""

# special methods ---> polymorphism

"""
'+' ---> it a shorthand for calling __add__() 
if the first operand is int type it does addition --> 5+4 = 9

if the first operand is str/char type it does concatination ---> "4" + "5" = "45"
"""

class Human:
    def __mul__(self,any):
        print("U are multiplying HUMANS \n U HAVE ACHEIVED POLYMORPHISM\n")

anand = Human()
anand*5