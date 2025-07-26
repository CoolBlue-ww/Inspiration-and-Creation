import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_36.items import ScrapyReadbook36Item

class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1107_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1107_\d+\.html"),
                                callback="parse_item",
                                follow=True),)

    def parse_item(self, response):
        li_list = response.xpath('//div/div[@class="bookslist"]/ul/li')
        for li in li_list:
            name = li.xpath('.//div/h3/a/text()').extract_first()
            author = li.xpath('.//div/p[1]/text()').extract_first()
            text = li.xpath('.//div/p[2]/text()').extract_first()
            src = li.xpath('.//div/div/a/img/@data-original').extract_first()
            books = ScrapyReadbook36Item(name=name, author=author, text=text, src=src)
            yield books
