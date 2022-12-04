# * asterisk
# you can pass any number of positional arguments to your function
# Treat *args as a list

def varLengthArg(a,b,*args, **kargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key, value in kargs.items():
        print(key, value)

def main():
    # *args example
    # varLengthArg('a', 'b', 'Hello world',1,2,3)

    #**kargs example
    varLengthArg('a', 2, 'Hello World',1, size='Up size', age=25)

if __name__ == '__main__':
    main()