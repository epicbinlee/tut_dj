import redis
from django.http import HttpResponse, Http404
from log.logger_config import logger

from cly_tasks.task1.tasks import hello as heo
from cly_tasks.task2.tasks import hi as ho

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
django.setup()


def hi(request):
    """
    django异步任务
    """
    if request.method == 'GET':
        # 异步任务的调度
        logger.info('调用异步接口开始.')
        r = ho.delay("hi")
        logger.info('异步接口调用结束. {}'.format(r.id))
        # 定时任务的调度
        return HttpResponse('task id: ' + str(r.id))
    else:
        raise Http404


def hello(request):
    """
    django异步任务
    """
    if request.method == 'GET':
        # 异步任务的调度
        logger.info('调用异步接口开始.')
        r = heo.delay("hello")
        logger.info('异步接口调用结束. {}'.format(r.id))
        # 定时任务的调度
        return HttpResponse('task id: ' + str(r.id))
    else:
        raise Http404


def get_hi(request):
    """
    django异步任务结果获取
    """
    if request.method == 'GET':
        rds = redis.Redis(host='127.0.0.1', port=6379, db=2)
        res = []
        for k in rds.keys():
            v = rds.get(k)
            s = str(k, 'utf-8') + "\t" + str(v, 'utf-8')
            res.append(s)
        logger.info("获取全量结果数据: {}".format(len(res)))
        return HttpResponse('\n'.join(res))
    else:
        raise Http404
