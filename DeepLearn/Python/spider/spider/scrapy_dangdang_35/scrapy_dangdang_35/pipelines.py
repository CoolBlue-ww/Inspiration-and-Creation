# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdang35Pipeline:
    # 打开spider文件（执行之前）
    def open_spider(self, spider):
        self.fb = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fb.write(str(item))

        return item

    # 关闭spider文件（执行之后）
    def close_spider(self, spider):
        self.fb.close()


