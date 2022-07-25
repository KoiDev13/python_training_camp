"""
Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
"""

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


odd_items = []
def get_odd(ls):
    odd_item=[]
    for x in range(len(ls)):
        if x%2 != 0:
            odd_item.append(ls[x])
    return odd_item


even_items = []
def get_even(ls):
    even_item=[]
    for x in range(len(ls)):
        if x%2 == 0:
            even_item.append(ls[x])
    return even_item

odd_items = get_odd(l1)
even_items = get_even(l2)


print(odd_items)
print(even_items)
print(odd_items + even_items)