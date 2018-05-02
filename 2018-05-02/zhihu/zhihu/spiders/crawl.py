# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem

class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['zhihu.com']
    start_urls = ["https://www.zhihu.com/question/36011809"]

    def parse(self, response):
        zh = ZhihuItem()

        answers = response.xpath(r'//div[@class="List-item"]')
        for answer in answers:
            zh['user_name'] = answer.xpath(r'.//a[@class="UserLink-link"]/text()').extract()
            zh['user_sen'] = answer.xpath(r'.//div[@class="RichText AuthorInfo-badgeText"]/text()').extract()

            user_answer = answer.xpath(
                r'.//div[@class ="RichContent RichContent--unescapable"]/div[1]/span/text()').extract()
            if len(user_answer) != 0:
                zh['user_answer'] = user_answer
            else:
                zh['user_answer'] = answer.xpath(
                    r'.//div[@class="RichContent RichContent--unescapable"]/div[1]/span/p/text()').extract()

            zh['photos'] = answer.xpath(r'.//img/@data-original').extract()

            yield zh


