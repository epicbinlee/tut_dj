from cly_tasks.celery import app
from log.logger_config import logger
import time


@app.task(bind=True, serializer='json')
def hi(s):
    logger.info("调用celery任务开始. 参数为: {}".format(s))
    time.sleep(2)
    logger.info("调用celery任务结束.")
    return 'hi-this is celery app.'
