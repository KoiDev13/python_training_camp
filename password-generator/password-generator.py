"""
This is generator is used for generating password
Conditions:

1/ Contains letter
2/ Contains number
3/ Contains punctuation
"""
import string
import random

def passwordLength():
    password_length = input('How long the password you want: ')
    return int(password_length)

def passwordGenerator(length=8):
    CHARACTER = string.ascii_letters
    NUMBER = string.digits
    PUNCTUATION = string.punctuation

    passwordable = f"{CHARACTER}{NUMBER}{PUNCTUATION}"
    passwordable = list(passwordable)
    random.shuffle(passwordable)
    random_password = random.choices(passwordable,k=length)
    random_password = ''.join(random_password)
    return random_password


def main():
    password_length = passwordLength()
    password = passwordGenerator(password_length)
    print(password)

if __name__ == "__main__":
    main()