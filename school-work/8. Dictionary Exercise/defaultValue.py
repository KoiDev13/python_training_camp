employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

kq = dict.fromkeys(employees, defaults)
print(kq)