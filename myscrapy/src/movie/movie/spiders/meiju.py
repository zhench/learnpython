# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meiju.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        print('start crawl')
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        #movies= response.xpath('//ul[@class="top-list  fn-clear"]/li')
        print(len(movies))
        for each_movie in movies:
            item=MovieItem()
            item['name']=each_movie.xpath('./h5/a/@title').extract()[0]
            yield item