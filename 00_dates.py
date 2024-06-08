### Dates ###
import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
# print(now.date)
print(now.hour)
print(now.minute)
print(now.second)

print('=================================')

time_stamp = now.timestamp()

print(time_stamp)

date = now.date()

print(date)

print('=================================')

year_2024 = datetime.datetime(2024, 6, 15)

def print_date(date):
  print(date.year)
  print(date.month)
  print(date.day)
  print(date.hour)
  print(date.minute)
  print(date.second)
  print(date.timestamp())

print_date(year_2024)

print('=================================')

current_time = datetime.time(21, 21, 15)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print('=================================')

current_date = datetime.date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

print('=================================')

current_date = datetime.date(2024, 5, 18)

print(current_date.year)
print(current_date.month)
print(current_date.day)

print('=================================')

current_date = datetime.date(current_date.year, current_date.month, current_date.day)

print(current_date.month)

current_date = datetime.date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

print('=================================')

diff = year_2024 - now

print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

print('=================================')
