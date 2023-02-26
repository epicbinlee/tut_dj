import time

from celery_task import hi, hello
from celery.result import AsyncResult
from celery_task import app

hi_res = hi.delay('hi')
print(hi_res.id)

hello_res = hello.delay('hello')
print(hello_res.id)

async_result = AsyncResult(id=hi_res.id, app=app)
while async_result.state != 'SUCCESS':
    print('任务处理中...')
    time.sleep(10)
if async_result.successful():
    result = async_result.get()
    print(result)
