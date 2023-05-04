import csv

file_name = 'testdata.csv'
sniffer = csv.Sniffer()

with open(file_name, 'r+', newline='') as f:
    snippet = f.read(2048)
    f.seek(0)

    dialect = sniffer.sniff(snippet)
    dialect.lineterminator='\n'

    print(f"Dialect: {dialect.__dict__}")

    reader = csv.reader(f, dialect)
    if sniffer.has_header(snippet):
        header_row = next(reader)

    for row in reader:
        last_id = int(row[0])
        print(row)

    writer = csv.writer(f, dialect)

    writer.writerows(
        [
        [last_id+1,'KhoiNguyen','khoinguyen@blogger.com','Male','194.31.131.72'],
        ]
    )