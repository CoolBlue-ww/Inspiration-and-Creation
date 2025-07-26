import scrapy


class Baidu32Spider(scrapy.Spider):
    name = "baidu_32"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print('苍茫的天涯是我的爱！')
        pass
