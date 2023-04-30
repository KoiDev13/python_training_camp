s = '12:05:45PM'

if 'AM' and '12' in s:
    h = '00'
    m = s[3:(len(s)-2)]
    ns = h+":"+m
if 'PM' and '12' in s:
    h = '12'
    m = s[3:(len(s)-2)]
    ns = h+":"+m
if 'AM' in s and '12' not in s:
    ns = s[:(len(s)-2)]
if 'PM' in s and '12' not in s:
    h = str(int(s[:2]) + 12)
    m = s[3:(len(s)-2)]
    ns = h+":"+m
print(ns)