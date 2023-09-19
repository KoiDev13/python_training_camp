testStr = 'ABCDCDC'
subStr = 'CDC'
count = 0

print(len(subStr))
for i in range(0, len(testStr)):
    if testStr[i: i+ int(len(subStr))] == subStr:
        count += 1
        print("Phat hien 1")
print(count)