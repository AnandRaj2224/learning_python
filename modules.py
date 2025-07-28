# built-in modules
import random # ---> import keyword followed by module name
import random as my_random # ----> can give alias to modules with use of 'as' keyword
from random import randint # ----> can using from module name import specific method/function 

# custom modules ----> u can import your own code/functions/classes/etc
#  syntax ---->  import file_name

# external modules ---> download from internet using (pip) 
#  pip package/module name 
from termcolor import colored
# help(termcolor) ---> explain everything on the modules(docs)

text = colored("hi there", color = "red", on_color="on_white")
print(text)