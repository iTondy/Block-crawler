# -*- coding: utf-8 -*-

import MySQLdb
import redis
import json

def process_item():
    Redis_conn=redis.StrictRedis(host='127.0.0.1',password='369369',port=6379,db=0)
    MySql_conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='12345678',port=3306,db='Blockchain',charset='utf8')
    offset = 1
    while True:
        try:
            source,data=Redis_conn.blpop("eightbtc:items")
            data=json.loads(data.decode("utf8"))
            cur=MySql_conn.cursor()
            sql=("insert into eightbtc(url,title,publish_time,content)"
                 "VALUES (%s,%s,%s,%s)")
            lis = (data['url'], data['title'], data['publish_time'], data['content'])
            cur.execute(sql,lis)
            MySql_conn.commit()
            cur.close()

            offset +=1
            print offset
        except:
            pass


if __name__=="__main__":
    process_item()