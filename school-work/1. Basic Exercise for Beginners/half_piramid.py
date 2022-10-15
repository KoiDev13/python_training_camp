"""
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)r
"""

print("Nhap input vao:")
n = int(input())
print(f'Ve tam giac co n bang ({n})')

for i in range(n, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print(" ")