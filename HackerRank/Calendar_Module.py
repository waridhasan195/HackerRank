
# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

# print(calendar.weekday(2015, 5, 8))


import calendar
month, day, year = input().split()

weekday = calendar.weekday(int(year), int(month), int(day))
print(weekday)

print((calendar.day_name[weekday]).upper())
