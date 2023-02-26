from celery import Celery

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

# celery -A celery_multitask.celery_app worker -l INFO

app = Celery(
    'celery_multitask',
    broker=broker,
    backend=backend,
    # 多任务
    include=[
        'celery_multitask.task01',
        'celery_multitask.task02'
    ]
)

app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False
