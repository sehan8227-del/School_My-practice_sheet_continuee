import datetime
import calendar

import datetime
import calendar

now = datetime.datetime.now()
year = now.year
month = now.month
month = now.month

days = calendar.monthrange(year, month)

print(f"{year}년 {month}월")

now = datetime.datetime.now()
year = now.year
month = now.month

days = calendar.monthrange(year, month)[1]

print(f"{year}년 {month}월")
