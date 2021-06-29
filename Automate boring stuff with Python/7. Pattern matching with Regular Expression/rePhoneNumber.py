import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print('Phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))