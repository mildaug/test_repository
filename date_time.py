from datetime import datetime
from zoneinfo import ZoneInfo

utc_now = datetime.utcnow().replace(tzinfo=ZoneInfo("UTC"))
vilnius_time = utc_now.astimezone(ZoneInfo("Europe/Vilnius"))
print(vilnius_time)