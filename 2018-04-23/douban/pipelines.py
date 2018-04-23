# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class DoubanPipeline:

    # 初始化时指定要操作的文件
    def __init__(self):
        self.filename = open('questions.json', 'wb')

    # 存储数据，将 Item 实例作为 json 数据写入到文件中
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(content.encode("utf-8"))
        return item
    # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.filename.close()
