"""
1. Write a Python script to display the - 
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
"""
import datetime

print('current date:')
print(datetime.date.today())
print('current date and time:')
print(datetime.datetime.now())
print('current year:')
print(datetime.date.today().year)
print('current month:')
print(datetime.date.today().month)
print('current month name:')
print(datetime.date.today().strftime('%B'))
print('current week of year:')
print(datetime.date.today().isocalendar()[1])
print('current weekday of the week:')
print(datetime.date.today().isoweekday())    # MON is 1
print('current day of year:')
print(datetime.date.today().strftime('%j'))
print('current day of month:')
print(datetime.date.today().strftime('%d'))
print('current day of week:')
print(datetime.date.today().strftime('%A'))

"""
2. Write a Python program to determine whether a given year is a leap year.
"""
import calendar

print(calendar.isleap(2018))

"""
3. Write a Python program to convert a string to datetime.
Sample String : Jan 1 2014 2:43PM 
Expected Output : 2014-01-01 14:43:00
"""
import datetime

day = 'Jan 1 2014 2:43PM'
print(datetime.datetime.strptime(day, '%b %d %Y %I:%M%p'))

"""
4. Write a Python program to get the current time in Python. 
Sample Format :  13:19:49.078205
"""
import datetime

print(datetime.datetime.today().time())

"""
5. Write a Python program to subtract five days from current date.
Sample Date : 
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17
"""
import datetime

print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(5))

"""
6. Write a Python program to convert unix timestamp string to readable date.
Sample Unix timestamp string : 1284105682
Expected Output : 2010-09-10 13:31:22
"""
import datetime
utimestamp = 1284105682
print(datetime.datetime.fromtimestamp(utimestamp))

"""
7. Write a Python program to print yesterday, today, tomorrow.
"""
import datetime

print(datetime.date.today()-datetime.timedelta(1))
print(datetime.date.today())
print(datetime.date.today()+datetime.timedelta(1))

"""
8. Write a Python program to convert the date to datetime (midnight of the date)
in Python. 
Sample Output : 2015-06-22 00:00:00
"""
import datetime

a_date = datetime.date.today()
print(a_date)

# for printing only format as string:
formatted_date = a_date.__format__('%Y-%m-%d %H:%M:%S')
print(formatted_date)

# if used farther as datetime object:
formatted_date = datetime.datetime.combine(a_date, datetime.time.min)
print(formatted_date)

"""
9. Write a Python program to print next 5 days starting from today.
"""
import datetime

for i in range(6):
    print(datetime.date.today()+datetime.timedelta(i))

"""
10. Write a Python program to add 5 seconds with the current time.
Sample Data :
13:28:32.953088 
13:28:37.953088
"""
import datetime

t = datetime.time(13,28,32)
print(t)
dt = datetime.datetime.combine(datetime.date.today(), t)
dt = dt + datetime.timedelta(seconds=5)
print(dt.time())

"""
11. Write a Python program to convert Year/Month/Day to Day of Year in Python.
"""
import datetime

my_date_str = '2018/04/18'
my_datetime = datetime.datetime.strptime(my_date_str, '%Y/%m/%d')
print(my_datetime)
print(my_datetime.strftime('%j'))

"""
12. Write a Python program to get current time in milliseconds in Python
"""
import time

x = time.localtime()
milisecs = ((x.tm_hour * 60 + x.tm_min)*60 + x.tm_sec)*1000
print(milisecs)

"""
13. Write a Python program to get week number. 
Sample Date : 2015, 6, 16
Expected Output : 25
"""
import datetime

td = datetime.date.today()
print(td.strftime('%W'))

"""
14. Write a Python program to find the date of the first Monday of a given week.
Sample Year and week : 2015, 50
Expected Output : Mon Dec 14 00:00:00 2015
"""
import datetime

week = '50'
year = '2015'
first_mon = '1'
date = datetime.datetime.strptime(year + week + first_mon, '%Y%W%w')
print(date)

"""
15. Write a Python program to select all the Sundays of a specified year.
"""
import datetime

year = '2018'
for week in range(53):
    print(datetime.datetime.strptime(year+str(week)+'0', '%Y%W%w'))
