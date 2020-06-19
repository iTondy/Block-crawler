# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Blockchain.items import JinseItem
from scrapy_redis.spiders import RedisSpider
from scrapy.loader.processors import TakeFirst, MapCompose, Join
import json

# class JinseSpider(scrapy.Spider):
class JinseSpider(RedisSpider):
    name = 'jinse'
    allowed_domains = ['jinse.com']

    # 起始地址
    # start_urls = ['https://api.jinse.com/v4/information/list/?catelogue_key=www&information_id=22717&limit=3&flag=down&version=9.9.9']
    redis_key = 'jinsespider:start_urls'

    # def parse(self, response):
    #     item = JinseItem()
    #     data = json.loads(response.text)["list"]
    #     # I = ItemLoader(item=JinseItem(),response=response)
    #
    #     for I in data:
    #         item["title"] = I["title"]
    #         item["publish_time"] = I['extra']['published_at']
    #         url_detail = I['extra']["topic_url"]
    #         list_a = response.urljoin(url_detail)
    #         yield scrapy.Request(list_a,meta={'key':item},callback=self.parse_detail)
    #
    # def parse_detail(self,response):
    #     item = response.meta['key']
    #     item["url"] = response.url
    #     item['content'] = response.xpath('//div[@class="js-article"]/p/text()').extract()
    #
    #     yield item

    def parse(self, response):
        data_list = json.loads(response.text)["list"]
        for data in data_list:
            url_detail = data['extra']["topic_url"]
            yield scrapy.Request(url_detail,callback=self.parse_detail)

    def parse_detail(self,response):
        I = ItemLoader(item=JinseItem(),response=response)
        I.add_xpath('title','//div[@class="title"]/h2/text()')
        I.add_xpath('publish_time','//div[@class="time"]/text()')
        I.add_xpath('content','//div[@class="js-article"]/p/text()')
        I.add_value('url',response.url)

        yield I.load_item()