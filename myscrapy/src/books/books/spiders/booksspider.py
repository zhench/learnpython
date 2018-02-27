# -*- coding: utf-8 -*-
import scrapy


class BooksspiderSpider(scrapy.Spider):
    name = 'booksspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
           # name=book.xpath("./h3/a/text()").extract()[0]
           # print(name)
           # name=book.xpath("./h3/a")
           # info=name[0].xpath('string(.)').extract()[0]
           # print(info)
            name=book.xpath('./h3/a/@title').extract()[0]
            price=book.css('p.price_color::text').extract()[0]
            yield{
                'name':name,
                'price':price,
            }
            next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
            print(response.css('ul.pager li.next a::attr(href)'))
            if next_url:
                next_url=response.urljoin(next_url)
                yield scrapy.Request(next_url,callback=self.parse)