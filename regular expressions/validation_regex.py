import re

def extract_mobile_number(input):
    mobile_regex = re.compile(r"^(6|8|9)(\d{9})$")
    match = mobile_regex.search(input)
    if match is not None:
        return match.group()
    return None

print(extract_mobile_number("912456789"))