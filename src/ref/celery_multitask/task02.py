from ref.celery_multitask.celery_app import app
import time


@app.task
def hi(s):
    print("start")
    time.sleep(60)
    print(s)
    print("end")
    return 'hi'
