
arr = [
    [11,2,4],
    [4,5,6], 
    [10, 8,-12]
]

primary_diagonal = 0 
sencond_diagonal = 0

for i in range(len(arr)):
    primary_diagonal += arr[i][i]
    sencond_diagonal += arr[i][(len(arr)-1)-i]

reSult = abs(primary_diagonal-sencond_diagonal)
print(reSult)