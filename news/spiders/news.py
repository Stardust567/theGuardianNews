# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from news.items import NewsItem

class HeadSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['theguardian.com']
    base_url = 'https://www.theguardian.com/'
    start_urls = []
    topics = ['world', 'science', 'cities', 'global-development',
              'uk/sport', 'uk/technology', 'uk/business', 'uk/environment', 'uk/culture']
    years = [2019]
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    months = ['jun']
    dates = range(18, 20)

    for topic in topics:
        for y in years:
            for m in months:
                for d in dates:
                    url = base_url + topic + '/' + str(y) + '/' + m + '/' + '%02d' % d + '/' + 'all'
                    start_urls.append(url) # 类似于 https://www.theguardian.com/uk/sport/2019/apr/01/all


    def parse(self, response):
        urls = response.css('a[class="fc-item__link"]').css('a[data-link-name="article"]').xpath('@href').extract()
        for url in urls: # 每个https://www.theguardian.com/uk/sport/2019/apr/01/all页面上的news连接
            yield Request(url, self.get_news)

    def get_news(self, response):
        item = NewsItem()

        title = response.css('h1[class ="content__headline "]').css('h1[itemprop="headline"]::text').extract()
        if(len(title)==0): # 卫报的news页面有两种形式，如果第一种没抓到，就用模式二
            title = response.css('meta[itemprop="description"]').xpath('@content').extract()

        time = response.css('time[itemprop = "datePublished"]::text').extract_first()

        category = response.css('a[class ="subnav-link subnav-link--current-section"]::text').extract_first()

        tags = response.css('a[class = "submeta__link"]::text').extract()

        content = response.css('div[itemprop = "articleBody"]').css('p::text').extract()
        if (len(content) == 0):
            content = title # 有些news内容可能时视频或者其它非文本模式，这时我们用title作为content

        item['title'] = title
        item['time'] = time
        item['category'] = category
        item['tags'] = tags
        item['content'] = content

        yield item
