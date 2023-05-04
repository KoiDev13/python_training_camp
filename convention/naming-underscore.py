"""
Underscore(_) can be used to name variables, functions and classes, etc..,

Single Pre Underscore:- _variable   bien project thanh private
Signle Post Underscore:- variable   use Python keyword as a variable
Double Pre Underscores:- __variable Mangling name: - trình thông dịch của Python thay đổi
                                                    tên biến theo cách khó 
                                                    xung đột khi lớp được kế thừa.
Double Pre and Post Underscores:- __variable__
"""


class SimpleClass:

    def __init__(self):
        self.__datacamp = "Excellent"

    def get_datacamp(self):
        return self.__datacamp

obj = SimpleClass()
print(obj.get_datacamp()) ## it prints the "Excellent" which is a __var
# print(obj.__datacamp)     ## here, we get an error as mentioned before. It changes the name of the variable
