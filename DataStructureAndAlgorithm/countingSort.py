data = [4, 2, 2, 8, 3, 3, 1]

size = len(data)
print(f"Size: {size}")

output = [0] * size
cnt = [0] * 10

# dem so 
for i in range(len(cnt)):
    cnt[i]=data.count(i)
print(f"Count xong {cnt}")

i = size - 1
while i >= 0:
    output[cnt[data[i]-1]] = data[i]
    cnt[data[i]] -= 1
    print(f"Count: {cnt}")
    print(f"Output: {output}")
    i -= 1
