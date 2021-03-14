# -*- coding: utf-8 -*-
import scrapy
import xml.etree.ElementTree as ET
import re


class TheguardianSpider(scrapy.Spider):
    name = 'theguardian'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/world/rss']

    @staticmethod
    def cleanHTML(raw_html):
        reCompare = re.compile('<.*?>|Continue reading...')
        cleanText = re.sub(reCompare, '', raw_html)
        return cleanText

    def parse(self, response):
        string_xml = response.body
        root = ET.fromstring(string_xml)
        newsItems = []

        for item in root.findall('./channel/item'):
            news = {}
            for child in item:

                if child.tag == 'title' or child.tag == 'link' or \
                        child.tag == 'description' or child.tag == 'pubDate':
                    news[child.tag] = TheguardianSpider.cleanHTML(child.text)
                # special checking for author tag
                elif child.tag == '{http://purl.org/dc/elements/1.1/}creator':
                    news['creator'] = child.text
            newsItems.append(news)
        print(newsItems)
