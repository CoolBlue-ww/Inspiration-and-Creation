# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    money = scrapy.Field()
    place = scrapy.Field()
    ask = scrapy.Field()
    hr = scrapy.Field()
    page_url = scrapy.Field()
