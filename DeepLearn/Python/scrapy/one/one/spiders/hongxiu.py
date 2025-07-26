import scrapy
from one.items import OneItem

class HongxiuSpider(scrapy.Spider):
    name = "hongxiu"
    allowed_domains = ["www.hongxiu.com"]
    start_urls = ["https://www.hongxiu.com/book/22719285201571504#Catalog"]

    def parse(self, response):
        a_list = response.xpath('//div[@id="j-catalogWrap"]/div[@class="volume-wrap"]/div/ul/li/a')
        for a in a_list:
            url = 'https://www.hongxiu.com' + a.xpath('.//@href').get()
            title = a.xpath('.//text()').get()
            yield scrapy.Request(url=url, callback=self.next_parse, meta={'title': title})

    def next_parse(self, response):
        # 一个章节里面的所有内容，及所有的p元素。
        text_list = response.xpath(
            '//div/div[contains(@class, "read-content")]/div[@class="ywskythunderfont"]/p/text()').getall()
        # 将所有的内容合并到一起。
        text = ''.join(text_list)
        title = response.meta['title']
        print(text)
        print(title)
        book = OneItem(title=title, text=text)
        yield book