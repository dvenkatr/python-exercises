import time
from datetime import datetime, timezone

# def add(moment):    
#     moment = datetime(2015, 1, 24, 22, 0, tzinfo = timezone.utc)
#     print(moment)
#     s = moment.timestamp() + 10**9
#     print(datetime.fromtimestamp(s, tz = timezone.utc))
#     return (datetime.fromtimestamp(s, tz = timezone.utc))

#     print(datetime.fromtimestamp(s))
#     return (datetime.fromtimestamp(s))

# a = datetime(2011, 4, 25, 0, 0)
# b = datetime(1977, 6, 13, 0, 0)
# c = datetime(1959, 7, 19, 0, 0)

# add(a)
# add(b)
# add(c)

from datetime import datetime, timedelta

def add(moment):
    giga_s=1000000000
    add_gs=timedelta(0, giga_s)
    return moment+add_gs