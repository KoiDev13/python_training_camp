"""
Print downward Half-Pyramid Pattern with Star (asterisk)r
"""

for i in range(10, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")