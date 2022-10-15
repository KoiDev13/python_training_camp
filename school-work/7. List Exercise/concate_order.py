"""
Exercise 4: Concatenate two lists in the following order
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newList=[]

for x in list1:
    for y in list2:
        newList.append(x+y)
print(newList)