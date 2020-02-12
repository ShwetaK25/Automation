'''
from datetime import datetime, timedelta
from pytz import timezone
import pytz
utc = pytz.utc
print utc.zone

eastern = timezone('US/Eastern')
print eastern.zone

amsterdam = timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
print "fmt", fmt
'''
'''
from datetime import datetime
from pytz import timezone

date_str = "2009-05-05 22:28:15"
datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('Europe/Amsterdam'))
print datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z")
'''
#http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print now_utc.strftime(fmt)

# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
print now_pacific.strftime(fmt)

# Convert to Europe/Berlin time zone
now_berlin = now_pacific.astimezone(timezone('Europe/Berlin'))
print now_berlin.strftime(fmt)
