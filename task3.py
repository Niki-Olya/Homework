#help('calendar')
import calendar
print(calendar.__file__)
print (dir(calendar))
print(calendar.isleap(2027))
print(calendar.weekday(1995,6,25))
print(calendar.day_name[calendar.weekday(1995,6,25)])
print(calendar.prcal(2023))
