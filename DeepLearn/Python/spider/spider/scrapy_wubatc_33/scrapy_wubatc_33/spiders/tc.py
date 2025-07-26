import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["zhaoren.58.com"]
    start_urls = ["https://zhaoren.58.com/login#/"]

    def parse(self, response):
        print("欢迎来到五八同城登录！")
        print('======================================================================================')
        # 字符串
        # content = response.text
        # print(content)

        # 获取的是二进制数据
        # content = response.body
        # print(content)

        # 可以直接使用xpath来解析查找response的内容
        content = response.xpath('//div[@id="app"]')
        # 提取selector对象的data属性值  extract()
        # extract_first() 提取的是selector列表的第一个数据
        print(content.extract())
        pass
