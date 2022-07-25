"""
Exercise 3: Turn every item of a list into its square
"""

numbers = [1, 2, 3, 4, 5, 6, 7]
square = []

for i in range(1,len(numbers)):
    square.append(i*i)
print(square)