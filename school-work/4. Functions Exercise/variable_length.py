"""
Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.
"""

def func1(*args):
    print("printing values:")
    for i in args:
        print(i) #print items trong tuple

# call function with 3 arguments
func1(20, 40, 60)
# call function with 2 arguments
func1(80, 100)