# Required parameters and default parameters
def print_name(name, greetings='Hello cac ban'):
    print(f'{name}, {greetings}')

def func1(a,b,c):
    print(a,b,c)

def main():
    # print_name('Khoi','Bye cac ban')
    # Positional aruguments
    func1(3,2,1)

    # Keyword arguments
    func1(a='Hello world', c='this is c', b=2)

if __name__ == '__main__':
    main()