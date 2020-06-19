# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re

from  Blockchain.settings import SQL_DATETIME_FORMAT
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


# 把对应的内容，去掉标签、空格、空行
def get_remove_tag(value):
    content = remove_tags(value)
    return re.sub(r'[\t\r\n\s]', '', content)

class BlockchainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 巴比特网站item字段
class EightbtcItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(output_processor=TakeFirst(),)
    content = scrapy.Field(output_processor=Join(''))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
            insert into eightbtc(url,title, publish_time, content) VALUES (%s, %s, %s, %s)
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params

# 金色财经网站字段及处理
class JinseItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(output_processor=TakeFirst(),)
    content = scrapy.Field(output_processor=Join(''))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
           insert into jinse(url , title, publish_time,content) VALUES (%s, %s, %s,%s )
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params

class BitkanItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(output_processor=TakeFirst(),)
    content = scrapy.Field(output_processor=Join(''))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
           insert into bitkan(url , title, publish_time,content) VALUES (%s, %s, %s,%s )
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params

# 比特币之家新闻字段及处理
class Btc798Item(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    publish_time = scrapy.Field(
        input_processor=MapCompose(get_remove_tag),
        output_processor=Join(),)
    content = scrapy.Field(output_processor=Join(''))

    def get_insert_sql(self):
        # 插入表的sql语句
        insert_sql = """
           insert into btc798(url , title, publish_time,content) VALUES (%s, %s, %s,%s )
        """
        params = (
            self["url"],
            self["title"],
            self["publish_time"],
            self["content"],
        )

        return insert_sql, params
