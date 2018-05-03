# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem
from selenium import webdriver
import time
from lxml import etree

class CrawlSpider(scrapy.Spider):
    name = 'zhihucrawl'
    allowed_domains = ['zhihu.com']
    start_urls = ["https://www.zhihu.com/question/36011809",]

    def parse(self, response):
        zh = ZhihuItem()

        chromedriver = r"d://chromedriver.exe"
        driver = webdriver.Chrome(chromedriver)
        driver.get(self.start_urls[0])

        page_height = 10000
        while page_height <= 489744:
            driver.execute_script("window.scrollTo(0," + str(page_height) + ")")
            page_height += 10000
            time.sleep(3)

        time.sleep(10)

        response = etree.HTML(driver.page_source)

        answers = response.xpath(r'//div[@class="List-item"]')
        for answer in answers:
            zh['user_name'] = answer.xpath(r'.//a[@class="UserLink-link"]/text()')
            zh['user_sen'] = answer.xpath(r'.//div[@class="RichText AuthorInfo-badgeText"]/text()')

            user_answer = answer.xpath(
                r'.//div[@class ="RichContent RichContent--unescapable"]/div[1]/span/text()')
            if len(user_answer) != 0:
                zh['user_answer'] = user_answer
            else:
                zh['user_answer'] = answer.xpath(
                    r'.//div[@class="RichContent RichContent--unescapable"]/div[1]/span/p/text()')

            zh['photos'] = answer.xpath(r'.//img/@data-original')

            yield zh

