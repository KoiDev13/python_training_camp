def commacode(mylist):
    result=''
    for i in range(len(mylist)):
        if i == int(len(mylist)-1):
            result = result + "and " + mylist[i]
        else:
            result = result + mylist[i] + ", "
    return result

mylist=["red", "big", "tasty"]
print(len(mylist))
kq = commacode(mylist)
print(kq)
