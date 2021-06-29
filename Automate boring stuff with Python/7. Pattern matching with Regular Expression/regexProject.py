import re

def dateDetection(text):
    dateRegex = re.compile(r'^(0[1-9]|1[1-9]|2[1-9]|3[01])\/(0[1-9]|1[012])\/(1\d{3}|2\d{3})$')
    mo1 = dateRegex.search(text)
    print("Date found is " + mo1.group())


def strongPassword(text):
    # strongpassRegex = re.compile(r'^(?=.?[A-Z]$)(?=.?[a-z]$)(?=.?[0-9]$)(?=.*?[#?!@$%^&*-]).{8,}$') # Error typo
    strongpassRegex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')                             
    mo2 = strongpassRegex.search(text)
    print(mo2.group() + " is strong password")#

"""
This regex will enforce these rules:

At least one upper case English letter, (?=.*?[A-Z])
At least one lower case English letter, (?=.*?[a-z])
At least one digit, (?=.*?[0-9])
At least one special character, (?=.*?[#?!@$%^&*-])
Minimum eight in length .{8,} (with the anchors)
"""
def regex_strip(s, chars = None):

    if chars == None:
        strip_left = re.compile(r'^\s*')
        strip_right = re.compile(r'\s*$')

        s = re.sub(strip_left, "", s)
        s = re.sub(strip_right, "", s)
    else:
        strip_left = re.compile(r'^[' + re.escape(chars) + r']*')
        strip_right = re.compile(r'[' + re.escape(chars) + r']*$')
        s = re.sub(strip_left, "", s)   
        s = re.sub(strip_right, "", s)
    return s

# # print("Insert a date (DD/MM/YYYY):")
# # date = input()
# dateDetection(date)

# print("Insert a password to check whether it strong or not:")
# password = input()
# strongPassword(password)



