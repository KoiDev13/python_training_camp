"""
Exercise 9: Check file is empty or not
Write a program to check if the given file is empty or not
"""

import os

fs = os.stat('read_sample.txt').st_size

if fs==0:
    print('File is empty!')
else:
    print('File is not empty!')