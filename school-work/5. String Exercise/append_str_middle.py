"""
Exercise 2: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""

def concate_name(str1, str2):
    return str1[0:len(str1)//2]+str2+str1[len(str1)//2:]

s1 = "Ault"
s2 = "Kelly"
name = concate_name(s1, s2)
print(name)
