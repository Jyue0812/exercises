# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    user_name = scrapy.Field()
    user_sen = scrapy.Field()
    user_answer = scrapy.Field()
    image_urls = scrapy.Field()


