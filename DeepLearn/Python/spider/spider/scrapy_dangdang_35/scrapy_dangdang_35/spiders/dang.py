import scrapy
from scrapy_dangdang_35.items import ScrapyDangdang35Item


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.21.01.00.00.00.html"]
    base_url = "https://category.dangdang.com/pg"
    page = 1
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, meta={'selenium': True}, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//div[@id="search_nature_rg"]/ul/li')
        # selector可以再次使用xpath
        for li in li_list:
            name = li.xpath('.//a/img/@alt').extract_first()
            src = li.xpath('.//a/img/@src').extract_first()
            price = li.xpath('.//p[3]/span[1]/text()').extract_first()
            text = li.xpath('.//p[2]/text()').extract_first()
            # print(name, price, text, src)

            book = ScrapyDangdang35Item(name=name, price=price, text=text, src=src)

            # yield返回一个return对象（一个book），交给pipelines。
            yield book

        if self.page < 100:
            self.page += 1
            url = self.base_url + str(self.page) + "-cp01.21.01.00.00.00.html"
            yield scrapy.Request(url, callback=self.parse)