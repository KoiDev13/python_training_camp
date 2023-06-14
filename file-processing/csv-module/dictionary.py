import csv

file_name = 'testdata.csv'

with open(file_name, 'r+',newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writerows(
        [
            {
                'id': 22,
                'first_name':'Khoi',
                'last_name':'Nguyen',
                'email':'khoi@gmail.com',
                'gender':'Male',
                'ip_address':'1.1.1.1'
            },
            {
                'id': 23,
                'first_name':'Khoi',
                'last_name':'Nguyen',
                'email':'khoi@gmail.com',
                'gender':'Male',
                'ip_address':'1.1.1.1'
            }
        ]
    )