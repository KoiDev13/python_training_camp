# array = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174 ]
# output = 169.375
# my_set = set(array)
# print(sum(my_set)/ len(my_set)) 

def average(array):
    solution = 0 
    my_set = set(array)
    return sum(my_set)/ len(my_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)