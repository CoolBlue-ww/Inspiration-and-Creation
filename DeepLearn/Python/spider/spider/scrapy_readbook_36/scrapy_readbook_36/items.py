# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyReadbook36Item(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    src = scrapy.Field()
