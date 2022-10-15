"""
Exercise 3: Calculate the sum of all numbers from 1 to a given number
"""

def sum(a):
    kq=0
    for i in range(1,a+1,1):
        kq = kq + i
    return kq

print("Nhap so: ", end=" ")
n = int(input())
kq = sum(n)
print(f"Tong tu 1 de {n} bang {kq}")