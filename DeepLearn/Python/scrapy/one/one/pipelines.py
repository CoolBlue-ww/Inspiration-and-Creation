# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class OnePipeline:
    def open_spider(self, spider):
        self.fb = open('one.txt', 'w', encoding='utf-8')

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
        self.host = settings['MYSQL_HOST']
        self.port = settings['MYSQL_PORT']
        self.user = settings['MYSQL_USER']
        self.passwd = settings['MYSQL_PASSWORD']
        self.name = settings['MYSQL_NAME']
        self.charset = settings['MYSQL_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            charset=self.charset,
            db=self.name
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into xiaoshuo (title, text) values ("{}", "{}") '.format(item['title'], item['text'])

        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

