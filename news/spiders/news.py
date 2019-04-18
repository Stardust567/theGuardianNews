# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from news.items import NewsItem

class HeadSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/world/2019/apr/14/all']

    def parse(self, response):

        urls = response.css('a[class="fc-item__link"]').css('a[data-link-name="article"]').xpath('@href').extract()
        for url in urls:
            yield Request(url, callback=self.get_news)

    def get_news(self, response):
        item = NewsItem()
        title = response.css('h1[class ="content__headline "]').css('h1[itemprop="headline"]::text').extract()
        if(len(title)==0):
            title = ['hello', ', world']
            title = response.css('meta[itemprop="description"]').xpath('@content').extract()

        time = response.css('time[itemprop = "datePublished"]::text').extract_first()
        category = response.css('a[class ="subnav-link subnav-link--current-section"]::text').extract_first()
        tags = response.css('a[class = "submeta__link"]::text').extract()
        content = response.css('div[itemprop = "articleBody"]').css('p::text').extract()

        item['title'] = title
        item['time'] = time
        item['category'] = category
        item['tags'] = tags
        item['content'] = content
        yield item
