s = '132 456 Wq  m e'
s_list = list(s)
print(s_list)
words = s.split()
my_list = []

for word in words:
    my_list.append(word.capitalize())

name = ' '.join(my_list)
# print(name)
