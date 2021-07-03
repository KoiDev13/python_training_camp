from pathlib import Path
import os
# Path.cwd()
# Path('C:\\Users\\khoi.nguyena\\Desktop\\test_folder').mkdir()
# os.makedirs('C:\\Users\\khoi.nguyena\\test_folder')
p = Path('C:\\Users\\khoi.nguyena\\Desktop\\test_folder\\hello.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.suffixes)
print(p.suffix)