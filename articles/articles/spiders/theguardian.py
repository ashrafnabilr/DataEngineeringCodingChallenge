# -*- coding: utf-8 -*-
import scrapy
import xml.etree.ElementTree as ET
import re
import os
import pymongo


# Please make sure before using this class that both 'mongodb_user' and
# 'mongodb_password' are defined in the system environment variables
# based on the user mongodb atlas user name and password
class TheguardianSpider(scrapy.Spider):
    name = 'theguardian'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/world/rss']
    CONNECTION_STRING = "mongodb+srv://" + os.environ.get('mongodb_user') + ":" + os.environ.get(
        'mongodb_password') + "@cluster0.6sidv.mongodb.net/articles?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)

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

        db = self.client['articles']
        col = db['data']
        col.delete_many({})
        col.insert_many(newsItems)
