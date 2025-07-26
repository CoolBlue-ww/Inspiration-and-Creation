import scrapy


class QichezhijiaSpider(scrapy.Spider):
    name = "qichezhijia"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price/brandid_51?pvareaid=104399"]

    def parse(self, response):
        # print('=========================你好啊？')
        list = response.xpath('//div[@class="tw-mb-[30px]"]/div[contains(@class, "tw-relative")]//div[contains('
                              '@class, "tw-mb-2")]/a/text()')
        # 林肯车型名字
        name_list = list[0:10:2].extract()
        # 对应的林肯车型的价格
        money_list = list[1:11:2].extract()
        for i in range(len(name_list)):
            name = name_list[i]
            money = money_list[i]
            print(name, money)
        pass
