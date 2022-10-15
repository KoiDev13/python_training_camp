from dateutil.parser import parse

date_string = "Feb 25 2020 4:20PM"
x = parse(date_string)
print(x)