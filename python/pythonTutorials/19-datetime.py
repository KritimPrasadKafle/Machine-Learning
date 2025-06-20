import datetime
d = datetime.date(2016,7,24)
print(d)

tday = datetime.date.today()
print(tday.day)

print(tday.isoweekday())

print(tday.weekday())

tdelta = datetime.timedelta(days = 7)
print(tday + tdelta)
print(tday - tdelta)

