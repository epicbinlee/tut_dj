import logging
import os
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from celery import Celery, platforms
from celery.signals import after_setup_logger
from dj import settings
# platforms.C_FORCE_ROOT = True

app = Celery('cly_tasks')

# 把celery和django进行组合，识别和加载django的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj.settings')

# 通过app对象加载配置
app.config_from_object("django.conf:settings", namespace='CELERY')

# 加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
app.autodiscover_tasks(["cly_tasks.task1", "cly_tasks.task2"])

# 启动Celery的命令
# redis-server
# pip3 install celery==5.0.0
# celery -A dj_celery.celery_app worker -l INFO
# 屏蔽上述日志，broker在Redis, 日志通过nohup方式获取
