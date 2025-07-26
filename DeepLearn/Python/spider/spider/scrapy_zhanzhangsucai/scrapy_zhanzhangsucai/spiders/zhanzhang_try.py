import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib.request

class ZhanzhangTrySpider(CrawlSpider):
    name = "zhanzhang_try"
    allowed_domains = ["chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/xiaomaotupian.html"]

    rules = (Rule(LinkExtractor(allow=r"xiaomaotupian_\d+\.html"),
                                callback="parse_item",
                                follow=True),)

    def parse(self, response):
        src_list = response.xpath('//div/div[contains(@class, "tupian-list")]/div[contains(@class, "item")]/img/@data-original').extract()
        print(src_list)

