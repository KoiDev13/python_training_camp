import csv

states = [{"city":"Jati","latitude":-6.8300602},
{"city":"Castêlo","latitude":41.3336366},
{"city":"Saldanha","latitude":-33.0276981},
{"city":"Vellinge","latitude":55.4738346},
{"city":"Fenggao","latitude":29.421736},
{"city":"Magburaka","latitude":8.7178672},
{"city":"Zaragoza","latitude":28.4943597},
{"city":"Ebene","latitude":-20.2418916},
{"city":"Telukpakedai","latitude":-0.3052095},
{"city":"Santa Catalina Norte","latitude":13.9311113},
{"city":"Gaopai","latitude":25.487867},
{"city":"Guanshui","latitude":37.215613},
{"city":"Hongyan","latitude":29.036141},
{"city":"Suva Reka","latitude":42.362461},
{"city":"Singida","latitude":-6.7453352},
{"city":"Lawrenceville","latitude":40.4770427},
{"city":"Cran-Gevrier","latitude":45.9075},
{"city":"Paledang","latitude":-6.6000226},
{"city":"Hostouň","latitude":49.5597209},
{"city":"Klimavichy","latitude":53.6091856}]

file_name = 'states.csv'

with open(file_name, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['city','latitude'])
    writer.writeheader()
    writer.writerows(states)