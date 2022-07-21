"""
Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication
"""
def multiply(number1, number2):
    """Ham nay dung de tinh phep nhan."""
    return number1 * number2

print("Nhap 2 so nguyen:")
num1 = int(input())
num2 = int(input())

kq=multiply(num1, num2)
print(f'{num1} nhan voi {num2} bang {kq}')