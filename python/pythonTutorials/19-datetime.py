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

tday = datetime.date.today()

bday = datetime.date(2016,9,24)

till_bday = tday - bday
print(till_bday)


t = datetime.time(9, 30, 45, 100000)
print(t.hour)

t = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

tdelta = datetime.timedelta(hours=12)

print(t)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

import pytz
dt = datetime.datetime(2016,7,27,12,30,45, tzinfo=pytz.UTC)
print(dt)
dt_noew = datetime.datetime.now(tz = pytz.UTC)
print(dt_noew)


dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)

mtn_tz = pytz.timezone('US/Mountain')

# dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)


print(mtn_tz.__dir__)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt)

# strftime = Datetime to String
# strpttime = String to Datetime