"""
Exercise 1B: Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.
"""

def name_create(str):
    mid = len(str)//2
    return str[mid-1] + str[mid] + str[mid+1]

str1 = "JhonDipPeta"
str2 = "JaSonAy"

name1 = name_create(str1)
name2 = name_create(str2)

print(name1)
print(name2)