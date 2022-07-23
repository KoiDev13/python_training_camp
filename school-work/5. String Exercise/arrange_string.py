"""
Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
"""


str1 = 'PyNaTive'
upper=[]
lower=[]
for i in str1:
    if i.islower()==True:
        lower.append(i)
    else:
        upper.append(i)
# newstr= lower + upper
newstr = (''.join(lower + upper))
print(newstr)