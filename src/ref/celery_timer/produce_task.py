import time

from celery_task import hi, hello
from datetime import datetime
from datetime import timedelta

# ------------------------------------------------------
# 定时任务调度方式1
# v1 = datetime(2022, 5, 26, 19, 18, 00)
# v2 = datetime.utcfromtimestamp(v1.timestamp())
# result1 = hi.apply_async(args=['hi'], eta=v2)
# print(result1.id)

# ------------------------------------------------------
# 定时任务调度方式2
ct = datetime.now()
utc_ct = datetime.utcfromtimestamp(ct.timestamp())
time_delay = timedelta(seconds=10)
task_time = utc_ct + time_delay
result2 = hello.apply_async(args=['hello'], eta=task_time)
print(result2.id)
