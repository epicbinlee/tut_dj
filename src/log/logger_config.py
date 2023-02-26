import datetime
import logging
import os.path
import sys
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

import pytz


def time_bj(src, what):
    """
    logging time converter
    """
    bj_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    return bj_time.timetuple()


def check_log_dir(_log_path):
    if not os.path.exists(_log_path):
        os.makedirs(_log_path)


# ----------------------------------------------------------------
# 创建一个logger
filename = os.getcwd() + '/logs/tut_cly.log'
logging.Formatter.converter = time_bj
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# ----------------------------------------------------------------
# 1.控制台日志，生产环境需要关闭控制台日志
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
formatter = logging.Formatter("%(asctime)s -%(filename)s -%(lineno)s -%(levelname)s: %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
# ----------------------------------------------------------------
# 2.文件日志
file_handler = logging.FileHandler(filename, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s -%(filename)s -%(lineno)s -%(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# ----------------------------------------------------------------
# 3.设置log日志文件按时间拆分记录，并保存几个历史文件，如果不需要拆分文件记录可忽略
formatter = logging.Formatter("%(asctime)s -%(filename)s -%(lineno)s -%(levelname)s: %(message)s")
# 每1(interval)天(when)重写1个文件,保留7(backupCount)个旧文件；when=Y/m/D/H/M/S
filehandler = TimedRotatingFileHandler(filename, when='D', interval=1, backupCount=7)
# 设置历史文件后缀
filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
# ----------------------------------------------------------------
# 4.设置log日志文件按文件大小拆分记录，并保存几个历史文件，如果不需要拆分文件记录可忽略
formatter = logging.Formatter("%(asctime)s -%(filename)s -%(lineno)s -%(levelname)s: %(message)s")
# 每500M Bytes重写一个文件,保留2(backupCount) 个旧文件
filehandler = RotatingFileHandler(filename, mode='a', maxBytes=1024 * 1024 * 500, backupCount=7)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
