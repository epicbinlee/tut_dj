import time

import celery

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

# [root@tps209 src]# celery -A celery_examples.celery_task worker -l INFO

app = celery.Celery('hello', broker=broker, backend=backend)


@app.task
def hello(s):
    print("start")
    time.sleep(60)
    print(s)
    print("end")
    return 'hello'


@app.task
def hi(s):
    print("start")
    time.sleep(60)
    print(s)
    print("end")
    return 'hi'
