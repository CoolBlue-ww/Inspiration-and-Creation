import scrapy
import urllib.request
from xiaomao.items import XiaomaoItem

class XxSpider(scrapy.Spider):
    name = "xx"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/xiaomaotupian.html"]
    page = 1
    base_url = 'https://sc.chinaz.com/tupian/xiaomaotupian_'

    def parse(self, response):
        src_list = response.xpath(
            '//div/div[contains(@class, "tupian-list")]/div[contains(@class, "item")]/img/@data-original').extract()
        name_list = response.xpath(
            '//div/div[contains(@class, "tupian-list")]/div[contains(@class, "item")]/img/@alt').extract()

        items = XiaomaoItem(src_list=src_list, name_list=name_list)
        yield items

        if self.page <= 25:
            self.page += 1
            next_url = self.base_url + str(self.page) + '.html'
            yield scrapy.Request(url=next_url, callback=self.parse)
