import celery
from datetime import timedelta
from celery.schedules import crontab

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

# 消费者
# [root@tps209 src]# celery -A celery_multidir_timer.celery_app worker -l INFO -c 10
# 生产者（不关闭会累积）
# [root@tps209 src]# celery -A celery_multidir_timer.celery_app beat

app = celery.Celery(
    'celery_multidir_timer',
    broker=broker,
    backend=backend,
    # 多任务
    include=[
        'celery_multidir_timer.task01',
        'celery_multidir_timer.task02',
    ]
)

app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False

app.conf.beat_schedule = {
    'add-every-n-second': {
        'task': 'celery_multidir_timer.task01.hello',
        # 定时
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=1),
        'args': ('hello',)
    }
}
