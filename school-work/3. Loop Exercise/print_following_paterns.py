"""
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.
"""
row_num=5
for i in range(1, row_num+1, 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print(" ")