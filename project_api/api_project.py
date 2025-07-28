import random
import requests

url = "https://icanhazdadjoke.com/search"

print("WELCOME TO DAD JOKE GENERATOR\n")
topic = input("what topic do u want a joke on \n")

respone = requests.get(url,
                       headers={
                           "Accept" : "application/json"
                       },
                       params={
                           "term" : topic
                       })

data = respone.json()
total_jokes = data["total_jokes"]

print(f"The total Number of jokes are - {total_jokes}\n")
jokes_wanted = int(input("enter the number of jokes u want\n"))

while jokes_wanted != 0:
    indx = random.randint(0,total_jokes-1)
    print(data["results"][indx]["joke"])
    print()
    jokes_wanted -= 1
