# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang35Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义数据结构，需要下载的内容。
    name = scrapy.Field()
    src = scrapy.Field()
    price = scrapy.Field()
    text = scrapy.Field()

