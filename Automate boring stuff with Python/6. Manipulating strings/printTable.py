tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

col_widths = []
for i, record in enumerate(tableData):
    col_widths.insert(i, max(len(item) for item in record))

for i in range(len(tableData[0])):
    print(' '.join(record[i].rjust(col_widths[j]) for j, record in enumerate(tableData)))