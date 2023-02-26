import time

from ref.celery_multidir_timer.task01 import hello
from ref.celery_multidir_timer.task02 import hi
from ref.celery_multidir_timer.celery_app import app
from celery.result import AsyncResult

# ------------------------------------------------------
hi_res = hi.delay('hi')
print(hi_res.id)

hello_res = hello.delay('hello')
print(hello_res.id)

# ------------------------------------------------------
# 获取结果
async_result = AsyncResult(id=hi_res.id, app=app)

# 同步获取结果
while async_result.state != 'SUCCESS':
    print('任务处理中...')
    time.sleep(10)

# 获取结果
if async_result.successful():
    result = async_result.get()
    print(result)

# ------------------------------------------------------
# 删除结果
# async_result.forget()
# async_result.revoke(terminate=True, timeout=80)
