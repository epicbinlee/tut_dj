import redis

rds = redis.Redis(host='127.0.0.1', port=6379, db=2)
print(rds.keys())

for i in rds.lrange("celery", 0, -1):
    print(i)
