import scrapy
import urllib.request


class TupianSpider(scrapy.Spider):
    name = "tupian"
    start_urls = ['https://sc.chinaz.com/tupian/madetupian_7.html']
    base_url = 'https://sc.chinaz.com/tupian/madetupian_'
    page = 7

    def parse(self, response):
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
            urllib.request.urlretrieve(url=img_url, filename='./ma/' + img_name + '.jpg')
            print(f'{img_name}下载成功！')

        if self.page <= 9:
            self.page += 1
            url = self.base_url + str(self.page) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)
