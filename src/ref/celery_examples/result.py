from celery.result import AsyncResult
from celery_task import app

async_result = AsyncResult(id='286d13e2-5b69-4734-84f0-66913d51f308', app=app)
print(async_result.state)
if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.state == 'SUCCESS':
    print("任务执行成功.")
