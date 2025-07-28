# status codes --->2xx ==> ok sucessful
#                  3xx ==> redirect
#                  4xx ==> client error
#                  5xx ==> server error 

# HTTP VERBS

#GET ---->  useful for retriving data
#           data is passed in query strings

# POST ----> useful for writing data
#            data is passed on request body

# APIs ----> allows to get data from other applications without needing to know how it works
#            it a version of the application intended for computer/other programs to interact with


# using request modules

import requests

# res = requests.get("https://news.ycombinator.com/")
# print(res)
# print(res.ok)
# print(res.headers)
# print(res.text)

url = "https://icanhazdadjoke.com/"
# respone = requests.get(url,headers= {"Accept" : "text/plain"})
respone1 = requests.get(url,headers= {"Accept" : "Application/Json"}) # need to get json for doing anything to the data

print(respone1.text) # this returns a string 
data = respone1.json() # to convert to python dictionary

print(data["joke"])

# QUERY STRING ----> a way to pass data to a server as part of a GET request

# htttps://name/search?key=value&key=value <---- syntax

# EXAMPLE
# https://www.google.com/search?
# q=cs&
# oq=cs&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiRAhiABBiKBTINCAIQABiRAhiABBiKBTIMCAMQABhDGIAEGIoFMgwIBBAAGEMYgAQYigUyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgyMjExajBqN6gCCLACAfEFz8YwMPc1nUo&sourceid=chrome&ie=UTF-8

url2 = "https://icanhazdadjoke.com/search"
respone2 = requests.get(url2,
                        params= {
                            "term" : "sea"
                        },headers= {"accept" : "application/json"})

print(respone2.text)
data2 = respone2.json()
