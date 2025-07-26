import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib.request


class TupianSpider(CrawlSpider):
    name = "tupian_"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/shuiziyuantupian.html"]

    rules = (Rule(LinkExtractor(allow=r"https://sc.chinaz.com/tupian/shuiziyuantupian_\d+\.html"), callback="parse_item",
                  follow=True),)

    def parse_item(self, response):
        img_src_list = response.xpath(
            '//div/div[contains(@class, "tupian-list")]/div[contains(@class, "item")]/img/@data-original').getall()
        img_name_list = response.xpath(
            '//div/div[contains(@class, "tupian-list")]/div[contains(@class, "item")]/img/@alt').getall()
        for i in range(len(img_src_list)):
            img_url1 = 'https:' + img_src_list[i]
            if '_s.jpg' in img_url1:
                img_url = img_url1[0:-6:1] + '.jpg'
            else:
                img_url = img_url1[0:-6:1] + '.png'
            img_name = img_name_list[i]
            urllib.request.urlretrieve(url=img_url, filename='./shuiziyuan/' + img_name + '.jpg')
            print(f'{img_name}下载成功！')

