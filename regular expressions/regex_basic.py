import re

pattern  = re.compile(r'\d{3}-\d{3}-\d{4}')

res = pattern.search("adhoiwhfoiehfoihfob")
print(res)

res = pattern.search("my phone number is 111-111-1111")
print(res)

if res is not None:
    print(res.group())

res = pattern.search("my phone number is not 111-11-111")
print(res)

