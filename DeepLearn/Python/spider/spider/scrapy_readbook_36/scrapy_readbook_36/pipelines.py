# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyReadbook36Pipeline:
    def open_spider(self, spider):
        self.fb = open('books.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fb.write(str(item))
        return item

    def close_spider(self, spider):
        self.fb.close()


from scrapy.utils.project import get_project_settings
import pymysql


class MysqlPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        # MYSQL_HOST = "172.25.224.1"
        # MYSQL_PORT = 3306
        # MYSQL_USER = "root"
        # MYSQL_PASSWORD = "CKR_JAVASCRIPT_2005"
        # MYSQL_NAME = "spider36"
        # MYSQL_CHARSET = "utf-8"
        self.host = settings['MYSQL_HOST']
        self.port = settings['MYSQL_PORT']
        self.user = settings['MYSQL_USER']
        self.password = settings['MYSQL_PASSWORD']
        self.name = settings['MYSQL_NAME']
        self.charset = settings['MYSQL_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into book(name, author, text, src) values ("{}", "{}", "{}", "{}")'.format(item['name'],
                                                                                                 item['author'],
                                                                                                 item['text'],
                                                                                                 item['src'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
