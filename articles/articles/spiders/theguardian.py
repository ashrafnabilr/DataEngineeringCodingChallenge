# -*- coding: utf-8 -*-
import scrapy


class TheguardianSpider(scrapy.Spider):
    name = 'theguardian'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/world/rss']

    def parse(self, response):
        print(response.body)
