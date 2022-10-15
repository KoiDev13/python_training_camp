"""
Exercise 2: Concatenate two lists index-wise
"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list = []

for i in range(len(list1)):
    list.append(list1[i] + list2[i])
print(list)
    
