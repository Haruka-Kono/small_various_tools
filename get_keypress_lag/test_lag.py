#import time
import datetime
now = datetime.datetime.now()
print(now)
now_prefix = now.strftime('%Y-%m-%d_%Hh%Mm')
print(now_prefix)
print(now_prefix+'_test')
