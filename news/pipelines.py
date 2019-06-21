# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class NewsPipeline(object):
    def __init__(self):
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient('127.0.0.1', 27017)
        # 连接所需数据库,ScrapyChina为数据库名
        db = client['ScrapyChina']
        # 连接所用集合，也就是我们通常所说的表，mingyan为表名
        self.post = db['mingyan']

    def process_item(self, item, spider):

        title = item['title']
        if title:
            title_str = ''.join(title)
            item['title'] = title_str.replace('\n', '')

        time = item['time']
        if time:
            item['time'] = time.replace('\n', '')

        category = item['category']
        if category:
            item['category'] = category.replace('\n', '')

        tags = item['tags']
        if tags:
            tags_str = ','.join(tags)
            item['tags'] = tags_str.replace('\n', '')

        content = item['content']
        if content:
            content_str = ''.join(content)
            item['content'] = content_str.replace('\n', '')

        postItem = dict(item)  # 把item转化成字典形式
        self.post.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写
