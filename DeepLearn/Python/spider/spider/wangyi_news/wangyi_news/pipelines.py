# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request
import hashlib

class WangyiNewsPipeline:
    def open_spider(self, spider):
        self.fb = open('new.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fb.write(str(item))
        return item

    def close_spider(self, spider):
        self.fb.close()


class ImagePipeline:
    def process_item(self, item, spider):

        for url in item['src']:
            if url:
                img_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
                urllib.request.urlretrieve(url=url, filename='./new_pictures/' + f"{img_hash}.png")
            else:
                pass
        return item

