# Complete the function below

# define a function
def fizzbuzz(n):
    result = []
    for i in range(1,n+1):
        if i%3 == 0:
            result.append('Fizz') 
        elif i%5 == 0:
            result.append('Buzz') 
        else:
            result.append(str(i))
    return result
    
# call the function
number = int(input())
output = fizzbuzz(number)
print(output)