import time

from celery import shared_task
from log.logger_config import logger

import sys

sys.path.append('../../log')


# @app.task
@shared_task
def hello(s):
    logger.info("调用cly任务开始. 参数为: {}".format(s))
    time.sleep(2)
    # x = 1 / 0
    logger.info("调用cly任务结束.")
    return 'hello'
