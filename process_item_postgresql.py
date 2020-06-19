# -*- coding: utf-8 -*-

import psycopg2
import redis
import json

def process_item(spidername=None):
    Redis_conn=redis.StrictRedis(host='127.0.0.1',password='369369',port=6379,db=0)
    Postgresql_conn=psycopg2.connect(host='127.0.0.1',user='ericliu',password='369369',port=5432,database='blockchain')

    offset=1

    while True:
        try:
            source,data=Redis_conn.blpop("{}:items".format(spidername))
            data=json.loads(data.decode("utf8"))
            # data=json.loads(data)

            cur=Postgresql_conn.cursor()
            sql=("insert into blockchain_item(url,title,publish_time,content) VALUES (%s,%s,%s,%s)")
            lis = (data['url'], data['title'], data['publish_time'], data['content'])

            cur.execute(sql,lis)
            Postgresql_conn.commit()
            cur.close()

            offset += 1
            print(spidername,offset)

        except:
            pass


if __name__=="__main__":

    process_item(spidername='eightbtc')
    process_item(spidername='jinse')
    process_item(spidername='jinse')

