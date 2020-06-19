# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy_redis.spiders import RedisCrawlSpider
from Blockchain.items import Btc798Item

# class Btc798Spider(CrawlSpider):
class Btc798Spider(RedisCrawlSpider):

    name = 'btc798'
    allowed_domains = ['btc798.com']
    # start_urls = ['http://www.btc798.com/cate/4.html']
    redis_key = 'btc798spider:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'btc798.com/home/cate/index/id/4/m/Home/p/\d+.html')),
        Rule(LinkExtractor(allow=r'articles/\d+'),callback='parse_item'),
    )

    def parse_item(self, response):
        I = ItemLoader(item=Btc798Item(),response=response)
        I.add_xpath('title','//div[@class="article__heading__title"]/text()')
        I.add_xpath('publish_time','//span[@class="meta-item__text"]/text()')
        I.add_xpath('content','//div[@class="node-article-content"]/p/span/text() | //div[@class="node-article-content"]/p/text()')
        I.add_value('url',response.url)

        yield I.load_item()
