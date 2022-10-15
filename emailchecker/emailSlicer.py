import re
from sqlalchemy import false, true

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validateEmail(email)->bool:
    if(re.fullmatch(regex,email)):
        return true
    else:
        return false

def emailProcessing(email):
     """This function use for slicing email to username and domain"""
     user_name = email[0:email.index("@")]
     domain_name = email[email.index("@")+1:]
     return [user_name, domain_name]

def printMsg(user_name, domain_name):
    print(f"User name is {user_name}\nDomain name is {domain_name}")

def main():
    """This is main function."""
    try:
        email=input("Insert your email:")
        # print(f"Hello {email}")
        valid = validateEmail(email)
        if valid == true:
            print("Valid email!")
            user_name, domain_name = emailProcessing(email)
            printMsg(user_name, domain_name)
        else: 
            print("Invalid email!")
    except:
        print("Debug please!")