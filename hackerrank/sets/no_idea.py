# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
l = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
happy = 0 

# for i in l:
#     if i in setA:
#         happy += 1
#     elif i in setB:
#         happy -= 1
# print(happy)
print(sum([1 for i in l if i in setA]) - sum([1 for j in l if j in setB]))
