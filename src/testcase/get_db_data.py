import pickle

from sqlalchemy import create_engine

eng = create_engine(url='postgresql://postgres:hik123@10.3.72.118:5432/qhb_try')
conn = eng.connect()
qry = 'select * from celery_taskmeta'
cursor = conn.execute(qry)
res = cursor.fetchall()
for x in res:
    print(x)
    print(pickle.loads(x[3]))
