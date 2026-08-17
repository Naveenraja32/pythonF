from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

timeZone = ZoneInfo('Asia/Kolkata')
now = datetime.now(tz=timeZone)

# Parses the string to a naive datetime, then applies the timezone
dateB = datetime.strptime('03-08-2026', '%d-%m-%Y').replace(tzinfo=timeZone)

# This will print the days/hours passed since August 3rd
print(now - dateB)

# Fixed the extra parenthesis error here
print(datetime.strftime(now + timedelta(days=1), '%d-%m-%Y'))
