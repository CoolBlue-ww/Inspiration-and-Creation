# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OneItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
