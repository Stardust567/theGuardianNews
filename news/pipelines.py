# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):
    def process_item(self, item, spider):

        title = item['title']
        if title:
            title_str = ''.join(title)
            item['title'] = title_str.replace('\n', '')

        time = item['time']
        if time:
            item['time'] = time.replace('\n', '')

        tags = item['tags']
        if tags:
            tags_str = ','.join(tags)
            item['tags'] = tags_str.replace('\n', '')

        content = item['content']
        if content:
            content_str = ''.join(content)
            item['content'] = content_str.replace('\n', '')

        return item
