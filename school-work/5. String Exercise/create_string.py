"""
Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.
"""
def name_create(str):
    return str[0] + str[len(str)//2] + str[-1]

str1 = "James"
str2 = "Khoi"
name = name_create(str1)
print(name)
name1 = name_create(str2)
print(name1)
