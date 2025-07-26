import scrapy
import json

class TextpostSpider(scrapy.Spider):
    name = "textpost"
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'javascript'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)
    def parse(self, response):
        content = response.text
        print(content)
        obj = json.loads(content)
        print(obj)