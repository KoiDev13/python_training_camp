"""
Exercise 2: Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
"""
list_sample = [34, 54, 67, 89, 11, 43, 94]
print(list_sample)
number = list_sample.pop(4)
print(list_sample)
list_sample.insert(2, number)
print(list_sample)
list_sample.append(number)
print(list_sample)