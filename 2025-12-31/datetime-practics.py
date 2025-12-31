# 1. 날짜 정보 뽑는법
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

# 2.날짜 옆에 빈자리를 넣는다.
for day in range(1, days + 1):
    print(f"{month}월 {day}일  [포차코 자리]")
