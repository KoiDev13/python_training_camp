"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
"""

def product(number1, number2): 
    """This function used for sum 2 numbers."""
    product = number1 * number2
    if product <= 1000: 
        return product
    else:
        return number1 + number2

#Product < 1000
print('The result is ', product(20,30))

#Product > 1000
print('The result is ', product(200,300))