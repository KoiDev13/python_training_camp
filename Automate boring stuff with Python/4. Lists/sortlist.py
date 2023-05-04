'''
Sort by element
list = ['Khoi','Nguyen','Pul']
sort_by_second = sorted(list, key=lambda el:el[1])
print(sort_by_second)
'''

import json

list_customer = [
    {
        'name': 'Khoi',
        'age' : 29
    },
    {
        'name': 'Nguyen',
        'age' : 27
    },
    {
        'name': 'Nguyen',
        'age' : 25
    },
]


sort_by_key = sorted(list_customer, key=lambda el:el['age'])
print(json.dumps(sort_by_key, indent=4))
