import json

thisdict = {
    'name': 'Khoi',
    'age' : 29
}

'''
if  "brand" in thisdict:
    print(thisdict["brand"])
else:
    print("No key found")
'''
thisdict['email'] = 'khoinguyen@gmail.com'

print(json.dumps(thisdict, indent=4))