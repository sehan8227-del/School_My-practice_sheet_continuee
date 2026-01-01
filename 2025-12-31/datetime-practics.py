# 1. 날짜 정보 뽑는법
import datetime
import calendar

import datetime
import calendar

import datetime
import calendar

import datetime
import calendar

import datetime
import calendar

now = datetime.datetime.now()
now = datetime.datetime.now()
now = datetime.datetime.now()
now = datetime.datetime.now()
now = datetime.datetime.now()
now = datetime.datetime.now()
now = datetime.datetime.now()
year = now.year 년
year = now.year
year = now.year
year = now.year
month = now.month 월
month = now.month
month = now.month
month = now.month
days = calendar.monthrange(year, month)
days = calendar.monthrange(year, month)
days = calendar.monthrange(year, month)
days = calendar.monthrange(year, month)
print(f"{year}년 {month}월")
print(f"{year}년 {month}월")
print(f"{year}년 {month}월")
print(f"{year}년 {month}월")
print(f"{year}년 {month}월")

for day in range(1,days + 1):
    print(f"{year}월 {day}일 [포차코 자리]")
    
for day in range(1, days + 1):
    print(f"{year}월 {days}일 [포차코 자리]")
for day in range(1, days +1):
    print(f"{year}월 {days}일 [포차코 자리]")
for day in range(1, days + 1):
    print(f"{year}월 {days}일 [포차코 자리]")
for day in range(1, days +1):
    print(f"{year}월 {days}일 [포차코 자리]")
#연습하다 궁금한것 for문을 왜 쓰지?굳이 쓸 이유가 있나?
#print중 f는 뭐지? 뭐길래 자세히 기입안해도 인식되서 들어가는 걸까?





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

for day in range(1, days + 1):
    print(f"{month}월 {day}일 [포차코 자리]")

