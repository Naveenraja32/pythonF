from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

timeZone = ZoneInfo('Asia/Kolkata')
now = datetime.now(tz=timeZone)

# Parses the string to a naive datetime, then applies the timezone
dateB = datetime.strptime('03-08-2026', '%d-%m-%Y').replace(tzinfo=timeZone)

print(datetime.combine(now, time=time(8,59,50)))

# This will print the days/hours passed since August 3rd
print(now - dateB)

# Fixed the extra parenthesis error here
print(datetime.strftime(now + timedelta(days=1), '%d-%m-%Y'))

# now = datetime.now().date()
# try:
#     print(datetime.combine(now, time=time(8,59,50)))
# except Exception as e:
#     print(type(e).__name__, ":", e)
print(datetime.strftime(now, '%H:%M'))

str='12-12-1947'
print(datetime.strptime(str, '%d-%m-%Y').date())