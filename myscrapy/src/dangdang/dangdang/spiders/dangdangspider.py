# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy import Selector
from lxml import etree
from dangdang.items import DangdangItem
from scrapy_redis.spiders import RedisSpider

class DangdangspiderSpider(RedisSpider):
    name = 'dangdangspider'
    redis_key='dangdangspider:urls'
    allowed_domains = ['dangdang.com']
    start_urls = 'http://category.dangdang.com/cp01.00.00.00.00.00.html'

    def start_requests(self):
        user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \ Safari/537.36 SE 2.X MetaSr 1.0"
        headers={'User-Agent':user_agent}
        print('start to request')
        yield scrapy.Request(url=self.start_urls,headers=headers,method="GET",callback=self.parse)

    def parse(self, response):
        user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \ Safari/537.36 SE 2.X MetaSr 1.0"
        headers={'User-Agent':user_agent}
        lists=response.body.decode('gbk')
        print(lists)
        print(type(lists))
        selector=etree.HTML(lists)
        goodslist=selector.xpath()
