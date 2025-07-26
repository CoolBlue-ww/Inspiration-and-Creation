# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request

class XiaomaoPipeline:
    def open_spider(self, spider):
        self.fb = open('xiaomao.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fb.write(str(item))
        return item

    def close_spider(self, spider):
        self.fb.close()


class ImageDownloadPipeline:
    def process_item(self, item, spider):
        for name in item['name_list']:
            for src in item['src_list']:
                url1 = 'https:' + src
                if url1[-1:-4:-1] == 'gpj':
                    url2 = url1[0:-6:1] + '.jpg'
                else:
                    url2 = url1[0:-6:1] + '.png'
                urllib.request.urlretrieve(url=url2, filename='./小猫素材/' + name + '.png')
