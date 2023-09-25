"""
Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores .
The website name can only have letters and digits .
The extension can only contain letters.
The maximum length of the extension is.

Input:
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Output:
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

import re

def check(email)->bool:
    """Create format to validate email."""
    regex = r'\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def filter_mail(emails)->list:
    """To applying filter on list of emails."""
    return list(filter(check, emails))

if __name__ == '__main__':
    """Main program."""
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)