from datetime import datetime, timedelta
from time import time
given_date = datetime(2020, 2, 25)
before_date = given_date - timedelta(7)
print(str(given_date) + ' --> ' + str(before_date))