import pyinputplus as pyip

while True:
    promt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(promt)
    if response == 'no':
        break
print('Thank you. Have a nice day.')