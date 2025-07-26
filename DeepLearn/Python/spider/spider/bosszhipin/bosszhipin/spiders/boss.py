import scrapy
from scrapy_selenium import SeleniumRequest
from bosszhipin.items import BosszhipinItem


class BossSpider(scrapy.Spider):
    name = 'boss'

    def start_requests(self):
        url = 'https://www.baidu.com'
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            meta={
                'selenium': True,
                'selenium_actions': [
                    {
                        'type': 'input',
                        'selector': 'input#kw',
                        'text': 'boss直聘'
                    },
                    {
                        'type': 'click',
                        'selector': 'input#su'
                    },
                ]
            }
        )

    def parse(self, response):
        boss_url = response.xpath('//div[@has-tts="false"]/div[@sub-show="true"]/h3/a/@href').extract()[0]
        yield SeleniumRequest(
            url=boss_url,
            callback=self.parse_next,
            meta={
                'selenium': True,
                'final_wait': 10,
                'selenium_actions': [
                    {
                        'type': 'input',
                        'selector': 'input[name="query"]',
                        'text': '爬虫工程师'
                    },
                    {
                        'type': 'click',
                        'selector': 'button[class="btn btn-search"]'
                    }
                ]
            }
        )

    def parse_next(self, response):
        li_list = response.xpath('//div/ul[@class="job-list-box"]/li')
        jobName = li_list.xpath('.//div/a/div[contains(@class, "job-title")]/span[1]/text()').extract()
        jobPlace = li_list.xpath('.//div/a/div[contains(@class, "job-title")]/span[2]/span/text()').extract()
        jobMoney = li_list.xpath('.//div/a/div[contains(@class, "job-info")]/span[1]/text()').extract()
        jobAsk1 = li_list.xpath('.//div/a/div[contains(@class, "job-info")]/ul/li[1]/text()').extract()
        jobAsk2 = li_list.xpath('.//div/a/div[contains(@class, "job-info")]/ul/li[2]/text()').extract()
        jobHr = li_list.xpath('.//div/a/div[contains(@class, "job-info")]/div[contains(@class, "info-public")]/text()').extract()
        page = li_list.xpath('.//div/a/@href').extract()
        # for i in range(len(jobName)):
        #     name = jobName[i]
        #     money = jobMoney[i]
        #     place = jobPlace[i]
        #     ask1 = jobAsk1[i]
        #     ask2 = jobAsk2[i]
        #     ask = ask1 + ask2
        #     hr = jobHr[i]
        #     page_url = 'https://www.zhipin.com/' + page[i]
        #
        #     job = BosszhipinItem(name=name, money=money, place=place, ask=ask, hr=hr, page_url=page_url)
        #     yield job
        url = page[0]
        yield SeleniumRequest(
            url=url,
            callback=self.parse_page,
            meta={
                'selenium': True,
                'final_wait': 10,
            }
        )

    def parse_page(self, response):
        print(response.text)
