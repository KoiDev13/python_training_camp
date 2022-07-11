"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
"""

print("Nhap input vao:")
n = int(input())
print(f'Printing current and previous number sum in a range({n})')
pre = 0

for i in range(n):
    print(f'Current Number {i} Previous Number {pre}  Sum: {pre + i}')
    pre = i