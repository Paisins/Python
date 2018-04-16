#第一个scrapy程序，用来输出Scrapy入门教程(http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)的目录

from scrapy import spiders

class Tutorial(spiders.Spider):
    name = 'tutorial'
    start_urls = ['http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html']

    def parse(self, response):
        titles = response.xpath('//a[@class="reference internal"]/text()').extract()
        for item in titles:
            print (item)
