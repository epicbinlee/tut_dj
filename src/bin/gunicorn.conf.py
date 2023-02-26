import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = '0.0.0.0:8005'
chdir = os.getcwd()
print(chdir)
backlog = 512
timeout = 900
worker_class = 'gevent'
# 并行工作进程数
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4
# 指定每个进程的线程数
threads = 4
# 设置日志记录水平
loglevel = 'info'
# 设置访问日志和错误信息日志路径
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
access_log = os.getcwd() + "/logs/gunicorn_access.log"
print(access_log)
error_log = os.getcwd() + "/logs/gunicorn_error.log"
