import scrapy
import sys


class MiddleDemoSpider(scrapy.Spider):
    name = "middle_demo"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print(response.request.headers)
        print(sys.executable)
